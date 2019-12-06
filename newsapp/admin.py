from django.contrib import admin

# Register your models here.
from newsapp.models import NewsArticle

admin.site.register(NewsArticle)