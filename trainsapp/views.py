from django.shortcuts import render, render_to_response, get_object_or_404
from trainsapp.models import *
from datetime import datetime, timedelta
import calendar

def showtrain(request, trainid):
	train = get_object_or_404(Train, id=trainid)
	return render_to_response('trainsapp/showtrain.htm', {
		'number': train.number,
		'name': train.name,
		'departure': train.departure,
		'intermediate': train.intermediatestop_set.all(),
		'arrival': train.arrival
	})

def showstation(request, stationcode, year, month):
	station = get_object_or_404(Station, code=stationcode)

	year = int(year)
	month = int(month)
	startpadding, monthlength = calendar.monthrange(year, month)
	endpadding = 7 - calendar.weekday(year, month, monthlength) - 1
	firstday = datetime(year, month, 1)
	lastday = datetime(year, month, monthlength, 23, 59, 59)	# screw the leap second

	departures = Departure.objects.filter(station__code=stationcode).exclude(departure__lt=firstday).exclude(departure__gt=lastday)
	intermediates = IntermediateStop.objects.filter(station__code=stationcode).exclude(departure__lt=firstday).exclude(departure__gt=lastday)
	arrivals = Arrival.objects.filter(station__code=stationcode).exclude(arrival__lt=firstday).exclude(arrival__gt=lastday)

	# this lists events by the day
	daylist = [[] for day in range(monthlength)]
	for queryset in departures, intermediates, arrivals:
		for event in queryset:
			daylist[event.sorting_date.day - 1].append(event)
	# and this converts them into a 2D matrix where rows are weeks
	# that should make template rendering easier
	weeks = []
	if startpadding:
		weeks.append([])
	for day in range(startpadding):
		weeks[-1].append(None)
	for day in range(monthlength):
		if (day + startpadding) % 7 == 0:
			weeks.append([])
		weeks[-1].append({'day': day + 1, 'stops': sorted(daylist[day], key=lambda event: event.sorting_date)})
	for day in range(endpadding):
		weeks[-1].append(None)

	if month == 1:
		prevmonth = {'year': year - 1, 'month': 12}
	else:
		prevmonth = {'year': year, 'month': month - 1}
	if month == 12:
		nextmonth = {'year': year + 1, 'month': 1}
	else:
		nextmonth = {'year': year, 'month': month + 1}

	return render_to_response('trainsapp/showstation.htm', {
		'stationcode': station.code,
		'name': station.name,
		'year': year,
		'month': month,
		'startpadding': startpadding,
		'endpadding': endpadding,
		'prevmonth': prevmonth,
		'nextmonth': nextmonth,
		'weeks': weeks
	})
