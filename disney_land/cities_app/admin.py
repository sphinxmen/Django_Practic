from django.contrib import admin

from .models import City
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'city',)
    list_display_links = ('pk',)
    list_filter = ('name', )

admin.site.register(City, CityAdmin)