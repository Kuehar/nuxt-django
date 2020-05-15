from django.urls import path

from .views import ItemListView,ItemDetailView,ItemCreateView

urlpatterns = [
    path('items/',ItemListView.as_view()),
    path('items/<int:pk>/',ItemDetailView.as_view()),
    path('items/add',ItemCreateView.as_view()),
]
