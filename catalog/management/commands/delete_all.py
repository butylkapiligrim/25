from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'add bl'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        Product.objects.create(name="Самса", description="Вкусная куриная самса", price="49", created_at="2024-12-24", updated_at="2024-12-24")
