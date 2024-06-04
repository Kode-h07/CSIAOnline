from django.contrib import admin
from .models import Monday,Tuesday,Wednesday,Thursday,DefaultMonday,DefaultTuesday,DefaultWednesday,DefaultThursday

# Register your models here.
admin.site.register(Monday)
admin.site.register(Tuesday)
admin.site.register(Wednesday)
admin.site.register(Thursday)
admin.site.register(DefaultMonday)
admin.site.register(DefaultTuesday)
admin.site.register(DefaultWednesday)
admin.site.register(DefaultThursday)