from datetime import date

from django.contrib.auth.models import User
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class EmployeeMPTT(MPTTModel):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SRMGR'
    BOSS = 'BS'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (BOSS, 'boss'),
        (PRESIDENT, 'president'))

    first_last_patro_name = models.CharField(max_length=100)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    date_of_employment = models.DateField(default=date.today)
    salary_amount = models.PositiveIntegerField()
    paid_salary_inf = models.PositiveIntegerField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='employee', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET(1))

    def __str__(self):
        return self.first_last_patro_name

    def __repr__(self):
        return self.__str__()