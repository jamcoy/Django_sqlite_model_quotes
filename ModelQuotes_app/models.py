from __future__ import unicode_literals
from django.db import models


class Quote(models.Model):

    class Meta:  # include this to ensure build in IDE
        app_label = "ModelQuotes_app"

    name = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)

    def __str__(self):
        return ' '.join([
            self.name + ": " + self.quote
        ])
