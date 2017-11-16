from django.shortcuts import render
from django.http import HttpResponse
from workers.models import TestModel, Topic, Comment, User, FinishedWork, Variable, UserServer, \
    CommentServer, Posts, Book
from datetime import datetime, timedelta, time, date
from django.forms.models import model_to_dict
from django.db.models import Q
import http.client, urllib.parse
import random, copy, time
from xlrd import open_workbook
from zlib import crc32
from django.utils import timezone
import pytz
from bs4 import BeautifulSoup
import logging
import threading
from . import scheduler
import uuid

logger = logging.getLogger('fileLog')


def index(request):
    logger.debug("test log 1")
    logger.info("test log 2")
    logger.error("test log 3")
    logger.critical("test log 4")
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
    '''
    obj = Variable.objects.get(keyName='trigger_rate')
    print(model_to_dict(obj))
    obj = CommentServer.objects.using('maimeng').all()
    for o in obj:
        print(model_to_dict(o))
        break
    obj = Comment.objects.all()
    for o in obj:
        print(model_to_dict(o))
        break
    '''
    jobs = scheduler.get_instance()
    if jobs.running is False:
        jobs.remove_all_jobs('default')
        jobs.remove_jobstore('default')
        jobs.start()

    do_time = datetime.now() + timedelta(minutes=1)
    jobs.add_job(randomBool, 'date', run_date=do_time, args=[1.00])
    print(jobs.get_jobs())
    # count = sum(int(randomBool(0.70)) for i in range(10000))
    # print(count)
    # timer = threading.Timer(5, randomBool, [1.00])
    # timer.start()
    return HttpResponse('hahahah')


HOST = 'api-test.maimengjun.com:80'
POST_URL = '/posts/publish'
COMMENT_URL = '/comment/commentPost'
LOGIN_URL = '/login'
REG_URL = '/register'
TOPIC_RATE = 1
COMMENT_RATE = 2
TRIGGER_RATE = 0.5
SEX_RATE = 0.5
TOPIC_OR_COMMENT_RATE = 0.5
RUN_DELAY_MIN = 0
HEADER_DATA = {'accesstoken': '', 'clientversion': '1.0', 'clientid': 'apitest', 'devicetype': '3'}


def getVariableByKey(key):
    obj = None
    try:
        obj = Variable.objects.get(keyName=key)
    except Variable.DoesNotExist:
        obj = None
    if obj is None:
        return None
    else:
        dictObj = model_to_dict(obj)
        value = dictObj['keyValue']
        if value.strip() == '':
            return None
        else:
            return value


def initVariable():
    global HOST, TOPIC_RATE, COMMENT_RATE, TRIGGER_RATE, SEX_RATE, TOPIC_OR_COMMENT_RATE, RUN_DELAY_MIN
    HOST = getVariableByKey('host') if getVariableByKey('host') is not None else HOST
    TOPIC_RATE = int(getVariableByKey('topic_rate')) if getVariableByKey('topic_rate') is not None else TOPIC_RATE
    COMMENT_RATE = int(getVariableByKey('comment_rate')) if getVariableByKey(
        'comment_rate') is not None else COMMENT_RATE
    TRIGGER_RATE = float(getVariableByKey('trigger_rate')) if getVariableByKey(
        'trigger_rate') is not None else TRIGGER_RATE
    SEX_RATE = float(getVariableByKey('sex_rate')) if getVariableByKey('sex_rate') is not None else SEX_RATE
    TOPIC_OR_COMMENT_RATE = float(getVariableByKey('topic_or_comment_rate')) if getVariableByKey(
        'topic_or_comment_rate') is not None else TOPIC_OR_COMMENT_RATE
    RUN_DELAY_MIN = int(getVariableByKey('run_delay_min')) if getVariableByKey(
        'run_delay_min') is not None else RUN_DELAY_MIN
    return True


