# Generated by Django 2.0.9 on 2018-10-16 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0040_page_draft_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('blog', '0003_auto_20181016_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('intro', models.CharField(max_length=250)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='blogtagen',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogtagen',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogtagro',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogtagro',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='indexro',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='pageen',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='pageen',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='pageen',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='pagero',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='pagero',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='pagero',
            name='tags',
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='blog.BlogPage'),
        ),
        migrations.RenameModel(
            old_name='IndexEn',
            new_name='BlogIndex',
        ),
        migrations.DeleteModel(
            name='BlogTagEn',
        ),
        migrations.DeleteModel(
            name='BlogTagRo',
        ),
        migrations.DeleteModel(
            name='IndexRo',
        ),
        migrations.DeleteModel(
            name='PageEn',
        ),
        migrations.DeleteModel(
            name='PageRo',
        ),
        migrations.AddField(
            model_name='blogtag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='blog.BlogIndex'),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_blogtag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]