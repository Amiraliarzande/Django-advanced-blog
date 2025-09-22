from django.contrib import admin
from .models import Post, Category

# Register your models here.

class blogAdmin (admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'published_at')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Post, blogAdmin)
admin.site.register(Category)
