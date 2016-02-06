from django.contrib import admin
from trainsapp.models import *

class TrainStopInline(admin.TabularInline):
    model = TrainStop
    extra = 5

class TrainAdmin(admin.ModelAdmin):
    inlines = [TrainStopInline]

admin.site.register(Train, TrainAdmin)
admin.site.register(Station)
