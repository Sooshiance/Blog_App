from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import Post, Comment, Like, Complaicent


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'admin_approval', 'is_private']
    list_filter = ('is_private', 'admin_approval',
                   ('created_at', JDateFieldListFilter),
                   ('updated_at', JDateFieldListFilter),)
    search_fields = ['user', 'title']
    sortable_by = ['created_at', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'admin_approval']
    list_filter = ('admin_approval',
                   ('created_at', JDateFieldListFilter),)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'vote']


@admin.register(Complaicent)
class ComplacentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'admin_approval']
