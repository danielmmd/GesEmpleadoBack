from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, TelefonoViewSet, EmailViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet, basename='empleado')
router.register(r'telefonos', TelefonoViewSet ,basename='telefono')
router.register(r'emails', EmailViewSet, basename='email')

urlpatterns = [
    path('', include(router.urls)),
]