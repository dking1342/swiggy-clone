import http
import uuid
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
def get_users_info(request):
    users = Userinfo.objects.all()
    serializer = UserinfoSerializer(users, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all users",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def get_user_info(request, pk):
    print(pk)
    try:
        user = Userinfo.objects.get(user_phone=pk)
        serializer = UserinfoSerializer(user, many=False)
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.OK.name,
            status_code=http.HTTPStatus.OK.value,
            message='Returning user with phone number: {0}'.format(pk),
            data=serializer.data
        )
        return Response(response_object)
    except:
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.BAD_REQUEST.name,
            status_code=http.HTTPStatus.BAD_REQUEST.value,
            message='Please try again',
            data=[]
        )
        return Response(response_object)


@api_view(['POST'])
def create_user(request):
    try:
        phone = request.data['phone']
        user = Userinfo.objects.all()
    except:
        raise Http404

    does_user_exists = False
    serializer_users = UserinfoSerializer(user, many=True)
    for u in serializer_users.data:
        if u['user_phone'] == phone:
            does_user_exists = True

    if does_user_exists:
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.BAD_REQUEST.name,
            status_code=http.HTTPStatus.BAD_REQUEST.value,
            message='User already exists',
            data=[]
        )
    else:
        user = {
            "user_id": uuid.uuid4(),
            "user_name": request.data['name'],
            "user_phone": request.data['phone'],
            "user_email": request.data['email']
        }
        serializer = UserinfoSerializer(data=user)
        if serializer.is_valid():
            response_object.update(
                timestamp=datetime.now(),
                status=http.HTTPStatus.OK.name,
                status_code=http.HTTPStatus.OK.value,
                message='Saving the user',
                data=serializer.validated_data
            )
            serializer.save()
        else:
            response_object.update(
                timestamp=datetime.now(),
                status=http.HTTPStatus.BAD_REQUEST.name,
                status_code=http.HTTPStatus.BAD_REQUEST.value,
                message='Error when saving the user',
                data=[]
            )
            raise Http404

    return Response(response_object)

