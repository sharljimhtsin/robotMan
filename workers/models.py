from __future__ import unicode_literals
from django.db import models


class TestModel(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=1)


class Topic(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200, null=1, blank=1, default='')
    clubId = models.IntegerField(default=0)
    lastTime = models.DateTimeField(auto_now=1)


class Comment(models.Model):
    postsId = models.ForeignKey(Topic)
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200, null=1, blank=1, default='')
    lastTime = models.DateTimeField(auto_now=1)


class FinishedWork(models.Model):
    type = models.IntegerField(default=0)
    contentId = models.IntegerField(default=0)
    userId = models.IntegerField(default=0)
    theTime = models.DateTimeField(auto_now_add=1)
    idInServer = models.IntegerField(default=0)


class User(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=100)
    nickname = models.TextField(max_length=10)
    avatar = models.TextField(max_length=20, null=1, blank=1, default='')
    birthday = models.DateTimeField()
    sex = models.IntegerField(default=1)
    signature = models.TextField(max_length=50)
    verifyCode = models.TextField(default='mmmh', max_length=20)
    lastTime = models.DateTimeField(auto_now=1)
    isRegister = models.IntegerField(default=0)
    idInServer = models.IntegerField(default=0)


class Variable(models.Model):
    keyName = models.TextField(max_length=30)
    keyValue = models.TextField(max_length=50)


# AUTO CODE
class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    qudao = models.CharField(max_length=255, blank=True, null=True)
    registertype = models.IntegerField(db_column='registerType')  # Field name made lowercase.
    avatar = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    sex = models.IntegerField()
    signature = models.CharField(max_length=50)
    ip = models.IntegerField()
    logintime = models.DateTimeField(db_column='loginTime', blank=True, null=True)  # Field name made lowercase.
    unionid = models.BigIntegerField(db_column='unionId')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Adimage(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=85)
    images = models.CharField(max_length=255)
    introduction = models.TextField()
    clickurl = models.CharField(db_column='clickUrl', max_length=255)  # Field name made lowercase.
    duration = models.SmallIntegerField()
    shownum = models.SmallIntegerField(db_column='showNum')  # Field name made lowercase.
    devicetype = models.CharField(db_column='deviceType', max_length=8)  # Field name made lowercase.
    customposition = models.SmallIntegerField(db_column='customPosition')  # Field name made lowercase.
    maxversionios = models.IntegerField(db_column='maxVersionIOS')  # Field name made lowercase.
    minversionios = models.IntegerField(db_column='minVersionIOS')  # Field name made lowercase.
    maxversionad = models.IntegerField(db_column='maxVersionAD')  # Field name made lowercase.
    minversionad = models.IntegerField(db_column='minVersionAD')  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='beginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    priority = models.IntegerField()
    clickcount = models.BigIntegerField(db_column='clickCount')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adimage'


class Appversion(models.Model):
    id = models.BigAutoField(primary_key=True)
    versioncode = models.IntegerField(db_column='versionCode')  # Field name made lowercase.
    versionname = models.IntegerField(db_column='versionName')  # Field name made lowercase.
    introduction = models.CharField(max_length=255)
    force = models.IntegerField()
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appversion'


class BindphoneLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.BigIntegerField()
    old_telephone = models.CharField(max_length=255, blank=True, null=True)
    new_telephone = models.CharField(max_length=255, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bindphone_log'


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    bannerimages = models.CharField(db_column='bannerImages', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    verticalimages = models.CharField(db_column='verticalImages', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    authorname = models.CharField(db_column='authorName', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    authorimages = models.CharField(db_column='authorImages', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    category = models.CharField(max_length=100)
    introduction = models.TextField()
    readmode = models.IntegerField(db_column='readMode')  # Field name made lowercase.
    length = models.IntegerField()
    updatetype = models.IntegerField(db_column='updateType')  # Field name made lowercase.
    updatevalue = models.CharField(db_column='updateValue', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    star = models.IntegerField()
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    sole = models.IntegerField()
    paid = models.IntegerField()
    showvolume = models.IntegerField(db_column='showVolume')  # Field name made lowercase.
    priority = models.BigIntegerField()
    defaultprice = models.IntegerField(db_column='defaultPrice', blank=True, null=True)  # Field name made lowercase.
    paidchapter = models.IntegerField(db_column='paidChapter', blank=True, null=True)  # Field name made lowercase.
    clubid = models.BigIntegerField(db_column='clubId')  # Field name made lowercase.
    thirdid = models.BigIntegerField(db_column='thirdId')  # Field name made lowercase.
    thirdupdatetime = models.DateTimeField(db_column='thirdUpdateTime', blank=True,
                                           null=True)  # Field name made lowercase.
    thirdsource = models.IntegerField(db_column='thirdSource')  # Field name made lowercase.
    checkstatus = models.SmallIntegerField(db_column='checkStatus')  # Field name made lowercase.
    isonline = models.IntegerField(db_column='isOnline')  # Field name made lowercase.
    status = models.SmallIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    ver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'book'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    cname = models.CharField(max_length=20)
    ename = models.CharField(max_length=20, blank=True, null=True)
    booktype = models.IntegerField(db_column='bookType')  # Field name made lowercase.
    images = models.CharField(max_length=255)
    introduction = models.TextField(blank=True, null=True)
    channel = models.IntegerField()
    usetype = models.IntegerField(db_column='useType')  # Field name made lowercase.
    ruletype = models.IntegerField(db_column='ruleType')  # Field name made lowercase.
    showmode = models.SmallIntegerField(db_column='showMode')  # Field name made lowercase.
    priority = models.BigIntegerField()
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    status = models.SmallIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    ver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category'


class Channel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    versioncode = models.IntegerField(db_column='versionCode')  # Field name made lowercase.
    versionname = models.IntegerField(db_column='versionName')  # Field name made lowercase.
    introduction = models.CharField(max_length=255)
    downloadurl = models.CharField(db_column='downloadUrl', max_length=255)  # Field name made lowercase.
    apkmd5 = models.CharField(db_column='apkMd5', max_length=50)  # Field name made lowercase.
    apksize = models.BigIntegerField(db_column='apkSize')  # Field name made lowercase.
    force = models.IntegerField()
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    appversionid = models.BigIntegerField(db_column='appVersionId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'channel'


class Chapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    chapterno = models.BigIntegerField(db_column='chapterNo')  # Field name made lowercase.
    showtime = models.DateTimeField(db_column='showTime')  # Field name made lowercase.
    point = models.IntegerField()
    paid = models.IntegerField()
    supportscorepay = models.IntegerField(db_column='supportScorePay')  # Field name made lowercase.
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    bookname = models.CharField(db_column='bookName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    booktype = models.IntegerField(db_column='bookType')  # Field name made lowercase.
    volumeid = models.BigIntegerField(db_column='volumeId')  # Field name made lowercase.
    volumename = models.CharField(db_column='volumeName', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    volumeno = models.BigIntegerField(db_column='volumeNo', blank=True, null=True)  # Field name made lowercase.
    thirdid = models.BigIntegerField(db_column='thirdId')  # Field name made lowercase.
    thirdupdatetime = models.DateTimeField(db_column='thirdUpdateTime', blank=True,
                                           null=True)  # Field name made lowercase.
    thirdsource = models.IntegerField(db_column='thirdSource')  # Field name made lowercase.
    checkstatus = models.SmallIntegerField(db_column='checkStatus')  # Field name made lowercase.
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    ver = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter'


class Chapterpraise(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId', blank=True, null=True)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientId', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    chapterid = models.BigIntegerField(db_column='chapterId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chapterpraise'


class Clickcount(models.Model):
    id = models.BigAutoField(primary_key=True)
    valuetype = models.IntegerField(db_column='valueType')  # Field name made lowercase.
    valueid = models.BigIntegerField(db_column='valueId')  # Field name made lowercase.
    clickcount = models.BigIntegerField(db_column='clickCount')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clickcount'


class Club(models.Model):
    id = models.BigAutoField(primary_key=True)
    originalname = models.CharField(db_column='originalName', max_length=255)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    images = models.CharField(max_length=255)
    introduction = models.TextField()
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'club'


class Clubhome(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=255)
    type = models.SmallIntegerField()
    shownum = models.IntegerField(db_column='showNum')  # Field name made lowercase.
    priority = models.SmallIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clubhome'


class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    booktype = models.BigIntegerField(db_column='bookType')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.SmallIntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collection'


class Comicchaptercontent(models.Model):
    chapterid = models.BigIntegerField(db_column='chapterId', primary_key=True)  # Field name made lowercase.
    images = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    format = models.CharField(max_length=10)
    originalsize = models.IntegerField(db_column='originalSize')  # Field name made lowercase.
    webpsize = models.IntegerField(db_column='webpSize')  # Field name made lowercase.
    supportwebp = models.IntegerField(db_column='supportWebp')  # Field name made lowercase.
    order = models.BigIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.
    ver = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comicchaptercontent'
        unique_together = (('chapterid', 'order'),)


class CommentServer(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    crccontent = models.BigIntegerField(db_column='crcContent', blank=True, null=True)  # Field name made lowercase.
    imageurls = models.TextField(db_column='imageUrls', blank=True, null=True)  # Field name made lowercase.
    valuetype = models.IntegerField(db_column='valueType')  # Field name made lowercase.
    valueid = models.BigIntegerField(db_column='valueId')  # Field name made lowercase.
    floor = models.BigIntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    viewtype = models.IntegerField(db_column='viewType')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    ip = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class Config(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.SmallIntegerField()
    value = models.TextField()
    desc = models.CharField(max_length=255, blank=True, null=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'config'


class Dailyclickreport(models.Model):
    date = models.DateField()
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    booktype = models.SmallIntegerField(db_column='bookType')  # Field name made lowercase.
    clickqty = models.BigIntegerField(db_column='clickQty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dailyclickreport'
        unique_together = (('date', 'bookid'),)


class Dailycollectreport(models.Model):
    date = models.DateField()
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    booktype = models.SmallIntegerField(db_column='bookType')  # Field name made lowercase.
    collectqty = models.BigIntegerField(db_column='collectQty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dailycollectreport'


class Device(models.Model):
    id = models.BigAutoField(primary_key=True)
    clientversion = models.CharField(db_column='clientVersion', max_length=10)  # Field name made lowercase.
    clientid = models.CharField(db_column='clientId', max_length=36, blank=True,
                                null=True)  # Field name made lowercase.
    crcclientid = models.BigIntegerField(db_column='crcClientId', blank=True, null=True)  # Field name made lowercase.
    devicetoken = models.CharField(db_column='deviceToken', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='deviceType')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'device'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Exceptcode(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    chinese = models.CharField(db_column='Chinese', max_length=255, blank=True, null=True)  # Field name made lowercase.
    japanese = models.CharField(db_column='Japanese', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    korean = models.CharField(db_column='Korean', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tw = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exceptcode'


class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    devicetoken = models.CharField(db_column='deviceToken', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='deviceType')  # Field name made lowercase.
    clientversion = models.CharField(db_column='clientVersion', max_length=255)  # Field name made lowercase.
    content = models.TextField()
    contact = models.CharField(max_length=255, blank=True, null=True)
    sessionid = models.BigIntegerField(db_column='sessionId')  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='parentId')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Informagainst(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    devicetoken = models.BigIntegerField(db_column='deviceToken')  # Field name made lowercase.
    valuetype = models.IntegerField(db_column='valueType')  # Field name made lowercase.
    valueid = models.BigIntegerField(db_column='valueId')  # Field name made lowercase.
    content = models.TextField()
    contact = models.CharField(max_length=255)
    ishandle = models.SmallIntegerField(db_column='isHandle')  # Field name made lowercase.
    handleuserid = models.BigIntegerField(db_column='handleUserId')  # Field name made lowercase.
    handletime = models.DateTimeField(db_column='handleTime')  # Field name made lowercase.
    againsttime = models.DateTimeField(db_column='againstTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'informagainst'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.IntegerField()
    reserved_at = models.IntegerField(blank=True, null=True)
    available_at = models.IntegerField()
    created_at = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class Notice(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    devicetoken = models.TextField(db_column='deviceToken')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    title = models.CharField(max_length=125)
    content = models.TextField()
    clickurl = models.TextField(db_column='clickUrl')  # Field name made lowercase.
    type = models.IntegerField()
    viewtype = models.SmallIntegerField(db_column='viewType')  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='sendTime')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notice'


class Novelchaptercontent(models.Model):
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    volumeid = models.BigIntegerField(db_column='volumeId')  # Field name made lowercase.
    chapterid = models.BigIntegerField(db_column='chapterId', primary_key=True)  # Field name made lowercase.
    wordcount = models.BigIntegerField(db_column='wordCount')  # Field name made lowercase.
    size = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'novelchaptercontent'


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    productid = models.BigIntegerField(db_column='productId')  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=255)  # Field name made lowercase.
    point = models.IntegerField()
    price = models.BigIntegerField()
    money = models.IntegerField()
    payway = models.IntegerField()
    thirdid = models.CharField(db_column='thirdId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField()
    remark = models.CharField(max_length=255)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Posts(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    title = models.CharField(max_length=255)
    cover = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    crccontent = models.BigIntegerField(db_column='crcContent', blank=True, null=True)  # Field name made lowercase.
    imageurls = models.TextField(db_column='imageUrls', blank=True, null=True)  # Field name made lowercase.
    authorname = models.TextField(db_column='authorName', blank=True, null=True)  # Field name made lowercase.
    istop = models.IntegerField(db_column='isTop')  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='beginTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    showtime = models.DateTimeField(db_column='showTime', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(max_length=255)
    level = models.IntegerField()
    viewcount = models.BigIntegerField(db_column='viewCount')  # Field name made lowercase.
    voteid = models.BigIntegerField(db_column='voteId')  # Field name made lowercase.
    clubid = models.BigIntegerField(db_column='clubId')  # Field name made lowercase.
    bookids = models.CharField(db_column='bookIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    isadmin = models.BigIntegerField(db_column='isAdmin')  # Field name made lowercase.
    ip = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    status = models.SmallIntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'posts'


class Prettyimages(models.Model):
    id = models.BigAutoField(primary_key=True)
    images = models.CharField(max_length=600)
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    size = models.IntegerField()
    format = models.CharField(max_length=30)
    label = models.CharField(max_length=255)
    showtime = models.DateTimeField(db_column='showTime')  # Field name made lowercase.
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    checkstatus = models.SmallIntegerField(db_column='checkStatus')  # Field name made lowercase.
    clubid = models.IntegerField(db_column='clubId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.IntegerField()
    remark = models.CharField(max_length=255)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prettyimages'


class Readhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    booktype = models.IntegerField(db_column='bookType')  # Field name made lowercase.
    chapterid = models.BigIntegerField(db_column='chapterId')  # Field name made lowercase.
    chapterno = models.BigIntegerField(db_column='chapterNo')  # Field name made lowercase.
    position = models.BigIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'readhistory'


class Recentupdate(models.Model):
    date = models.DateField(primary_key=True)
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    chapterid = models.BigIntegerField(db_column='chapterId')  # Field name made lowercase.
    chapterno = models.IntegerField(db_column='chapterNo')  # Field name made lowercase.
    sole = models.IntegerField()
    showtime = models.DateTimeField(db_column='showTime')  # Field name made lowercase.
    isappear = models.IntegerField(db_column='isAppear')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recentupdate'
        unique_together = (('date', 'bookid'),)


class Recharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    yearmonth = models.IntegerField(db_column='yearMonth')  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=255)  # Field name made lowercase.
    money = models.IntegerField()
    point = models.IntegerField()
    score = models.BigIntegerField()
    payway = models.IntegerField()
    devicetype = models.IntegerField(db_column='deviceType')  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId')  # Field name made lowercase.
    thirdorderid = models.CharField(db_column='thirdOrderId', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recharge'


class Recommend(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    type = models.SmallIntegerField()
    clickurl = models.CharField(db_column='clickUrl', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    position = models.SmallIntegerField()
    showmode = models.SmallIntegerField(db_column='showMode')  # Field name made lowercase.
    showvalue = models.IntegerField(db_column='showValue')  # Field name made lowercase.
    shownum = models.SmallIntegerField(db_column='showNum')  # Field name made lowercase.
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    priority = models.SmallIntegerField()
    extra = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recommend'


class Reply(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    commentid = models.BigIntegerField(db_column='commentId')  # Field name made lowercase.
    content = models.TextField()
    crccontent = models.BigIntegerField(db_column='crcContent', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=255, blank=True, null=True)
    ip = models.IntegerField()
    parentuserid = models.BigIntegerField(db_column='parentUserId')  # Field name made lowercase.
    parentid = models.BigIntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.SmallIntegerField()
    viewtype = models.IntegerField(db_column='viewType')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reply'


class Search(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    values = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search'


class Searchhistory(models.Model):
    type = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    searchqty = models.BigIntegerField(db_column='searchQty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'searchhistory'


class Smsverify(models.Model):
    id = models.BigAutoField(primary_key=True)
    telephone = models.CharField(max_length=255)
    verifycode = models.CharField(db_column='verifyCode', max_length=4)  # Field name made lowercase.
    sendtype = models.SmallIntegerField(db_column='sendType')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.IntegerField()
    sendtime = models.DateTimeField(db_column='sendTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'smsverify'


class Submissionworks(models.Model):
    id = models.BigAutoField(primary_key=True)
    comics_name = models.CharField(max_length=255)
    works_name = models.CharField(max_length=255)
    comics_type = models.SmallIntegerField()
    plot_type = models.SmallIntegerField()
    plot_desc = models.CharField(max_length=6144)
    cover_img = models.CharField(max_length=255)
    sub_mirror = models.TextField()
    to_produce = models.TextField()
    status = models.SmallIntegerField()
    user_id = models.BigIntegerField()
    id_submit = models.SmallIntegerField()
    praise = models.BigIntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'submissionworks'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    occ = models.BigIntegerField()
    priority = models.SmallIntegerField()
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tags'


class Test(models.Model):
    keywords = models.CharField(max_length=255)
    searchqty = models.CharField(db_column='searchQty', max_length=11, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'


class TopicServer(models.Model):
    id = models.BigAutoField(primary_key=True)
    booktype = models.IntegerField(db_column='bookType')  # Field name made lowercase.
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    images = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    introduction = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    sourcetype = models.IntegerField(db_column='sourceType')  # Field name made lowercase.
    sourcevalue = models.CharField(db_column='sourceValue', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    offstatus = models.IntegerField(db_column='offStatus')  # Field name made lowercase.
    priority = models.BigIntegerField()
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic'


class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    yearmonth = models.IntegerField(db_column='yearMonth')  # Field name made lowercase.
    point = models.IntegerField()
    score = models.IntegerField()
    chapterid = models.BigIntegerField(db_column='chapterId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    devicetype = models.IntegerField(db_column='deviceType')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transaction'


class UserServer(models.Model):
    id = models.BigAutoField(primary_key=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    sex = models.IntegerField()
    signature = models.CharField(max_length=50)
    qudao = models.CharField(max_length=255, blank=True, null=True)
    registertype = models.IntegerField(db_column='registerType')  # Field name made lowercase.
    level = models.IntegerField()
    enableemchat = models.IntegerField(db_column='enableEmChat')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Userclub(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    clubid = models.BigIntegerField(db_column='clubId')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userclub'


class Userconcern(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    concernuserid = models.BigIntegerField(db_column='concernUserId')  # Field name made lowercase.
    status = models.SmallIntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userconcern'


class Userpraise(models.Model):
    id = models.BigAutoField(primary_key=True)
    valuetype = models.IntegerField(db_column='valueType')  # Field name made lowercase.
    valueid = models.BigIntegerField(db_column='valueId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId', blank=True, null=True)  # Field name made lowercase.
    viewtype = models.SmallIntegerField(db_column='viewType')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userpraise'


class Userrank(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    images = models.CharField(max_length=255)
    introduction = models.TextField()
    top = models.SmallIntegerField()
    priority = models.BigIntegerField()
    status = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userrank'


class Userscore(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.SmallIntegerField()
    score = models.BigIntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userscore'


class Userscorerule(models.Model):
    scoretype = models.SmallIntegerField(db_column='scoreType', primary_key=True)  # Field name made lowercase.
    score = models.IntegerField()
    toplimit = models.IntegerField(db_column='topLimit')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userscorerule'


class Uservote(models.Model):
    id = models.BigAutoField(primary_key=True)
    voteid = models.BigIntegerField(db_column='voteId')  # Field name made lowercase.
    voteitemids = models.CharField(db_column='voteItemIds', max_length=50)  # Field name made lowercase.
    deviceid = models.BigIntegerField(db_column='deviceId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uservote'


class Volume(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    volumeno = models.BigIntegerField(db_column='volumeNo')  # Field name made lowercase.
    bookid = models.BigIntegerField(db_column='bookId')  # Field name made lowercase.
    bookname = models.CharField(db_column='bookName', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    status = models.IntegerField()
    ver = models.IntegerField()
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volume'


class Vote(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    introduction = models.TextField()
    choicetype = models.IntegerField(db_column='choiceType')  # Field name made lowercase.
    showtype = models.IntegerField(db_column='showType')  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='beginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    status = models.SmallIntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vote'


class Voteitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    images = models.CharField(max_length=255)
    voteqty = models.BigIntegerField(db_column='voteQty')  # Field name made lowercase.
    order = models.SmallIntegerField()
    voteid = models.BigIntegerField(db_column='voteId')  # Field name made lowercase.
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    status = models.IntegerField()
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='modifyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'voteitem'
