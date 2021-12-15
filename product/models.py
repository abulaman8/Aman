from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.name
    


    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = 'https://dummyimage.com/450x300/dee2e6/6c757d.jpg'
        return url

    