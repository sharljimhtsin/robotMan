from django.contrib import admin
from .models import TestModel, Topic, Comment, FinishedWork, User, Variable

# Register your models here.
admin.site.register(TestModel)
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(FinishedWork)
admin.site.register(User)
admin.site.register(Variable)
