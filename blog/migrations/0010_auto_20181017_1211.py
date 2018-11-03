# Generated by Django 2.0.9 on 2018-10-17 12:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181017_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock())], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock())], icon='arrow-right', label='Right column content'))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('htmljs', wagtail.core.blocks.TextBlock()), ('code_bash', wagtail.core.blocks.TextBlock()), ('code_py', wagtail.core.blocks.TextBlock()), ('code_htmljs', wagtail.core.blocks.TextBlock())], blank=True, null=True),
        ),
    ]