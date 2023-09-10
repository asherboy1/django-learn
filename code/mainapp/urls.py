from django.contrib import admin
from django.urls import path, re_path
from mainapp.views import *

urlpatterns = [
    # path('test/<int:num>/', view='')
    # 部门管理
    path('depart/list/', view=depart_list),

    # 添加部门
    path('depart/add/page', view=depart_add_page),
    path('depart/add', view=depart_add),

    # 删除部门
    re_path("depart/delete/", view=depart_delete),

    # 编辑部门
    path("depart/modify/page/", view=depart_modify_page),
    path("depart/modify", view=depart_modify),
    # path("depart/modify/<int:nid>/edit", view=depart_modify_page),

    # 继承模板测试
    path("test/", view=render_succ),

    # 用户管理
    path('userinfo/', view=userinfoPage),
    # 添加用户
    path('userinfoAddPage/', view=userinfoAddPage),
    path("userinfo/add", view=userinfoAdd),
    path("userinfoFormAddPage/", view=user_model_form_add),
    # 删除用户
    path("userinfoDelPage/", view=userinfoDelPage),
    path("userinfo/del/", view=userinfoDel),
]