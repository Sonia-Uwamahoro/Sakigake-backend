# Generated by Django 4.2.5 on 2023-09-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_read',
        ),
        migrations.AlterField(
            model_name='notification',
            name='preview',
            field=models.CharField(max_length=50),
        ),
    ]
