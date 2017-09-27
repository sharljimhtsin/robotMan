from django.shortcuts import render
from django.http import HttpResponse
from workers.models import TestModel, Topic, Comment, User, FinishedWork
from datetime import datetime, timedelta, time, date
from django.forms.models import model_to_dict
from django.db.models import Q
import http.client, urllib.parse
import random


def index(request):
    print(request.GET)
    data = TestModel.objects.all()
    print(model_to_dict(data[0]))
    print(data[0].__dict__)
    data = {'a': 'bbbb'}
    print(data)
    resp = doRequest({}, "baidu.com:80", "/aaa", 'POST', {})
    print(resp)
    resp = "".join(m.__str__() for m in data)
    tmp = Comment.objects.raw(
        'select a.* from workers_comment as a LEFT JOIN workers_topic as b on a.postsId_id = b.title WHERE b.id = %s or b.id = %s',
        [5, 1])
    print(tmp.__dict__)
    for row in tmp:
        print(row.__dict__)
    return HttpResponse("hello world" + resp)


def doTest(request):
    return HttpResponse('hahahah')


HOST = 'api-test.maimengjun.com:80'
POST_URL = '/posts/publish'
COMMENT_URL = '/comment/commentPost'
LOGIN_URL = '/login'
REG_URL = '/register'
TOPIC_RATE = 1
COMMENT_RATE = 2
HEADER_DATA = {'accesstoken': '', 'clientversion': '1.0', 'clientid': 'apitest', 'devicetype': '3'}


def doRequest(postData, hostName, subUrl, method, header=None):
    params = urllib.parse.urlencode(postData)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    if header is not None:
        headers.update(header)
    conn = http.client.HTTPConnection(hostName)
    conn.request(method, subUrl, params, headers)
    response = conn.getresponse()
    data = response.read()
    print(response.status, response.reason, data)
    conn.close()
    return data


def isOK(body):
    jsonObj = eval(body)
    if jsonObj['code'] == 0:
        return True
    else:
        return False


def sendTopic(topic, headerData):
    postData = model_to_dict(topic)
    rawData = doRequest(postData, HOST, POST_URL, 'POST', headerData)
    topic.lastTime = datetime.now()
    topic.save()
    return rawData


def sendComment(comment, headerData, followerId):
    postData = comment.__dict__
    postData['postsId'] = followerId
    rawData = doRequest(postData, HOST, COMMENT_URL, 'POST', headerData)
    comment.lastTime = datetime.now()
    comment.save()
    return rawData


def saveJob(rawData, isTopic, element, user):
    objData = eval(rawData)
    typeValue = 1 if isTopic else 0
    idValue = element.id
    idInServer = objData['data']['id']
    fw = FinishedWork(type=typeValue, contentId=idValue, userId=user.id, theTime=datetime.now(),
                      idInServer=idInServer)
    fw.save()
    return True


def randomBool():
    return random.random() < 0.5


def pickUser():
    sex = 1 if randomBool() else 0
    userList = User.objects.exclude(
        Q(lastTime__gte=date.today()), Q(lastTime__lte=date.today() + timedelta(days=1))
    ).filter(
        sex__exact=sex
    )
    random.shuffle(userList)
    print(userList, sex)
    user = userList[0]
    return user


def getToken(user):
    if user.isRegister == 0:
        postData = model_to_dict(user)
        jsonData = doRequest(postData, HOST, REG_URL, 'POST', HEADER_DATA)
        if isOK(jsonData):
            token = eval(jsonData)['data']['token']
            HEADER_DATA['accesstoken'] = token
            user.isRegister = 1
            user.lastTime = datetime.now()
            user.save()
            return True
        else:
            return False
    else:
        postData = model_to_dict(user)
        jsonData = doRequest(postData, HOST, LOGIN_URL, 'POST', HEADER_DATA)
        if isOK(jsonData):
            token = eval(jsonData)['meta']['token']
            HEADER_DATA['accesstoken'] = token
            user.lastTime = datetime.now()
            user.save()
            return True
        else:
            return False


def checkTopicOrNot(clubId):
    topicSentList = FinishedWork.objects.raw(
        'select a.* from workers_finishedwork AS a LEFT JOIN workers_topic AS b ON a.contentId = b.id WHERE a.theTime BETWEEN %s AND %s AND a.type = 1 AND b.clubId = %s',
        [date.today() - timedelta(days=10), date.today(), clubId])
    return randomBool() or topicSentList.count() == 0, topicSentList


def pickElement(isTopic, clubId):
    if isTopic:
        topicList = Topic.objects.exclude(
            Q(lastTime__gte=date.today()), Q(lastTime__lte=date.today() + timedelta(days=1))
        ).filter(
            clubId__exact=clubId
        )
        random.shuffle(topicList)
        return topicList[0]
    else:
        commentList = Comment.objects.raw(
            'select b.* from workers_topic AS a LEFT JOIN workers_comment AS b ON a.id = b.postsId_id WHERE a.clubId = %s AND b.lastTime NOT BETWEEN %s AND %s',
            [clubId, date.today(), date.today() + timedelta(days=1)])
        random.shuffle(commentList)
        return commentList[0]


# trigger start here
def start(request):
    post = request.POST
    clubId = post.get('id')
    # check parameter
    if clubId is None or not clubId.isdigit():
        return HttpResponse('ERROR')
    # prepare the user data
    user = pickUser()
    if getToken(user) is False:
        return HttpResponse("ERROR")

    # create new topic or give a comment
    isTopic, mainList = checkTopicOrNot(clubId)
    print(isTopic, mainList)
    # do the post
    if isTopic:
        for i in range(0, TOPIC_RATE):
            # prepare the fake data
            element = pickElement(isTopic, clubId)
            rawData = sendTopic(element, HEADER_DATA)
            if isOK(rawData):
                saveJob(rawData, isTopic, element, user)
            else:
                return HttpResponse('ERROR')
    else:
        for i in range(0, COMMENT_RATE):
            # prepare the fake data
            random.shuffle(mainList)
            postId = mainList[0]['idInServer']
            element = pickElement(isTopic, clubId)
            rawData = sendComment(element, HEADER_DATA, postId)
            if isOK(rawData):
                saveJob(rawData, isTopic, element, user)
            else:
                return HttpResponse('ERROR')

    return HttpResponse('OK')