def doRequest(postData, hostName, subUrl, method, header=None):
    time.sleep(3)  # sleep seconds for avoid server-side ban
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


def get_local_datetime():
    return datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M:%S')


def sendTopic(topic, headerData):
    postData = copy.deepcopy(topic)
    postData.pop('id', None)
    rawData = doRequest(postData, HOST, POST_URL, 'POST', headerData)
    updateObj = Topic.objects.get(pk=topic['id'])
    updateObj.lastTime = get_local_datetime()
    updateObj.save()
    return rawData


def sendTopicViaDB(topic, user, createtime=get_local_datetime()):
    rawData = Posts.objects.using('maimeng').create(
        type=0,
        title=topic['title'],
        content=topic['content'],
        crccontent=crc32(str.encode(topic['content'])),  # crc16.crc16xmodem(str.encode(topic['content'])),
        imageurls=topic['imageUrls'],
        istop=0,
        label='',
        level=0,
        viewcount=0,
        voteid=0,
        clubid=topic['clubId'],
        userid=user['id'],
        isadmin=3,
        ip=0,
        offstatus=0,
        status=1,
        showtime=get_local_datetime(),
        createtime=createtime,
        modifytime=get_local_datetime()
    )
    updateObj = Topic.objects.get(pk=topic['id'])
    updateObj.lastTime = get_local_datetime()
    updateObj.save()
    return model_to_dict(rawData)


def sendComment(comment, headerData, followerId):
    postData = copy.deepcopy(comment)
    postData['postsId'] = followerId
    postData.pop('id', None)
    rawData = doRequest(postData, HOST, COMMENT_URL, 'POST', headerData)
    updateObj = Comment.objects.get(pk=comment['id'])
    updateObj.lastTime = get_local_datetime()
    updateObj.save()
    return rawData


def sendCommentViaDB(comment, user, followerId, createtime=get_local_datetime()):
    comment['postsId'] = followerId
    rawData = CommentServer.objects.using('maimeng').create(
        content=comment['content'],
        imageurls=comment['imageUrls'],
        valuetype=1,
        valueid=followerId,
        floor=1,
        status=1,
        viewtype=1,
        userid=user['id'],
        ip=0,
        createtime=createtime,
        modifytime=get_local_datetime(),
        crccontent=crc32(str.encode(comment['content']))
    )
    updateObj = Comment.objects.get(pk=comment['id'])
    updateObj.lastTime = get_local_datetime()
    updateObj.save()
    return model_to_dict(rawData)


def saveJob(rawData, isTopic, element, user, clubId, isDB=0):
    idInServer = 0
    if isDB == 0:
        objData = eval(rawData)
        idInServer = objData['data']['id']
    else:
        idInServer = rawData['id']
    typeValue = 1 if isTopic else 0
    idValue = element['id']
    fw = FinishedWork(type=typeValue, contentId=idValue, userId=user['id'], theTime=get_local_datetime(),
                      idInServer=idInServer, clubId=clubId)
    fw.save()
    return True


def randomBool(rate=0.5):
    return random.random() < rate


def pick_user():
    sex = 1 if randomBool(SEX_RATE) else 2
    user_list = UserServer.objects.using('maimeng').filter(
        id__range=(2000001, 2010000)
    ).filter(
        sex__exact=sex
    ).order_by(
        'modifytime'
    )[:10]
    print(user_list, sex, 'user_list & sex')
    user_list = querySetToDict(user_list)
    random.shuffle(user_list)
    user = None if len(user_list) == 0 else user_list[0]
    return user


def pickUser():
    sex = 1 if randomBool(SEX_RATE) else 0
    userList = User.objects.exclude(
        Q(lastTime__gte=date.today()), Q(lastTime__lte=date.today() + timedelta(days=1))
    ).filter(
        sex__exact=sex
    )
    print(userList, sex)
    userList = querySetToDict(userList)
    random.shuffle(userList)
    user = None if len(userList) == 0 else userList[0]
    return user


