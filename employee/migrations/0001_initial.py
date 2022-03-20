# Generated by Django 4.0.3 on 2022-03-20 19:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMPTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_patro_name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('STD', 'base employee'), ('MGR', 'manager'), ('SRMGR', 'senior manager'), ('BS', 'boss'), ('PRES', 'president')], max_length=25)),
                ('date_of_employment', models.DateField(default=datetime.date.today)),
                ('salary_amount', models.PositiveIntegerField()),
                ('paid_salary_inf', models.PositiveIntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='employee.employeemptt')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]