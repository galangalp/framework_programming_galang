from django.urls import path, include
from .views import WargaListAPIView, WargaDetailAPIView, PengaduanListAPIView, PengaduanDetailAPIView

from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'Pengaduan', PengaduanViewSet, basename='Pengaduan')

urlpatterns = [
    # path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    # path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    # path('pengaduan/', PengaduanListAPIView.as_view(), name='api-pengaduan-list'),
    # path('pengaduan/<int:pk>/', PengaduanDetailAPIView.as_view(), name='api-pengaduan-detail'),
    path('', include(router.urls)),

]