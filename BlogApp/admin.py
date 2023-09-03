from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import Post, Comment, Like


@admin.register(Post)
class PAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'admin_approval', 'is_private']
    list_filter = ('is_private', 'admin_approval',
                   ('created_at', JDateFieldListFilter),
                   ('updated_at', JDateFieldListFilter),)
    search_fields = ['user', 'title']


@admin.register(Comment)
class CAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'admin_approval']
    list_filter = ('admin_approval',
                   ('created_at', JDateFieldListFilter),)


@admin.register(Like)
class LAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'vote']
