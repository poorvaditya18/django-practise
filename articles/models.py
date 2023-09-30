from django.db import models

from dataclasses import dataclass
# Create your models here.

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()


"""
Writing data -->
    obj = Article(title='Hello World', content='This is awesome')
    obj.save()
    print(obj.id)
                    OR 
    obj2 = Article.objects.create(title='Hello World Again', content='This is awesome')
    print(obj2.id)

Reading data -->
    obj = Article.objects.get(id=1)
"""