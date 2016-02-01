from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 1
    
admin.site.register(models.Article, ArticleAdmin)

