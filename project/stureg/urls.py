from django.urls import re_path
from stureg import views

urlpatterns = [
    re_path(r'^api/stureg$',views.stu_list),
    re_path(r'^api/stureg/(?P<pk>[0-9]+)$',views.stu_details),
    re_path(r'^api/stureg/sbg$',views.stu_bloodgroup)
]