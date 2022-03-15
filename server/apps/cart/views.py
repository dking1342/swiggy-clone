import http
import uuid
from datetime import datetime

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from apps.cart.models import Cart
from apps.cart.serializers import CartSerializer


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': 'cart/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of cart'
        },
        {
            'Endpoint': 'cart/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single cart'
        },
        {
            'Endpoint': 'cart/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new cart'
        },
        {
            'Endpoint': 'cart/update/:id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing cart'
        },
        {
            'Endpoint': 'cart/delete/:id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an cart'
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
def get_orders(request):
    orders = Cart.objects.all()
    serializer = CartSerializer(orders, many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all cart",
        data=serializer.data
    )
    return Response(response_object)


@api_view(['GET'])
def get_order(request, pk):
    try:
        order = Cart.objects.raw(
            'SELECT * '
            'FROM cart_cart '
            'WHERE order_reference = %s', [pk]
        )

        serializer = CartSerializer(order, many=True)
        response_object.update(
            timestamp=datetime.now(),
            status=http.HTTPStatus.OK.name,
            status_code=http.HTTPStatus.OK.value,
            message='Returning order with id: {0}'.format(pk),
            data=serializer.data
        )
        return Response(response_object)

    except:
        raise Http404


@api_view(['POST'])
def create_order(request):
    cart_order = JSONParser().parse(request)
    order_items = cart_order['order_item']
    order_reference_id = uuid.uuid4()
    response_list = []

    for order in order_items:
        item = {
            "order_item_id": uuid.uuid4(),
            "order_item_name": order['order_item_name']['menu_item'],
            "order_item_quantity": order['order_item_quantity'],
            "order_item_price": order['order_item_name']['menu_price'],
            "order_item_cost": order['order_item_name']['menu_price'] * order['order_item_quantity'],
            "order_reference": order_reference_id,
            "order_restaurant": order['order_item_name']['restaurant']
        }

        serializer = CartSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            response_list.append(item)
        else:
            print(serializer.errors)
            raise Http404

    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message='Saving the order',
        data=response_list
    )
    return Response(response_object)

