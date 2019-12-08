from django.urls import path
from rest_framework import routers
from upwork.views import JobViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Jobs API')

router = routers.DefaultRouter()
router.register('job', JobViewSet)
urlpatterns = [
#     path('docs/', schema_view)
]
urlpatterns += router.urls
