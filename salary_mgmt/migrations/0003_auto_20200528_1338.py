# Generated by Django 2.2.12 on 2020-05-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary_mgmt', '0002_auto_20200527_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalary',
            name='login',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
