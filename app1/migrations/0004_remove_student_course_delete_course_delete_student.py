# Generated by Django 4.0.2 on 2022-04-05 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='course',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
