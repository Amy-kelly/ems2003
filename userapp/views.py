from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return HttpResponse("登陆成功")

def index(request):
    return

def demo(request):
    print("hello world")
    return HttpResponse("本次提交成功")