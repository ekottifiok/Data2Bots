from django.urls import path
from ishoppers.views import OrderView, PersonView, ProductView

app_name = 'ishoppers'

urlpatterns = [
    path('login/', PersonView.as_view()),
    path('logout/', PersonView.as_view()),
    path('history/', OrderView.as_view()),
    path('products/', ProductView.as_view())
]