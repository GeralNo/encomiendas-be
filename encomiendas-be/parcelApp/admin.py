from django.contrib import admin
from .models.envios import Envios
from .models.trabajadores import Trabajadores
from .models.transportadores import Transportadores

from .models.user import User
from .models.account import Account

# Register your models here.

admin.site.register(User)
admin.site.register(Envios)
admin.site.register(Trabajadores)
admin.site.register(Transportadores)
admin.site.register(Account)


