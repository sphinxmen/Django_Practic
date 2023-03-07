from django.contrib import admin
from .models import Humans, Child, PersonRelationShip
# Register your models here.


class HumansAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'age', 'gender',)
    list_display_links = ('pk',)
    list_filter = ('name',)
    list_editable = ('name',)
    search_fields = ('name', 'age',)


admin.site.register(Humans, HumansAdmin)

class PersonRelationShipAdmin(admin.ModelAdmin):
    list_display = ('pk', 'parent', 'child')
    list_display_links = ('pk',)
    list_filter = ('parent',)
    search_fields = ('parent', 'child',)

admin.site.register(PersonRelationShip, PersonRelationShipAdmin)



class ChildAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'age', 'gender',)
    list_display_links = ('pk',)
    list_filter = ('name',)
    list_editable = ('name',)
    search_fields = ('name', 'age',)


admin.site.register(Child, ChildAdmin)