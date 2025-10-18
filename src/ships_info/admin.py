from django.contrib import admin
from .models import ShipTypes, ShipData, DimensionsCorrelation, PiancShips

# Register your models here.
admin.site.register(ShipTypes)
admin.site.register(ShipData)
admin.site.register(DimensionsCorrelation)
admin.site.register(PiancShips)