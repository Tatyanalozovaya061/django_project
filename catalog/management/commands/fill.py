from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'одежда для женщин', 'category_description': 'платья, костюмы'},
            {'category_name': 'одежда для мужчин', 'category_description': 'брюки, футболки'},
            {'category_name': 'одежда для детей', 'category_description': 'ползунки, чепчики, боди'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)
