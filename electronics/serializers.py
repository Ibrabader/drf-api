from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Electronics

class ElectronicsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['product_name','description','relase_date','update_date','brand']
        model = Electronics
