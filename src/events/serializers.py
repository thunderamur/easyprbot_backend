from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers

from .models import Event, EventType


class EventTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventType
        fields = ['url', 'id', 'name']


class EventCreateSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Event
        fields = ['url', 'id', 'user', 'type', 'title', 'description', 'start_time', 'notified']


class EventDetailSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=EventType.objects.all(),
        view_name='eventtype-detail'
    )

    class Meta:
        model = Event
        fields = ['url', 'id', 'user', 'type', 'title', 'description', 'start_time', 'notified']
