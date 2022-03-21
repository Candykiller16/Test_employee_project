from rest_framework import serializers
from employee.models import EmployeeMPTT


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMPTT
        fields = ['id', 'first_last_patro_name', 'role', 'date_of_employment', 'salary_amount', 'paid_salary_inf',
                  'level', 'parent']
