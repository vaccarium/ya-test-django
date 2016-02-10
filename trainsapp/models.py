from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class Train(models.Model):
    number = models.CharField(max_length = 6)
    name = models.CharField(max_length = 100, null = True, blank = True)

    departure = models.OneToOneField("Departure")
    arrival = models.OneToOneField("Arrival")
    
    def __unicode__(self):
        return u"(Train {}, id {})".format(self.number, self.id)

    def clean(self):
        try:
            departure = self.departure
        except ObjectDoesNotExist:
            raise ValidationError(u"The Departure does not exist.")
        try:
            arrival = self.arrival
        except ObjectDoesNotExist:
            raise ValidationError(u"The Arrival does not exist.")
        if departure > arrival:
            raise ValidationError(u"Trains should arrive after they depart.")

class Station(models.Model):
    code = models.BigIntegerField(unique = True)
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

    def clean(self):
        if self.arrival > self.departure:
            raise ValidationError(u"Trains cannot arrive after departure.")
        departure = self.train.departure
        arrival = self.train.arrival
        if not (departure <= self.departure <= self.arrival <= arrival):
            raise ValidationError(u"IntermediateStops should lie between train departure and arrival.")

    class Meta:
        ordering = ('departure',)

class Departure(models.Model):
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
