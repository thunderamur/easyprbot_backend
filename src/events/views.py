import django_filters
from rest_framework import viewsets

from .models import Event, EventType
from .serializers import EventCreateSerializer, EventDetailSerializer, EventTypeSerializer


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'title': ['icontains'],
            'start_time': ['gt', 'lt']
        }


class EventViewSet(viewsets.ModelViewSet):
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update', 'update'):
            return EventCreateSerializer
        return EventDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
