from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'destinations', views.DestinationViewSet)
router.register(r'server', views.DataHandlerViewSet, basename='server')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
