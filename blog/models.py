from django import forms
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock

from wagtail.search.backends import get_search_backend
from home.models import Root

from blog.tools import get_tree
from blog.blocks import TwoColumnBlock, ThreeColumnBlock


local_functions = locals()

def SetContext(context):
    categories = BlogCategory.objects.all()
    context['categories'] = categories
    tagList = []
    tags = BlogTag.objects.all()
    #tags = BlogTag.objects.order_by("tag")
    for tag in tags:
        if tag.tag.name not in tagList:
            tagList.append(tag.tag.name)
    tagList.sort()
    context['tags'] = tagList

class BlogIndex(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().not_type(BlogTagIndex).not_type(BlogQueryCategory).live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        SetContext(context)
        return context

    #template = 'blog_index.html'

class BlogSearch(Page):
    def get_context(self, request):
        word = request.GET.get('key')
        context = super().get_context(request)
        s = get_search_backend()
        posts = s.search(word, BlogPage)
        SetContext(context)
        context['posts'] = posts
        return context

class BlogQueryCategory(Page):
    def get_context(self, request):
        categoryName = request.GET.get('category')

        # Filter posts by category name
        rez = BlogCategory.objects.filter(name=categoryName)
        if (len(rez) == 0):
            return
        else:
            # Update template context
            context = super().get_context(request)
            
            blogpages = BlogPage.objects.filter(categories=rez[0])
            context['blogpages'] = blogpages
            SetContext(context)
            return context

class BlogTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

from django.shortcuts import render


class BlogPage(Page):
    date = models.DateField("Post date")
    description = models.CharField(max_length=250, blank=True)
    tags = ClusterTaggableManager(through='blog.BlogTag', blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
        ('image', ImageChooserBlock()),
        ('htmljs', blocks.TextBlock()),
        ('code_bash', blocks.TextBlock()),
        ('code_py', blocks.TextBlock()),
        ('code_htmljs', blocks.TextBlock()),
    ],null=True,blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('description'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def get_context(self, request):
        #update context: adding catgories list for side widget
        context = super().get_context(request)
        SetContext(context)
        return context


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
                           #blank=True, null=True, on_delete=models.SET_NULL
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class BlogTagIndex(Page):

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        SetContext(context)
        return context

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BlogTree(Page):
    def get_context(self, request):

        context = super().get_context(request)
        index = BlogIndex.objects.filter(title='Posts')[0]
        posts = index.get_children().live().order_by('-first_published_at')
        context['posts'] = posts
        SetContext(context)

        html_menu = get_tree(BlogIndex)
        context['menu'] = html_menu

        return context

