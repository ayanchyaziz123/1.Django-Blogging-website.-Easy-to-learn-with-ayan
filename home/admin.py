from django.contrib import admin
from .models import Category, Post, Sliders


from .models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('postId', 'postTitle', 'postTimeDate')
    list_filter = ('postId', 'postTitle')
    search_fields = ('postId', 'postTitle', 'postTimeDate')







admin.site.register(Category)
admin.site.register(Sliders)





