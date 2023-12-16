from django.contrib import admin
from .models import Store, Address, OpeningHours, Food


admin.site.register(Store)
admin.site.register(Address)
admin.site.register(OpeningHours)
admin.site.register(Food)