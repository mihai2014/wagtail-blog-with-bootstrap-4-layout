# Generated by Django 2.0.9 on 2018-10-17 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogquerycategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
