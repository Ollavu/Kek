# Generated by Django 4.0.6 on 2022-08-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top', '0005_alter_datatoexport_closedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatoexport',
            name='object_name',
            field=models.CharField(max_length=150, verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='datatoexport',
            name='worker_fullname',
            field=models.CharField(max_length=150, verbose_name='ФИО'),
        ),
    ]
