# Generated by Django 3.1.1 on 2020-09-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='discreption',
            field=models.TextField(blank=True),
        ),
    ]