# Generated by Django 2.1.5 on 2020-07-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStu', '0014_mcq_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255)),
                ('clas', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
