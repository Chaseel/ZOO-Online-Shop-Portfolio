# Generated by Django 4.2.1 on 2023-07-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
    ]