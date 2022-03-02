import datetime

from django.http import JsonResponse
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    response_object = {
        'timestamp': '',
        'status': '',
        'status_code': '',
        'message': '',
        'data': []
    }

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['timestamp'] = datetime.datetime.now()
        response.data['status'] = "Error"
        response.data['message'] = response.data['detail'],
        response.data['status_code'] = response.status_code
        response.data['data'] = []
        print(response.data['detail'])
    return response
# class custom_exception_handler:

