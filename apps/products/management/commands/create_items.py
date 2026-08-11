from django.core.management.base import BaseCommand

from products.models import Item

import pathlib
import os
import json
import typing as t


class Command(BaseCommand):
    """Fills database with some items to test."""
    def handle(self, *args: t.Any, **kwargs: t.Any) -> None:
        root_path = pathlib.Path(__file__).resolve().parent
        data_path = os.path.join(root_path, 'items.json')
        with open(data_path, 'r') as file:
            txt_data = file.read()
            json_data = json.loads(txt_data)
            Item.objects.bulk_create(Item(**fields) for fields in json_data)
