from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Places)

admin.site.register(ContactTable)
admin.site.register(TestModel)

class Display(admin.ModelAdmin):
    list_display = (
        'country',
        'img3dname' ,
        'lang_name',
    )
admin.site.register(PlacesDetail, Display)