def getToken(user):
    global HEADER_DATA
    postData = user
    if user['isRegister'] == 0:
        jsonData = doRequest(postData, HOST, REG_URL, 'POST', HEADER_DATA)
        if isOK(jsonData):
            token = eval(jsonData)['meta']['token']
            HEADER_DATA['accesstoken'] = token
            updateObj = User.objects.get(pk=user['id'])
            updateObj.isRegister = 1
            updateObj.lastTime = get_local_datetime()
            updateObj.save()
            return True
        else:
            return False
    else:
        jsonData = doRequest(postData, HOST, LOGIN_URL, 'POST', HEADER_DATA)
        if isOK(jsonData):
            token = eval(jsonData)['meta']['token']
            HEADER_DATA['accesstoken'] = token
            updateObj = User.objects.get(pk=user['id'])
            updateObj.lastTime = get_local_datetime()
            updateObj.save()
            return True
        else:
            return False


def needRegister(user):
    if user['isRegister'] == 0:
        obj = UserServer.objects.using("maimeng").create(
            nickname=user['nickname'],
            sex=user['sex'],
            signature=user['signature'],
            registertype=1,
            level=1,
            enableemchat=1,
            status=1)
        if obj is not None:
            updateObj = User.objects.get(pk=user['id'])
            updateObj.isRegister = 1
            updateObj.idInServer = obj.id
            updateObj.lastTime = get_local_datetime()
            updateObj.save()
            return updateObj.idInServer
        else:
            return 0
    else:
        updateObj = User.objects.get(pk=user['id'])
        updateObj.lastTime = get_local_datetime()
        updateObj.save()
        return updateObj.idInServer


def checkTopicOrNot(clubId=0):
    topicSentList = FinishedWork.objects.raw(
        'select a.* from workers_finishedwork AS a LEFT JOIN workers_topic AS b ON a.contentId = b.id WHERE a.theTime BETWEEN %s AND %s AND a.type = 1 AND a.clubId = %s',
        [date.today() - timedelta(days=10), date.today() + timedelta(days=1), clubId])
    return randomBool(TOPIC_OR_COMMENT_RATE) or len(list(topicSentList)) == 0, rawQuerySetToDict(topicSentList)


def rawQuerySetToDict(rawData):
    list = []
    for row in rawData:
        list.append(row.__dict__)
    return list


def querySetToDict(rawData):
    list = []
    for row in rawData:
        list.append(model_to_dict(row))
    return list


def pickElement(is_topic, post_id=0, club_id=0):
    if is_topic:
        topicList = Topic.objects.exclude(
            Q(lastTime__gte=date.today()), Q(lastTime__lte=date.today() + timedelta(days=1))
        ).filter(
            clubId__exact=club_id
        )
        topicList = querySetToDict(topicList)
        random.shuffle(topicList)
        return None if len(topicList) == 0 else topicList[0]
    else:
        commentList = Comment.objects.raw(
            'select b.* from workers_topic AS a LEFT JOIN workers_comment AS b ON a.id = b.postsId_id WHERE a.clubId = %s AND a.id = %s AND b.lastTime NOT BETWEEN %s AND %s',
            [club_id, post_id, date.today(), date.today() + timedelta(days=1)])
        commentList = rawQuerySetToDict(commentList)
        random.shuffle(commentList)
        return None if len(commentList) == 0 else commentList[0]


