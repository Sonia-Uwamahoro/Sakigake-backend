# Generated by Django 4.2.5 on 2023-09-11 06:49

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_added',
            new_name='date_added_at',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='date_updated',
            new_name='date_updated_at',
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region='KE', unique=True),
        ),
    ]
