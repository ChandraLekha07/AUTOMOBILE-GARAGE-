from django.contrib import admin

from .models import Make, Model, Variant, Car

# Register your models here.
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Variant)
admin.site.register(Car)