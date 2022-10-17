
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet, 'products')
router.register('new-products', views.NewProductViewSet, 'new-products')
router.register('teddy-bear-hot', views.TeddyBearHotViewSet, 'teddy-bear-hot')
router.register('bouquet-hot', views.BouquetHotViewSet, 'bouquet-hot')
router.register('gift-box-hot', views.GiftBoxHotViewSet, 'gift-box-hot')
router.register('gau-bong', views.GauBongViewSet, 'gau-bong')
router.register('thu-bong', views.ThuBongViewSet, 'thu-bong')
router.register('goi-bong', views.GoiBongViewSet, 'goi-bong')
router.register('gau-bong-hoat-hinh',
                views.GauBongHoatHinhViewSet, 'gau-bong-hoat-hinh')
router.register('bup-be', views.BupBeViewSet, 'bup-be')
router.register('hoa', views.HoaViewSet, 'hoa')
router.register('phu-kien', views.PhuKienViewSet, 'phu-kien')
router.register('hop-qua', views.HopQuaViewSet, 'hop-qua')


urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
]
