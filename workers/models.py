from django.db import models


class TestModel(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=1)


class Topic(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200, null=1, blank=1)
    clubId = models.IntegerField(default=0)
    lastTime = models.DateTimeField(auto_now=1)


class Comment(models.Model):
    postsId = models.ForeignKey(Topic)
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200, null=1, blank=1)
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
    avatar = models.TextField(max_length=20, null=1, blank=1)
    birthday = models.DateTimeField()
    sex = models.IntegerField(default=1)
    signature = models.TextField(max_length=50)
    verifyCode = models.TextField(default='mmmh', max_length=20)
    lastTime = models.DateTimeField(auto_now=1)
    isRegister = models.IntegerField(default=0)
