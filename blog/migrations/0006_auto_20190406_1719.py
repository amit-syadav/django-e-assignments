# Generated by Django 2.1.7 on 2019-04-06 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_assignment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='user',
            new_name='q_author',
        ),
    ]
