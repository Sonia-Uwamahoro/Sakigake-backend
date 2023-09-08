from django.db import models

class Material(models.Model):
    keywords = models.ManyToManyField('Keyword')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
