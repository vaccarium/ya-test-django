import json
from trainsapp.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        f = open('trainsapp/fixtures/data.json')
        data = json.load(f)

        for datum in data:
            fields = datum['fields']

            if 'station' in fields:
                fields['station_id'] = fields['station']
                del fields['station']
            if 'train' in fields:
                fields['train_id'] = fields['train']
                del fields['train']

            if datum['model'] == 'trainsapp.station':
                model = Station(**fields)
            elif datum['model'] == 'trainsapp.arrival':
                model = Arrival(**fields)
            elif datum['model'] == 'trainsapp.departure':
                model = Departure(**fields)
            elif datum['model'] == 'trainsapp.intermediatestop':
                model = IntermediateStop(**fields)
            elif datum['model'] == 'trainsapp.train':
                if 'arrival' in fields:
                    fields['arrival_id'] = fields['arrival']
                    del fields['arrival']
                if 'departure' in fields:
                    fields['departure_id'] = fields['departure']
                    del fields['departure']
                model = Train(**fields)

            model.pk = datum['pk']
            model.save()
