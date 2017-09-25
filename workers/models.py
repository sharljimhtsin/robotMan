from django.db import models

class TestModel(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
