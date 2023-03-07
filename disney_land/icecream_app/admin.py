from django.contrib import admin

from .models import Ice_cream, Ice_cream_shop

# Register your models here.


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'sort_of', 'price',)
    list_display_links = ('pk',)
    list_filter = ('name',)
    list_editable = ('sort_of',)
    search_fields = ('name', 'sort_of',)


admin.site.register(Ice_cream, IceCreamAdmin)


class IceCreamShopAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_of_create', 'address', 'ower', 'geo', 'city',)
    list_display_links = ('pk',)
    list_filter = ('name',)
    list_editable = ('name',)
    search_fields = ('name', 'address',)


admin.site.register(Ice_cream_shop, IceCreamShopAdmin)