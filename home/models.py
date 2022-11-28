from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from lesson.models import LessonIndexPage

class HomePage(Page):
    
     
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


    def get_context(self, request):
        context = super().get_context(request)
        context['lesson_index_pages'] = self.get_children().type(LessonIndexPage)
        return context
