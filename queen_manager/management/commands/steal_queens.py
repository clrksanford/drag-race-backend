from django.core.management.base import BaseCommand
from ...models import Queen
import requests
import json

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        response = requests.get('http://www.nokeynoshade.party/api/queens?limit=50&offset=70')

        response = response.json()
        print(response)

        for queen in response:
            name = queen['name']
            image_url = queen['image_url']
            quote = queen['quote']
            winner = queen['winner']
            miss_congeniality = queen['missCongeniality']

            new_queen = Queen.objects.create(
                name=name,
                image_url=image_url,
                quote=quote,
                winner=winner,
                miss_congeniality=miss_congeniality,
            )
