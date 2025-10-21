from django.urls import path
from .views import WargaListView, WargaDetailListView, PengaduanListView, WargaCreateView, PengaduanCreateView, WargaUpdateView,  WargaDeleteView
urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), 
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'), 
]