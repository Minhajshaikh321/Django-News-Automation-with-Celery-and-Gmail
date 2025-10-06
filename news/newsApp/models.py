from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    url=models.URLField(unique=True)
    published_date=models.DateTimeField()
    source=models.CharField(max_length=200)

    def __str__(self):
        return self.title