from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse("登陆成功")

def index(request):
    print("分支即便有误，切换到master也没有影响")
    return HttpResponse("强大的分支")

def demo(request):
    print("hello world")
    return HttpResponse("本次提交成功")