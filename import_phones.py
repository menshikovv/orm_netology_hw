import csv
from django.core.management.base import BaseCommand
from your_app.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Phone.objects.create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
        self.stdout.write(self.style.SUCCESS('Phones imported successfully'))
