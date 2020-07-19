from django.urls import include, path
from rest_framework import routers

from events.views import EventViewSet, EventTypeViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'eventtypes', EventTypeViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
