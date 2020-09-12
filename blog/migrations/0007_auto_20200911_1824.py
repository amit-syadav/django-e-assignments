# Generated by Django 2.1 on 2020-09-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190406_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='q_author',
            new_name='assigned_to',
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='quest',
            new_name='content',
        ),
        migrations.AddField(
            model_name='assignment',
            name='title',
            field=models.TextField(null=True),
        ),
    ]