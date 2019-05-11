from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('eventos', views.EventView)
router.register('lugares', views.LocationView)
router.register('secciones', views.SectionView)

urlpatterns = [
    path('store/', include(router.urls))
]
