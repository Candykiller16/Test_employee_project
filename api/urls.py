from django.urls import path, include, re_path
from rest_framework import routers

from .views import EmployeeListView, EmployeeDetailView, EmployeeRoleList

urlpatterns = [
    path('', EmployeeListView.as_view()),
    path('<int:pk>/', EmployeeDetailView.as_view()),
    re_path('^employee-level/(?P<level>.+)/$', EmployeeRoleList.as_view()),
]