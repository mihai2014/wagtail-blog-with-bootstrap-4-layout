# Generated by Django 2.0.9 on 2018-10-16 15:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='Root',
        ),
    ]
