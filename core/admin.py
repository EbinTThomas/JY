from django.contrib import admin
from .models import Zones, UserDetails, Ministries, Roles, UserMinistry

admin.site.register(Zones)
admin.site.register(UserDetails)
admin.site.register(Ministries)
admin.site.register(Roles)
admin.site.register(UserMinistry)