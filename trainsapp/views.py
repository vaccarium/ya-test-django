from django.shortcuts import render, render_to_response, get_object_or_404
from trainsapp.models import *

def showtrain(request, trainid):
	train = get_object_or_404(Train, id=trainid)
	return render_to_response('trainsapp/showtrain.htm', {
		'number': train.number,
		'name': train.name,
		'departure': train.departure,
		'intermediate': train.intermediatestop_set.all(),
		'arrival': train.arrival
	})
