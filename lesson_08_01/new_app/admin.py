from django.contrib import admin
from .models import Author, Post, Category
# Register your models here.\


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bio')
    ordering = ['-email']
    search_fields = ['email']


class PostAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'title', 'status')
    list_filter = ['status', 'author_id']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)



