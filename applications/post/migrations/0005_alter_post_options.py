# Generated by Django 4.2.5 on 2023-09-13 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-id',)},
        ),
    ]