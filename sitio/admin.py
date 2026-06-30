from django.contrib import admin
from .models import serviciop, eventop, serviciopop, paquetes

class AdminModel(admin.ModelAdmin):
    readonly_fields=('id','created','updated')
    list_display=('id','nombre','categoria','generalidades')
    list_editable=['generalidades']
    date_hierarchy='created' 
    list_filter = ['categoria']


admin.site.register(serviciop, AdminModel)
admin.site.register(eventop)
admin.site.register(serviciopop)
admin.site.register(paquetes)