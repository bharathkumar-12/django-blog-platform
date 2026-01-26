from django.contrib import admin

from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_at')
	search_fields = ('title', 'body')
	list_filter = ('created_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	search_fields = ('name',)
