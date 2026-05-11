from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('Item_ID', 'Item_Name', 'Type', 'Unit', 'Price')
    search_fields = ('Item_Name', 'Type')
