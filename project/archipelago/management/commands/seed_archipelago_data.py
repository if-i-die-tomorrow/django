import random
from django.core.management.base import BaseCommand
from archipelago.models import WorldBorder
from django.contrib.gis.geos import Polygon, MultiPolygon

class Command(BaseCommand):
    help = 'Seed the WorldBorder model with initial data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=5, help='Number of objects to create')
        parser.add_argument('--delete', action='store_true', help='Delete existing objects before seeding')

    def generate_random_polygon(self, state):
        # Generate a random polygon within a specific range of coordinates representing a state or region
        if state == 'US':
            min_lon, max_lon = -125, -66  # Longitude range for the United States
            min_lat, max_lat = 25, 49  # Latitude range for the United States
        elif state == 'UK':
            min_lon, max_lon = -10, 2  # Longitude range for the United Kingdom
            min_lat, max_lat = 49, 59  # Latitude range for the United Kingdom
        elif state == 'FR':
            min_lon, max_lon = -5, 8  # Longitude range for France
            min_lat, max_lat = 41, 51  # Latitude range for France
        else:
            min_lon, max_lon = -180, 180  # Default longitude range
            min_lat, max_lat = -90, 90  # Default latitude range

        num_points = random.randint(4, 6)  # Number of points in the polygon
        coordinates = [(random.uniform(min_lon, max_lon), random.uniform(min_lat, max_lat)) for _ in range(num_points)]
        coordinates.append(coordinates[0])  # Close the polygon
        polygon = Polygon(coordinates)
        return polygon

    def handle(self, *args, **options):
        count = options['count']
        delete_existing = options['delete']

        if delete_existing:
            WorldBorder.objects.all().delete()
            self.stdout.write(self.style.WARNING('Existing WorldBorder objects deleted.'))

        if count <= 0:
            self.stdout.write(self.style.ERROR('Invalid count value. Count must be greater than zero.'))
            return

        existing_count = WorldBorder.objects.count()

        if existing_count >= count:
            self.stdout.write(self.style.WARNING('The number of existing objects is equal to or greater than the requested count.'))
            return

        random.seed(42)  # Set a seed for reproducible results
        available_names = ['Border A', 'Border B', 'Border C', 'Border D', 'Border E']
        available_regions = [1, 2, 3, 4, 5]
        available_subregions = [1, 2, 3, 4, 5]

        if existing_count > 0:
            last_name = WorldBorder.objects.order_by('-id').values_list('name', flat=True).first()
            last_region = WorldBorder.objects.order_by('-id').values_list('region', flat=True).first()
            last_subregion = WorldBorder.objects.order_by('-id').values_list('subregion', flat=True).first()

            name_index = available_names.index(last_name) + 1
            region_index = available_regions.index(last_region) + 1
            subregion_index = available_subregions.index(last_subregion) + 1

            if name_index >= len(available_names):
                name_index = 0
            if region_index >= len(available_regions):
                region_index = 0
            if subregion_index >= len(available_subregions):
                subregion_index = 0

            available_names = available_names[name_index:] + available_names[:name_index]
            available_regions = available_regions[region_index:] + available_regions[:region_index]
            available_subregions = available_subregions[subregion_index:] + available_subregions[:subregion_index]

        world_borders = []
        for _ in range(count - existing_count):
            if not available_names:
                available_names = ['Border A', 'Border B', 'Border C', 'Border D', 'Border E']
            if not available_regions:
                available_regions = [1, 2, 3, 4, 5]
            if not available_subregions:
                available_subregions = [1, 2, 3, 4, 5]

            name = random.choice(available_names)
            available_names.remove(name)
            area = random.randint(100, 1000)
            pop2005 = random.randint(1000, 10000)
            state = random.choice(['US', 'UK', 'FR', 'DE', 'IT'])
            fips = state
            iso2 = state
            iso3 = state
            un = random.randint(1, 10)
            region = random.choice(available_regions)
            available_regions.remove(region)
            subregion = random.choice(available_subregions)
            available_subregions.remove(subregion)
            lon = random.uniform(-180, 180)
            lat = random.uniform(-90, 90)

            mpoly = MultiPolygon(self.generate_random_polygon(state))

            world_borders.append(
                WorldBorder(
                    name=name,
                    area=area,
                    pop2005=pop2005,
                    fips=fips,
                    iso2=iso2,
                    iso3=iso3,
                    un=un,
                    region=region,
                    subregion=subregion,
                    lon=lon,
                    lat=lat,
                    mpoly=mpoly,
                )
            )

        WorldBorder.objects.bulk_create(world_borders)
        self.stdout.write(self.style.SUCCESS(f'{count} WorldBorder objects seeded successfully.'))
