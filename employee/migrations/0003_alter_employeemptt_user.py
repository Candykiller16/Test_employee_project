# Generated by Django 4.0.3 on 2022-03-23 21:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0002_employeemptt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemptt',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(1), to=settings.AUTH_USER_MODEL),
        ),
    ]