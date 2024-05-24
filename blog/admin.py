from django.contrib import admin
from .models import About, Author, Comment, SocialMedia, Post, Tag


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    filter_horizontal = ('tags',)
    list_filter = ('author',)
    search_fields = ('id', 'title')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    filter_horizontal = ('social_media',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment)
admin.site.register(SocialMedia)
admin.site.register(Tag)
admin.site.register(About)
