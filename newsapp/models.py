from django.db import models


# Create your models here. source author title description url urlToImage publishedAt content
class NewsArticle(models.Model):
    source = models.CharField(max_length=100,default="unknown")
    author = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    url = models.URLField(null=True)
    urlToImage = models.URLField(null=True)
    publishedAt = models.CharField(primary_key=True, max_length=100)
    content = models.TextField(null=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title