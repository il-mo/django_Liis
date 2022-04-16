from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'name', 'visible', 'text')
    list_display = (
        'pk',
        'name',
        'text',
        'author',
    )
    search_fields = ('name',)
