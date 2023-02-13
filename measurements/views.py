from django.http import HttpResponse
from .logic import measurements_logic as ml
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def measurements_view(request):
    if request.method =='GET':
        measurements = ml.get_measurements()
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, 'application/json')

def measurement_view (request, pk):
    if request.method == 'GET':
        measurement = ml.get_measurement(pk)
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        measurement_dto = ml.create_variable(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ml.get_variable(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = ml.update_variable(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
