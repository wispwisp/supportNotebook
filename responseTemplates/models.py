from django.db import models

from taggit.managers import TaggableManager


class ResponseTemplate(models.Model):
    tags = TaggableManager()

    def __str__(self):
        return str(self.tags.names())


class Paragraph(models.Model):
    template = models.ForeignKey(ResponseTemplate)
    text = models.TextField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.text[:80] + "..."
