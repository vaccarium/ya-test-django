from django.contrib import admin
from trainsapp.models import *

class IntermediateStopInline(admin.TabularInline):
    model = IntermediateStop
    extra = 5

class TrainAdmin(admin.ModelAdmin):
    inlines = (IntermediateStopInline, )

admin.site.register(Train, TrainAdmin)
admin.site.register(Station)
admin.site.register(Departure)
admin.site.register(Arrival)
