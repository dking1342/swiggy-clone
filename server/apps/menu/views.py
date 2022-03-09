import http
from datetime import datetime

from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.menu.models import Menu
from apps.menu.serializers import MenuSerializer


# Create your views here.
@api_view(['GET'])
def get_routes(request):
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
def get_menus(request):
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
def get_menu(request, pk):
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


@api_view(['GET'])
def get_menu_restaurant(request, pk):
    try:
        menu = Menu.objects.all()
        filtered_menu = []
        for m in menu:
            if m.restaurant.restaurant_id == pk:
                filtered_menu.append(m)

        if len(filtered_menu):
            serializer = MenuSerializer(filtered_menu,many=True)
            response_object.update(
                timestamp=datetime.now(),
                status=http.HTTPStatus.OK.name,
                status_code=http.HTTPStatus.OK.value,
                message='Returning menu with restaurant id: {0}'.format(pk),
                data=serializer.data
            )
            return Response(response_object)
        else:
            raise Http404
    except:
        print("error happened")
        raise Http404
