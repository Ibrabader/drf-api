from django.urls import path 
from .views import ElectronicsList, ElectronicsDetail

urlpatterns = [
    path('', ElectronicsList.as_view(), name = 'Electronics_list'),
    path('<int:pk>/',ElectronicsDetail.as_view(), name = 'Electronics_Detail')

]




