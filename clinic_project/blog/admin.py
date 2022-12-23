from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'content',)
    list_display_links = ('pk',)
    list_filter = ('title',)
    list_editable = ('title',)
    search_fields = ('title', 'content',)

admin.site.register(Article, ArticleAdmin)
