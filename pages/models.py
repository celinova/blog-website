from django.db import models

# Create your models here.


class Entry(models.Model):
    entry_title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    entry_text = models.TextField(default=None)
    publish_date = models.DateTimeField("Date Published")
    edit_date = models.DateTimeField("Date Edited", auto_now_add=True)

    def __str__(self):
        return self.entry_title

    # shortened content property for index page
    @property
    def short_content(self):
        return (
            (self.entry_text[:200] + "...")
            if len(self.entry_text) > 140
            else self.entry_text
        )
