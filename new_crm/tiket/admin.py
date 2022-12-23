from django.contrib import admin
from .models import Tikets


# Register your models here.


class TiketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'date_create',)
    list_display_links = ('pk',)
    list_filter = ('number',)
    list_editable = ('number',)
    search_fields = ('number', 'date_create',)


admin.site.register(Tikets, TiketAdmin)
