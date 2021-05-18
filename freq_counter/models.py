from django.db import models

# Create your models here.


class Url_mod(models.Model):

    url = models.URLField(max_length=100000)
    frequent_words = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.url

