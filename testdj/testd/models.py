from __future__ import unicode_literals

from django.db import models


class MySite(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    author = models.CharField(max_length=100)
    num = models.IntegerField(max_length = 100)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['num']
# Create your models here.
