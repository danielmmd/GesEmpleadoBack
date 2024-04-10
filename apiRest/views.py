from rest_framework import viewsets
from .serializer import EmpleadoSerializer, EmailSerializer, TelefonoSerializer
from .models import Empleado, Telefono, Email
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Create the views


class EmpleadoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class TelefonoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer 


class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    
