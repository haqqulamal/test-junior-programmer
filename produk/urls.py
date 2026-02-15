from django.urls import path
from . import views

app_name = 'produk'

urlpatterns = [
    path('', views.ProdukListView.as_view(), name='list'),
    path('tambah/', views.ProdukCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.ProdukUpdateView.as_view(), name='edit'),
    path('hapus/<int:pk>/', views.ProdukDeleteView.as_view(), name='delete'),
]
