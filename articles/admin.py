from django.contrib import admin

# Register your models here.
from .models import Articles, Comment

class CommentInline(admin.TabularInline): # new
    model = Comment


class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

admin.site.register(Articles,ArticleAdmin)
admin.site.register(Comment)