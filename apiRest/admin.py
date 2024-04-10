from django.contrib import admin

from .models import Empleado
from .models import Email
from .models import Telefono

admin.site.register(Empleado)
admin.site.register(Email)
admin.site.register(Telefono)



# Register your models here.
