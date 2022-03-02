from datetime import datetime

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/restaurants/', include('apps.restaurants.urls')),
    path('api/v1/discounts/', include('apps.discount.urls')),
    path('api/v1/menu/', include('apps.menu.urls')),
    path('api/v1/userinfo/', include('apps.userinfo.urls')),
]


def response404(request, status=200, message='Not Found'):
    response_object = {
        'timestamp': datetime.now(),
        'status': 'Data unavailable',
        'status_code': 404,
        'message': message,
        'data': []
    }
    return JsonResponse(data=response_object, status=status)


def response500(request, status=500, message='Not Found'):
    response_object = {
        'timestamp': datetime.now(),
        'status': 'Error',
        'status_code': status,
        'message': message,
        'data': []
    }
    return JsonResponse(data=response_object, status=status)


handler404 = response404
handler500 = response500
