# Generated by Django 4.1.3 on 2023-06-29 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_person_user_auth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auth',
        ),
    ]
