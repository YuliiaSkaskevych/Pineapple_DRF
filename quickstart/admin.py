from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'heading', 'text', ]
    search_fields = ['heading', 'author']
    ordering = ['heading']
    date_hierarchy = "create"
    raw_id_fields = ['author', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author', 'text', 'post']
    search_fields = ['author', 'post']
    ordering = ['author']
    date_hierarchy = "publish"
    raw_id_fields = ['author', ]

TokenAdmin.raw_id_fields = ['user']
