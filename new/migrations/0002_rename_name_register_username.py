# Generated by Django 4.1.6 on 2023-02-10 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='username',
        ),
    ]
