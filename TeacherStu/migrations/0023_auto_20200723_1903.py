# Generated by Django 2.1.5 on 2020-07-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0022_auto_20200723_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
