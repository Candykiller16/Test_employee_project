from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from employee.models import EmployeeMPTT
from rest_framework import generics
from rest_framework import permissions


class EmployeeListView(generics.ListAPIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = EmployeeMPTT.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = EmployeeMPTT.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]


class EmployeeRoleList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        level = self.kwargs['level']
        return EmployeeMPTT.objects.filter(level=level)
