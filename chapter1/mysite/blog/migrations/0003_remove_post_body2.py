# Generated by Django 3.0.14 on 2021-05-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_body2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body2',
        ),
    ]
