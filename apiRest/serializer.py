from rest_framework import serializers
from .models import Empleado, Telefono, Email


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'
        read_only_fields = ['empleado']  

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
        read_only_fields = ['empleado']  

class EmpleadoSerializer(serializers.ModelSerializer):
    telefonos = TelefonoSerializer(many=True)
    emails = EmailSerializer(many=True)

    class Meta:
        model = Empleado
        fields = '__all__'

    def create(self, validated_data):
        telefonos_data = validated_data.pop('telefonos')
        emails_data = validated_data.pop('emails')
        empleado = Empleado.objects.create(**validated_data)

        for telefono_data in telefonos_data:
            Telefono.objects.create(empleado=empleado, **telefono_data)

        for email_data in emails_data:
            Email.objects.create(empleado=empleado, **email_data)

        return empleado