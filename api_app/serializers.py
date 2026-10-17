from rest_framework import serializers
from api_app.models import ProductModel



class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
