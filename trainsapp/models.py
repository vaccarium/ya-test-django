from __future__ import unicode_literals

from django.db import models

class Train(models.Model):
    id = models.AutoField()
    number = models.CharField(max_length = 6)
    name = models.CharField(max_length = 100, null = True)
    
    def __unicode__(self):
        return u"(Train {}, id {})".format(self.number, self.id)

class Station(models.Model):
    code = models.BigIntegerField()
    name = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return u"(Station {}, code {})".format(self.name, self.code)

class TrainStop(models.Model):
    train = models.ForeignKey(Train)
    station = models.ForeignKey(Station)
    arrival = models.DateTimeField(null = True)
    departure = models.DateTimeField(null = True)
    
    def __unicode__(self):
        return u"(Stop at {} from {} to {})".format(
            self.station.name,
            self.arrival,
            self.departure
        )
