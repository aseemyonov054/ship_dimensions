from django.db import models

# ship types 
class ShipTypes(models.Model):
    name = models.CharField(max_length=100)
    eng_name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name
    
    @classmethod
    def get_default_pk(cls):
        exam, created = cls.objects.get_or_create(
            name='default', 
        )
        return exam.pk

# ship data
class ShipData(models.Model):
    ship_type = models.ForeignKey(ShipTypes, on_delete=models.CASCADE, default=ShipTypes.get_default_pk)
    imo = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    deadweight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    depth = models.FloatField()
    def __str__(self):
        return self.ship_type.name + " - " + self.imo

# PIANC ships parameters
class PiancShips(models.Model):
    ship_type = models.ForeignKey(ShipTypes, on_delete=models.CASCADE, default=ShipTypes.get_default_pk)
    ship_class_name = models.CharField(max_length=150)
    deadweight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField(default=0)
    depth = models.FloatField()
    container_capacity = models.FloatField(null=True, blank=True)

# corelation coefficients
class DimensionsCorrelation(models.Model):
    ship_type = models.ForeignKey(ShipTypes, on_delete=models.CASCADE, default=ShipTypes.get_default_pk)
    parameter = models.CharField(max_length=20)
    a_value = models.FloatField()