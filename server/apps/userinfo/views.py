import http
from datetime import datetime

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.userinfo.models import Userinfo
from apps.userinfo.serializers import UserinfoSerializer


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'userinfo/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of users'
        },
        {
            'Endpoint': 'userinfo/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single user'
        },
        {
            'Endpoint': 'userinfo/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new user'
        },
        {
            'Endpoint': 'userinfo/update/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing user'
        },
        {
            'Endpoint': 'userinfo/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a user'
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
def getUserinfos(request):
    users = Userinfo.objects.all()
    serializer = UserinfoSerializer(users,many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all users",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def getUserinfo(request,pk):
    try:
        user = Userinfo.objects.get(id=pk)
    except:
        raise Http404

    serializer = UserinfoSerializer(user,many=False)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message='Returning user with id: {0}'.format(pk),
        data=[serializer.data]
    )
    return Response(response_object)

