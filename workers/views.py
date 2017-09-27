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


def doRequest(postData, hostName, subUrl, method, header=None):
    params = urllib.parse.urlencode(postData)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    if header is not None:
        headers.update(header)
    conn = http.client.HTTPConnection(hostName)
    conn.request(method, subUrl, params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    conn.close()
    return data


def isOK(body):
    jsonObj = eval(body)
    if jsonObj['code'] == 0:
        return True
    else:
        return False


# trigger start here
def start(request):
    post = request.POST
    clubId = post.get('id')
    if clubId is None or not clubId.isdigit():
        return HttpResponse('ERROR')
    # prepare the user data
    sex = 1
    headerData = {'accesstoken': '', 'clientversion': '1.0', 'clientid': 'apitest', 'devicetype': '3'}
    userList = User.objects.filter(
        lastTime__gte=date.today()
    ).filter(
        lastTime__lte=date.today() + timedelta(days=1)
    ).filter(
        sex__exact=sex
    )
    random.shuffle(userList)
    user = userList[0]
    if user.isRegister == 0:
        postData = {}
        jsonData = doRequest(postData, HOST, REG_URL, 'POST', headerData)
        token = jsonData
        user.isRegister = 1
        jsonData['accesstoken'] = token
    else:
        postData = {}
        headerData = {}
        jsonData = doRequest(postData, HOST, LOGIN_URL, 'POST', headerData)
        token = jsonData
        jsonData['accesstoken'] = token

    user.lastTime = datetime.now()
    user.save()
    # prepare the fake data
    topicSentList = FinishedWork.objects.filter(
        theTime__gte=date.today() - timedelta(days=10)
    ).filter(
        theTime__lte=date.today()
    ).filter(
        type__exact=1
    ).filter(
        clubId__exact=clubId
    )
    # create new topic or give a comment
    isTopic = 1 or topicSentList.count() == 0
    topic = None
    comment = None
    if isTopic:
        topicList = Topic.objects.exclude(
            Q(lastTime__gte=date.today()), Q(lastTime__lte=date.today() + timedelta(days=1))
        ).filter(
            clubId__exact=clubId
        )
        random.shuffle(topicList)
        topic = topicList[0]
    else:
        commentList = Comment.objects.raw(
            'select b.* from workers_topic as a LEFT JOIN workers_comment as b on a.id = b.postsId_id WHERE a.clubId = %s and b.lastTime not between %s and %s',
            [clubId, date.today(), date.today() + timedelta(days=1)])
        random.shuffle(commentList)
        comment = commentList[0]
    # do the post
    url = POST_URL if isTopic else COMMENT_URL
    rawData = None
    if isTopic:
        postData = model_to_dict(topic)
        rawData = doRequest(postData, HOST, url, 'POST', headerData)
        topic.lastTime = datetime.now()
        topic.save()
    else:
        postData = comment.__dict__
        rawData = doRequest(postData, HOST, url, 'POST', headerData)
        comment.lastTime = datetime.now()
        comment.save()
    if isOK(rawData):
        objData = eval(rawData)
        typeValue = 0 if isTopic else 1
        idValue = topic.id if isTopic else comment.id
        fw = FinishedWork(type=typeValue, contentId=idValue, userId=user.id, theTime=datetime.now(),
                          idInServer=objData[''])
        fw.save()
    else:
        return HttpResponse('FAIL')
    return HttpResponse('OK')
