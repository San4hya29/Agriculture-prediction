# Generated by Django 4.1.6 on 2023-03-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_rename_name_register_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=522)),
            ],
        ),
    ]
