# Generated by Django 4.2.5 on 2023-09-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_alter_subject_subject_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
