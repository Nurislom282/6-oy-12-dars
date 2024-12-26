from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category,Dish, Comment

admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','category','get_image')
    list_display_links = ('name', 'pk')
    list_editable = ('category',)
    list_filter = ('category',)
    search_fields = ('pk', 'name', 'description')
    list_per_page = 10

    def get_image(self, Dish):
        if Dish.photo:
            return mark_safe(f'<img src="{Dish.photo.url}" width="150px">')
        else:
            return '-'

    get_image.short_description = "Rasmi"


admin.site.register(Dish, PostAdmin)
admin.site.register(Comment)
