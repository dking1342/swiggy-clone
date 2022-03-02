from datetime import datetime
import http

from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Restaurant
from .serializers import RestaurantSerializer


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'restaurants/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of restaurants'
        },
        {
            'Endpoint': 'restaurants/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single restaurant'
        },
        {
            'Endpoint': 'restaurants/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new restaurant'
        },
        {
            'Endpoint': 'restaurants/update/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing restaurant'
        },
        {
            'Endpoint': 'restaurants/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a restaurant'
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
def getRestaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all restaurants",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def getRestaurant(request, pk):
    try:
        restaurant = Restaurant.objects.get(id=pk)
    except:
        raise Http404

    serializer = RestaurantSerializer(restaurant, many=False)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message='Returning restaurant with id: {0}'.format(pk),
        data=[serializer.data]
    )

    return Response(response_object)


# @api_view(['POST'])
# def createRestaurant(request):
#     data = request.data
#     serializer = RestaurantSerializer(data=data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)

