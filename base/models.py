from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20)
    nrc_id = models.CharField(max_length=20)

    def __str__(self):
        return f"customer name: {self.name}"


class Roomtype(models.Model):
    type = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return f"room type :{self.type}"


class Room(models.Model):
    room_type = models.ForeignKey(Roomtype, on_delete=models.CASCADE)
    no = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"room  no :{str(self.no)}"


class Record(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"customer:{self.customer}, checkin :{self.checkin}, checkout :{self.checkout}"
