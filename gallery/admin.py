from django.contrib import admin

from .models import Style, Painting

class StyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Style,StyleAdmin)

class PaintingAdmin(admin.ModelAdmin):
    list_display = ['title', 'available', 'style', 'quantity', 'price', 'description', 'created', 'updated']
    list_editable = ['price', 'style', 'quantity', 'available', 'description']
    prepopulated_fields = {'slug':('title',)}
    list_per_page = 25
admin.site.register(Painting,PaintingAdmin)