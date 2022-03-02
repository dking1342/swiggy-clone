import http
from datetime import datetime

from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.menu.models import Menu
from apps.menu.serializers import MenuSerializer


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'menu/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of menus'
        },
        {
            'Endpoint': 'menu/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single menu item'
        },
        {
            'Endpoint': 'menu/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new menu'
        },
        {
            'Endpoint': 'menu/update/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing menu'
        },
        {
            'Endpoint': 'menu/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a menu'
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
def getMenus(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all menus",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def getMenu(request, pk):
    try:
        menu = Menu.objects.get(id=pk)
    except:
        raise Http404
    serializer = MenuSerializer(menu, many=False)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message='Returning menu with id: {0}'.format(pk),
        data=[serializer.data]
    )

    return Response(response_object)
