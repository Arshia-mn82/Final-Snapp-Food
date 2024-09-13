from django.contrib.admin import register,ModelAdmin
from .models import *

@register(Wallet)
class  UserAdmin(ModelAdmin):
    pass

@register(Profile)
class ProfileAdmin(ModelAdmin):
    pass
