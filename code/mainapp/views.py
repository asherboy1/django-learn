from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from first_app.models import Department, UserInfo
from django import forms
from datetime import date
from django.forms.models import model_to_dict

# Create your views here.

def userinfoPage(request):
    # 数据库数据
     # 获取所有用户信息
    user_query = UserInfo.objects.all()

    dict_list = [{"queryset": dict1} for dict1 in user_query]
    func_add_list_no = lambda x,i:x.update({"list_no": i})
    for _i,_info in enumerate(dict_list):
        func_add_list_no(_info, i=_i+1)
    print(dict_list)

    return render(request, 'user_info.html', context={"dict_list": dict_list})

# 添加用户模块
def userinfoAddPage(request):
    depart_info = Department.objects.all()

    return render(request, "userAddPage_copy.html", context={"depart_info": depart_info})

def userinfoAdd(request):
    _name = request.POST.get("name", None)
    _password = request.POST.get("password", None)

    # 插入数据至数据库
    UserInfo.objects.create(name=_name, password=_password)
    return redirect("/userinfo/")

# 删除用户模块
def userinfoDelPage(request):
    return render(request, "userDelPage.html")

def userinfoDel(request):
    # 对name进行判断操作
    # _name = request.GET.get("username")
    # data = UserInfo.objects.filter(name=_name)
    # if data:
    #     UserInfo.objects.filter(name=_name).delete()
    #     return HttpResponse("删除成功")
    # return HttpResponse("未找到指定用户")
    #---------------------------------
    _id = request.GET.get("id")
    UserInfo.objects.filter(id=_id).delete()
    return redirect("/userinfo/")


#---------------------------------
def depart_list(request):
    """部门管理主页"""
    
    # 获取所有部门列表信息
    department_query = Department.objects.all()
    # print(departmeny_query)
    # print({"department_query": department_query})

    dict_list = [model_to_dict(dict1) for dict1 in department_query]
    func_add_list_no = lambda x,i:x.update({"list_no": i})
    for _i,_info in enumerate(dict_list):
        func_add_list_no(_info, i=_i+1)
    return render(request, 'depart_list_copy.html', context={"department_query": dict_list})


def depart_add_page(request):
    """添加部门页面"""
    return render(request, "depart_add.html")

def depart_add(request):
    """添加部门"""
    
    # 遍历所有部门信息
    department_query = Department.objects.all()

    # 将所有models对象转为dict
    dict_list = [model_to_dict(dict1) for dict1 in department_query]
    
    # 提取name
    func_extract_name = lambda x:x.get("depart_name")
    depart_names = [func_extract_name(x) for x in dict_list]
    # return render(request, "depart_add.html")

    # 添加部门逻辑
    depart_temp = request.POST.get("depart_temp_name")
    if depart_temp:
        if depart_temp.strip() not in depart_names:
            department_query.create(depart_name=depart_temp)
            return redirect("/depart/list")
        else:
            return render(request, "depart_add_copy.html", context={"error_msg": "添加失败，已有该部门"})
    else:
        return render(request, "depart_add_copy.html")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get("id")

    depart_info = Department.objects.filter(id=nid).delete()

    # Department.
    return redirect("/depart/list")


def depart_modify_page(request):
    """编辑部门页面"""
    # print(nid)
    _id = request.GET.get("id")
    depart_info = Department.objects.filter(id=_id)
    return render(request, "depart_modify_copy.html", context={"depart_info": depart_info})

def depart_modify(request):
    """编辑部门"""
    # 遍历所有部门信息
    department_query = Department.objects.all()
    # 将所有models对象转为dict
    dict_list = [model_to_dict(dict1) for dict1 in department_query]
    
    # 提取name
    func_extract_name = lambda x:x.get("depart_name")
    depart_names = [func_extract_name(x) for x in dict_list]
    # return render(request, "depart_add.html")
    
    # 编辑部门逻辑
    depart_temp = request.POST.get("depart_temp_name")
    depart_id = request.POST.get("depart_name_id")
    if depart_temp:
        if depart_temp.strip() not in depart_names:
            department_query.filter(id=depart_id).update(depart_name=depart_temp)
            return redirect("/depart/list")
        else:
            # 报错时需重新传递 info参数将编辑部门信息展示
            depart_info = Department.objects.filter(id=depart_id)

            return render(request, "depart_modify_copy.html", context={"error_msg": "添加失败，已有该部门", "depart_info": depart_info})
    else:
        return render(request, "depart_modify_copy.html")


def render_succ(request):
    return render(request, "test1.html")

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "account", "department", "gender"]
        # fields = '__all__' # 字段直接全部添加
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "姓名", "autocomplete":"off",
            "required":"required"}),  # 此处可设计输入格式与样式
            "password": forms.TextInput(attrs={"class": "form-control", "placeholder": "密码","autocomplete":"off",
            "required":"required"}),
            "age": forms.TextInput(attrs={"class": "form-control", "placeholder": "年龄","autocomplete":"off",
            "required":"required"}),
            "account": forms.TextInput(attrs={"class": "form-control", "placeholder": "总资产余额","autocomplete":"off",
            "required":"required"}),
            "department": forms.Select(attrs={"class": "form-control", "placeholder": "部门","autocomplete":"off",
            "required":"required"}),
            "gender": forms.Select(attrs={"class": "form-control", "placeholder": "部门","autocomplete":"off",
            "required":"required"}),
        
        }

def user_model_form_add(request):
    form = UserModelForm()
    
    return render(request, "user_model_form_add.html", {"form": form})

