from django.contrib import admin

# Register your models here.
#from .models import Users
from django.contrib.auth.models import User


from .models import user



admin.site.register(user)
