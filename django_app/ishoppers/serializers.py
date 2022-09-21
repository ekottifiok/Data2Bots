from rest_framework.serializers import ModelSerializer
from ishoppers.models import OrderHistory, Person, Product

class PersonSerializer(ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'
        
class ProductSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderSerializer(ModelSerializer):
    
    class Meta:
        model = OrderHistory
        fields = '__all__'