from django.contrib import admin
from trainsapp.models import *

class IntermediateStopInline(admin.TabularInline):
    model = IntermediateStop
    extra = 5
class ArrivalInline(admin.TabularInline):
    model = Arrival
class DepartureInline(admin.TabularInline):
    model = Departure

class TrainAdmin(admin.ModelAdmin):
    inlines = (DepartureInline, IntermediateStopInline, ArrivalInline)

admin.site.register(Train, TrainAdmin)
admin.site.register(Station)
