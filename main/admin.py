from django.contrib import admin
from .models import Article, Comment, Category


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
