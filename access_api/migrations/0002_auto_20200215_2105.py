# Generated by Django 3.0.2 on 2020-02-15 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('access_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'posts'},
        ),
    ]
