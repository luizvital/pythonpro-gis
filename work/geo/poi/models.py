from django.contrib.gis.db import models


class POI(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    amenity = models.CharField(max_length=50)
    name = models.CharField(max_length=200, blank=True, null=True, default='')
    addr_street = models.CharField(max_length=300, null=True, default='')
    addr_city = models.CharField(max_length=100, null=True,  default='')
    addr_country = models.CharField(max_length=100, null=True,  default='')
    addr_housenumber = models.CharField(max_length=30, null=True, default='')
    wheelchair = models.CharField(max_length=10, null=True,  default='')
    addr_postcode = models.CharField(max_length=10, null=True,  default='')
    phone = models.CharField(max_length=50, null=True, default='')
    source = models.CharField(max_length=100, null=True, default='')
    brewery = models.CharField(max_length=100, null=True, default='')
    smoking = models.CharField(max_length=50, null=True, default='')
    food = models.CharField(max_length=50, null=True, default='')
    internet_access = models.CharField(max_length=50, null=True, default='')
    website = models.CharField(max_length=300, null=True, default='')
    outdoor_seating = models.CharField(max_length=50, null=True, default='')
    delivery = models.CharField(max_length=50, null=True, default='')
    description = models.CharField(max_length=300, null=True, default='')
    addr_state = models.CharField(max_length=100, null=True, default='')
    opening_hours_covid19 = models.CharField(max_length=50, null=True, default='')
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.name or '--'
