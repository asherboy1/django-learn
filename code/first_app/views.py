from django.http import HttpResponse
from django.shortcuts import render, redirect
from first_app.models import UserInfo


# 这个view层展示欢迎页面 与 登录逻辑
# Create your views here.
def test(request, **kwargs):
    return HttpResponse("this is test")

def welcome(request):
    return redirect('/firstapp/login')

def login(request, **kwargs):
    if request.method.lower() == "get":
        return render(request, "welcome.html")
    else:
        username = request.POST.get("username", None)
        if not username:  
            return render(request, "welcome.html", context={"error_msg": "登录失败,用户名为空"}, status=200) 
 
        password = request.POST.get("password", None)
        if not password:
            return render(request, "welcome.html",context={"error_msg": "登录失败,密码为空"}, status=200) 
    # 初始化对象
    UserInfo_base = UserInfo.objects
    # 判断用户登录信息
    if UserInfo_base.filter(name=username):
        if UserInfo_base.filter(name=username, password=password):
           return redirect("/userinfo/")
        return render(request, "welcome.html",context={"error_msg": "用户名或密码错误"}, status=200) 
    else:
        # return HttpResponse("登陆失败")
        # 原html进行模板渲染
        return render(request, template_name="welcome.html", context={"error_msg": "登录失败,无该用户"}, status=200)
    