from rest_framework import serializers
from .models import Roomtype, Room, Record, Customer


class RoomtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roomtype
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomtypeSerializer()

    class Meta:
        model = Room
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class RecordSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer()
    # room = RoomSerializer()

    class Meta:
        model = Record
        fields = "__all__"
