import http
from datetime import datetime

from django.http import Http404
from django.shortcuts import render

from rest_framework.decorators import api_view


# Create your views here.
from rest_framework.response import Response

from apps.cuisines.models import Cuisines
from apps.cuisines.serializers import CuisinesSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'cuisines/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of cuisines'
        },
        {
            'Endpoint': 'cuisines/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single cuisine'
        },
        {
            'Endpoint': 'cuisines/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new cuisine'
        },
        {
            'Endpoint': 'cuisines/update/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing cuisine'
        },
        {
            'Endpoint': 'cuisines/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a cuisine'
        }
    ]
    return Response(routes)


response_object = {
    'timestamp': '',
    'status': '',
    'status_code': '',
    'message': '',
    'data': []
}


@api_view(['GET'])
def getCuisines(request):
    cuisines = Cuisines.objects.all()
    serializer = CuisinesSerializer(cuisines,many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all cuisines",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def getCuisine(request,pk):
    try:
        cuisine = Cuisines.objects.get(id=pk)
    except:
        raise Http404

    serializer = CuisinesSerializer(cuisine,many=False)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning a cuisine",
        data=serializer.data
    )
    return Response(response_object)