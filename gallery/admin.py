from django.contrib import admin

from .models import Style, Painting

class StyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Style,StyleAdmin)

class PaintingAdmin(admin.ModelAdmin):
    list_display = ['title', 'available', 'quantity', 'price', 'description', 'created', 'updated']
    list_editable = ['price', 'quantity', 'available', 'description']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 25
admin.site.register(Painting,PaintingAdmin)