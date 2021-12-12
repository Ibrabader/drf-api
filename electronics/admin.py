from django.contrib import admin
from .models import Electronics 

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display =[
        'product_name','published','relase_date','update_date','brand',
    ]
