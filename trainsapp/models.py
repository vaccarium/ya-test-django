from __future__ import unicode_literals

from django.db import models

class Train(models.Model):
    number = models.CharField(max_length = 6)
    name = models.CharField(max_length = 100, null = True, blank = True)
    
    def __unicode__(self):
        return u"(Train {}, id {})".format(self.number, self.id)

class Station(models.Model):
    code = models.BigIntegerField()
    name = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return u"(Station {}, code {})".format(self.name, self.code)

class IntermediateStop(models.Model):
    train = models.ForeignKey(Train)
    station = models.ForeignKey(Station)
    arrival = models.DateTimeField()
    departure = models.DateTimeField()

    @property
    def duration(self):
        return self.departure - self.arrival

    @property
    def sorting_date(self):
        return self.departure

    def __unicode__(self):
        return u"(Stop at {} from {} to {})".format(
            self.station.name,
            self.arrival,
            self.departure
        )

    class Meta:
        ordering = ('departure',)

    #def clean

class Departure(models.Model):
    train = models.OneToOneField(Train)
    station = models.ForeignKey(Station)
    departure = models.DateTimeField()
    
    @property
    def sorting_date(self):
        return self.departure
    
    def __unicode__(self):
        return u"(Departure from {} at {})".format(
            self.station.name,
            self.departure
        )

class Arrival(models.Model):
    train = models.OneToOneField(Train)
    station = models.ForeignKey(Station)
    arrival = models.DateTimeField()

    @property
    def sorting_date(self):
        return self.arrival
    
    def __unicode__(self):
        return u"(Arrival at {} at {})".format(
            self.station.name,
            self.arrival
        )
