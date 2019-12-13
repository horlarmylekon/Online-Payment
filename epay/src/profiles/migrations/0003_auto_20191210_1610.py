# Generated by Django 2.0.9 on 2019-12-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20191209_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dep_option',
            field=models.CharField(choices=[('Default', '---------'), ('ENG', 'Engineering'), ('MTH', 'Mathematics'), ('ECN', 'Economics')], max_length=225, verbose_name='Option'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='matric_number',
            field=models.CharField(max_length=225, verbose_name='Matric Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='Contact'),
        ),
    ]
