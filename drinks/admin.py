from django.contrib import admin
from .models import Drinks
from .models import Users
from .models import Restaurants

admin.site.register(Drinks)
admin.site.register(Users)
admin.site.register(Restaurants)