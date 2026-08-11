from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Display information for Item model on Admin page."""
    list_display = ('name', 'description', 'price')
    ordering = ('price',)
