from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand, CommandError
from poi.models import POI

MAPPING = {
    'id': 'id',
    'amenity': 'amenity',
    'name': 'name',
    'addr_street': 'addr:street',
    'addr_city': 'addr:city',
    'addr_country': 'addr:country',
    'addr_housenumber': 'addr:housenumber',
    'addr_postcode': 'addr:postcode',
    'addr_state': 'addr:state',
    'wheelchair': 'wheelchair',
    'phone': 'phone',
    'source': 'source',
    'brewery': 'brewery',
    'smoking': 'smoking',
    'food': 'food',
    'internet_access': 'internet_access',
    'website': 'website',
    'outdoor_seating': 'outdoor_seating',
    'delivery': 'delivery',
    'description': 'description',
    'opening_hours_covid19': 'opening_hours:covid19',
    'geom': 'POINT'
}

class Command(BaseCommand):
    help = 'Import Bar data from OSM GeoJSON'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file')

    def handle(self, *args, **options):

        lm = LayerMapping(POI, options['geojson_file'], MAPPING)
        lm.save(verbose=True)

