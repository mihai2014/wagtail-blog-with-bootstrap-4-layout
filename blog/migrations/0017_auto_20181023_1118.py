# Generated by Django 2.0.8 on 2018-10-23 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20181023_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='intro',
            new_name='description',
        ),
    ]
