# Generated by Django 2.0.9 on 2018-10-17 11:59

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogIndex'),
        ),
    ]