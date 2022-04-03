from django.urls import path, include, re_path
from rest_framework import routers

from .views import EmployeeListView, EmployeeDetailView, EmployeeRoleList

urlpatterns = [
    path('', EmployeeListView.as_view()),
    path('<int:pk>/', EmployeeDetailView.as_view()),
    re_path('^employee-level/(?P<level>.+)/$', EmployeeRoleList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
