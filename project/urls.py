from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def blank(request):
    return HttpResponse("For API Used Only")


urlpatterns = [
    path('', blank),
    path('admin/', admin.site.urls),
    path('api/v1/', include('upwork.urls'))
]
