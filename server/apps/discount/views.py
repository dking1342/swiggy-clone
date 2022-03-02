import http
from datetime import datetime

from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.discount.models import Discount
from apps.discount.serializers import DiscountSerializer


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'discounts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of discounts'
        },
        {
            'Endpoint': 'discounts/:id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single discount'
        },
        {
            'Endpoint': 'discounts/create',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new discount'
        },
        {
            'Endpoint': 'discounts/update/id',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing discount'
        },
        {
            'Endpoint': 'discounts/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a discount'
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
def getDiscounts(request):
    discounts = Discount.objects.all()
    serializer = DiscountSerializer(discounts,many=True)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning all discounts",
        data=serializer.data
    )
    return Response(response_object)

@api_view(['GET'])
def getDiscount(request,pk):
    try:
        discount = Discount.objects.get(id=pk)
    except:
        raise Http404

    serializer = DiscountSerializer(discount,many=False)
    response_object.update(
        timestamp=datetime.now(),
        status=http.HTTPStatus.OK.name,
        status_code=http.HTTPStatus.OK.value,
        message="Returning discount with id: {0}".format(pk),
        data=[serializer.data]
    )
    return Response(response_object)

