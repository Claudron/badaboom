from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet


class LessonIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        lessonpages = self.get_children().live().order_by('-first_published_at')
        context['lessonpages'] = lessonpages
        return context

class LessonPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'LessonPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )        
    

class LessonPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=LessonPageTag, blank=True)
    author = models.CharField(blank=True, null=True, max_length=250)
    categories = ParentalManyToManyField('lesson.LessonCategory', blank=True)
    videos = ParentalManyToManyField('lesson.Video', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('author'),
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Lesson information"),
        FieldPanel('intro'),
        FieldPanel('videos', widget=forms.Select),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]    


class LessonPageGalleryImage(Orderable):
    page = ParentalKey(LessonPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

class LessonTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        lessonpages = LessonPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['lessonpages'] = lessonpages
        return context


@register_snippet
class LessonCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'lesson categories'


@register_snippet
class Video(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    description = RichTextField(blank=True)

    panels =  [
        FieldPanel('title'),
        FieldPanel('url'),
        FieldPanel('description'),    
    ]    

    def __str__(self):
        return self.title



