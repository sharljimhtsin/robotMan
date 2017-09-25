from django.shortcuts import render
from django.http import HttpResponse
from workers.models import TestModel


def index(request):
    data = TestModel.objects.all()
    print(data)
    resp = "".join(m.__str__() for m in data)
    return HttpResponse("hello world" + resp)


def doTest(request):
    return HttpResponse('hahahah')


def doPost(postData, hostName, subUrl):
    import http.client, urllib.parse
    params = urllib.parse.urlencode(postData)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(hostName)
    conn.request("POST", subUrl, params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    conn.close()
