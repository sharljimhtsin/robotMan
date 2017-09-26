from django.db import models


class TestModel(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=1)

    def __str__(self):
        return self.username


class Topic(models.Model):
    id = models.IntegerField(primary_key=1)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200)
    clubId = models.IntegerField(default=0)
    lastTime = models.DateTimeField(auto_now_add=1)


class Comment(models.Model):
    id = models.IntegerField(primary_key=1)
    postsId = models.ForeignKey(Topic, to_field='id')
    content = models.TextField(max_length=300)
    imageUrls = models.TextField(max_length=200)
    lastTime = models.DateTimeField(auto_now_add=1)


class FinishedWork(models.Model):
    id = models.IntegerField(primary_key=1)
    type = models.IntegerField(default=0)
    contentId = models.IntegerField(default=0)
    userId = models.IntegerField(default=0)
    theTime = models.DateTimeField(auto_now_add=1)


class User(models.Model):
    id = models.IntegerField(primary_key=1)
    username = models.TextField(max_length=10)
    password = models.TextField(max_length=20)
    nickname = models.TextField(max_length=10)
    avatar = models.TextField(max_length=20)
    birthday = models.DateTimeField()
    sex = models.IntegerField(default=1)
    signature = models.TextField(max_length=50)
    verifyCode = models.TextField(default='maimengmanhua', max_length=20)
    lastTime = models.DateTimeField(auto_now_add=1)
    isRegister = models.IntegerField(default=0)
