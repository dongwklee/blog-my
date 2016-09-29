from django.contrib import admin
from .models import Post, PostImage, Comment


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','author']
    list_display_links = ['title']
    inlines = [PostImageInline]



admin.site.register(Post,PostAdmin)




class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'text','author']
	list_display_links = ['text']

admin.site.register(Comment,CommentAdmin)
