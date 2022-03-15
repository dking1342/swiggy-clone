import uuid
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
    restaurants = Restaurant.objects.raw(
        'SELECT * FROM restaurants_restaurant INNER JOIN discount_discount ON restaurants_restaurant.discounts_id = discount_discount.discount_id')
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
        restaurant = Restaurant.objects.raw(
            'SELECT * FROM restaurants_restaurant INNER JOIN discount_discount ON restaurants_restaurant.discounts_id = discount_discount.discount_id')
        filtered_restaurant = []
        for r in restaurant:
            if r.restaurant_id == pk:
                filtered_restaurant.append(r)

        if len(filtered_restaurant):
            serializer = RestaurantSerializer(filtered_restaurant[0], many=False)
            response_object.update(
                timestamp=datetime.now(),
                status=http.HTTPStatus.OK.name,
                status_code=http.HTTPStatus.OK.value,
                message='Returning restaurant with id: {0}'.format(pk),
                data=[serializer.data]
            )
            return Response(response_object)
        else:
            raise Http404

    except:
        print("something went wrong")
        raise Http404
