from ishoppers.serializers import PersonSerializer, ProductSerializer, OrderSerializer
from rest_framework.generics import ListAPIView
from ishoppers.models import OrderHistory, Person, Product

# Create your views here.


class ProductView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class OrderView(ListAPIView):
    queryset = OrderHistory.objects.all()
    serializer_class = OrderSerializer


class PersonView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
