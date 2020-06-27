from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def login(request):
    return HttpResponse("登陆成功")

def index(request):
    return

def demo(request):
    print("hello world")
    return HttpResponse("本次提交成功")

class UserView(View):
    pass