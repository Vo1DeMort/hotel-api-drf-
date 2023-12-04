from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
    IsAuthenticated,
)
from .models import Room, Record, Customer
from .serializers import RoomSerializer, RecordSerializer, CustomerSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def testjwt(request):
    return Response({"test": "test is good"})


class Checkrooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        available_rooms = Room.objects.filter(available=True)

        if not available_rooms.exists():
            return Response(
                {"info": "no rooms are available for now"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return available_rooms


class CreateCustomers(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


"""
the create method is typically responsible for handling the HTTP request and the 
initial creation logic, and perform_create is used for additional logic after the 
instance has been created
"""


class Checkin(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAdminUser]

    # this works
    def perform_create(self, serializer):
        obj = serializer.save()
        """
        when i wrote ,obj.room.available = False
                      obj.room.save() donesn't work ??
        """
        room_obj = obj.room
        room_obj.available = False
        room_obj.save()
        return obj


"""why not just do the calculations and return the bill , why do i stll using RetrieveAPIView"""


# working
@api_view(["GET"])
@permission_classes([IsAdminUser])
def calculateBill(request, obj_id):
    try:
        record = Record.objects.get(id=obj_id)
    except Record.DoesNotExist:
        return Response({"error": "record not found"}, status=status.HTTP_404_NOT_FOUND)

    roomType = record.room.room_type
    time = record.checkout - record.checkin
    ppn = roomType.price
    total = time.days * ppn

    response_data = {"detail": {"duration": time.total_seconds(), "cost": total}}

    return Response(response_data, status=status.HTTP_200_OK)


class Checkout(generics.UpdateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAdminUser]

    # working properly
    def perform_update(self, serializer):
        # obj is the instance of Record model
        obj = serializer.save()
        room_obj = obj.room
        room_obj.available = True
        room_obj.save()

        return obj
