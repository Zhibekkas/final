from django.contrib import admin
from webapp.models import Category, Advertisement


class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image', 'author', 'is_moderated',
                    'category', 'price', 'created_at', 'modified_at', 'published_at']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['title', 'description', 'image', 'author', 'is_moderated',
              'category', 'price', 'created_at', 'modified_at', 'published_at']
    readonly_fields = ['created_at', 'modified_at', 'published_at']


admin.site.register(Advertisement, AdAdmin)
admin.site.register(Category)
