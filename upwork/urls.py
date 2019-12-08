from rest_framework import routers

from upwork.views import JobViewSet

router = routers.DefaultRouter()
router.register('job', JobViewSet)
urlpatterns = []
urlpatterns += router.urls
