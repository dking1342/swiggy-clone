import http
import uuid
from datetime import datetime

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.rating.models import Rating
from apps.rating.serializers import RatingSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': 'rating/list',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of ratings'
        },
        {
            'Endpoint': 'rating/get/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single rating'
        },
        {
            'Endpoint': 'rating/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new rating'
        },
        {
            'Endpoint': 'rating/update/:id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing rating'
        },
        {
            'Endpoint': 'rating/delete/:id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an rating'
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
def get_ratings(request):
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all ratings",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def get_rating(request, pk):
    try:
        rating = Rating.objects.raw(
            'SELECT * '
            'FROM rating_rating '
            'WHERE rating_rating.rating_order_reference = %s', [pk]
        )
        serializer = RatingSerializer(rating, many=True)
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.OK.name,
            status_code=http.HTTPStatus.OK.value,
            message="Returning single cart",
            data=serializer.data
        )
        return Response(response_object)
    except:
        print("error")
        raise Http404


@api_view(['POST'])
def create_rating(request):
    request.data['rating_id'] = uuid.uuid4()
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.OK.name,
            status_code=http.HTTPStatus.OK.value,
            message='Saving the rating',
            data=serializer.data
        )
        return Response(response_object)
    else:
        print(serializer.errors)
        raise Http404