def parseExcel(request):
    fileName = 'excel.xlsx'
    wb = open_workbook(fileName)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols
        items = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value = (sheet.cell(row, col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
            item = values
            items.append(item)

    for item in items:
        saveTopicAndComment(item)
    return HttpResponse("OK")


def saveTopicAndComment(items):
    isTopic = False
    isTopicContent = False
    isComment = False
    currentIndex = 0
    postObj = None
    title = ''
    content = ''
    comment = ''
    for item in items:
        if item == '':
            continue
        currentIndex += 1
        isTopic = True if currentIndex == 1 else False
        isTopicContent = True if currentIndex == 2 else False
        isComment = True if currentIndex > 2 else False
        if (isTopic):
            title = item
        elif (isTopicContent):
            content = item
            postObj = Topic.objects.create(title=title, content=content)
        elif (isComment):
            comment = item
            Comment.objects.create(postsId=postObj, content=comment)
        else:
            continue
    return True


# trigger start here
def start(request):
    post = request.POST
    clubId = post.get('id')
    # check parameter
    if clubId is None or not clubId.isdigit():
        logger.error("clubId error")
        return HttpResponse('ERROR')

    initVariable()
    trigger_rate = TRIGGER_RATE > random.random()
    if trigger_rate is False:
        return HttpResponse("SKIP")

    # prepare the user data
    user = pickUser()
    if user is None or getToken(user) is False:
        logger.error("user error")
        return HttpResponse("ERROR")

    # create new topic or give a comment
    isTopic, mainList = checkTopicOrNot()
    print(isTopic, mainList)
    # do the post
    if isTopic:
        for i in range(0, TOPIC_RATE):
            # prepare the fake data
            element = pickElement(isTopic)
            element['clubId'] = clubId
            if element is None:
                logger.error("topic error")
                return HttpResponse('ERROR')

            rawData = sendTopic(element, HEADER_DATA)
            if isOK(rawData):
                saveJob(rawData, isTopic, element, user)
            else:
                logger.error("save topic error")
                return HttpResponse('ERROR')
    else:
        for i in range(0, COMMENT_RATE):
            # prepare the fake data
            random.shuffle(mainList)
            postId = mainList[0]['idInServer']
            element = pickElement(isTopic)
            if element is None:
                logger.error("comment error")
                return HttpResponse('ERROR')

            rawData = sendComment(element, HEADER_DATA, postId)
            if isOK(rawData):
                saveJob(rawData, isTopic, element, user)
            else:
                logger.error("save comment error")
                return HttpResponse('ERROR')

    return HttpResponse('OK')


# trigger start here
def start_fork(request):
    post = request.POST
    clubId = post.get('id')
    # check parameter
    if clubId is None or not clubId.isdigit():
        return HttpResponse('ERROR')

    initVariable()
    trigger_rate = TRIGGER_RATE > random.random()
    if trigger_rate is False:
        return HttpResponse("SKIP")

    # prepare the user data
    user = pickUser()
    if user is None or needRegister(user) == 0:
        return HttpResponse("ERROR")

    # create new topic or give a comment
    isTopic, mainList = checkTopicOrNot()
    print(isTopic, mainList)
    # do the post
    if isTopic:
        for i in range(0, TOPIC_RATE):
            # prepare the fake data
            element = pickElement(isTopic)
            element['clubId'] = clubId
            if element is None:
                return HttpResponse('ERROR')

            rawData = sendTopicViaDB(element, user)
            if rawData is not None:
                saveJob(rawData, isTopic, element, user, 1)
            else:
                return HttpResponse('ERROR')
    else:
        for i in range(0, COMMENT_RATE):
            # prepare the fake data
            random.shuffle(mainList)
            postId = mainList[0]['idInServer']
            element = pickElement(isTopic)
            if element is None:
                return HttpResponse('ERROR')

            rawData = sendCommentViaDB(element, user, postId)
            if rawData is not None:
                saveJob(rawData, isTopic, element, user, 1)
            else:
                return HttpResponse('ERROR')

    return HttpResponse('OK')


def skip_or_not(club_id):
    objects = Book.objects.using('maimeng').filter(
        type__exact=1
    ).filter(
        clubid=club_id
    )
    maps = querySetToDict(objects)
    return True if len(maps) == 0 else False


def run_topic_further(element, user, isTopic, clubId, create_time):
    rawData = sendTopicViaDB(element, user, create_time)
    if rawData is not None:
        saveJob(rawData, isTopic, element, user, clubId, 1)
        logger.debug('run_topic_further @ ' + get_local_datetime())
    else:
        logger.error("save topic error")
    return True


def run_comment_further(element, user, isTopic, clubId, postId, create_time):
    rawData = sendCommentViaDB(element, user, postId, create_time)
    if rawData is not None:
        saveJob(rawData, isTopic, element, user, clubId, 1)
        logger.debug('run_comment_further @ ' + get_local_datetime())
    else:
        logger.error("save comment error")
    return True


def init_or_get_scheduler():
    jobs = scheduler.get_instance()
    if jobs.running is False:
        jobs.remove_all_jobs('default')
        jobs.remove_jobstore('default')
        jobs.start()
    print(jobs.get_jobs())
    return jobs


def get_random_create_time():
    # 随机数关系2：实时（+0）：未来1天（+1）：未来2天（+2）：未来3天（+3）=3：2：2：3
    rate_map = [0.3, 0.2, 0.2, 0.3]
    time_map = [0, 1, 2, 3]
    i = random.random()
    j = 0
    k = -1
    for rate in rate_map:
        j += rate
        k += 1
        if j >= i:
            break

    days = time_map[k]
    print(days, k)
    return datetime.now() + timedelta(days=days)


# trigger start here
def start_fork_again(request):
    post = request.POST
    clubId = post.get('id')
    # check parameter
    if clubId is None or not clubId.isdigit():
        logger.error("clubId error")
        return HttpResponse('ERROR')

    # check parameter
    if skip_or_not(clubId):
        logger.error("clubId skip")
        return HttpResponse('SKIP')

    initVariable()
    trigger_rate = TRIGGER_RATE > random.random()
    if trigger_rate is False:
        return HttpResponse("SKIP")

    # prepare the user data
    user = pick_user()
    if user is None:
        logger.error("user error")
        return HttpResponse("ERROR")

    # create new topic or give a comment
    isTopic, mainList = checkTopicOrNot(clubId)
    print(isTopic, mainList, 'isTopic & mainList')
    # do the post
    if isTopic:
        for i in range(0, TOPIC_RATE):
            # prepare the fake data
            element = pickElement(isTopic)
            element['clubId'] = clubId
            if element is None:
                logger.error("topic error")
                return HttpResponse('ERROR')

            jobs = init_or_get_scheduler()
            do_time = get_random_create_time()
            print(do_time)
            jobs.add_job(run_topic_further, 'date', run_date=do_time,
                         args=[element, user, isTopic, clubId, get_local_datetime()],
                         id=uuid.uuid1().__str__())
            update_obj = Topic.objects.get(pk=element['id'])
            update_obj.lastTime = get_local_datetime()
            update_obj.save()

    else:
        for i in range(0, COMMENT_RATE):
            # prepare the fake data
            random.shuffle(mainList)
            post_id = mainList[0]['idInServer']
            source_id = mainList[0]['contentId']
            element = pickElement(isTopic, source_id)
            print(element, source_id, 'element & source_id')
            if element is None:
                logger.error("comment error")
                return HttpResponse('ERROR')

            jobs = init_or_get_scheduler()
            do_time = get_random_create_time()
            print(do_time)
            jobs.add_job(run_comment_further, 'date', run_date=do_time,
                         args=[element, user, isTopic, clubId, post_id, get_local_datetime()],
                         id=uuid.uuid1().__str__())
            update_obj = Comment.objects.get(pk=element['id'])
            update_obj.lastTime = get_local_datetime()
            update_obj.save()

    update_obj = UserServer.objects.using('maimeng').get(pk=user['id'])
    update_obj.modifytime = get_local_datetime()
    update_obj.save()
    return HttpResponse('OK')
