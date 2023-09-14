# Generated by Django 4.2.5 on 2023-09-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_phone_number_alter_customuser_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='school_name',
            field=models.CharField(default=1, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
