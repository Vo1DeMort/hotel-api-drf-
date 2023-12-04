from django.urls import path
from . import views

urlpatterns = [
    path("", views.Checkrooms.as_view(), name="checkrooms"),
    path("createuser/", views.CreateCustomers.as_view(), name="createcustomers"),
    path("checkin/", views.Checkin.as_view(), name="checkin"),
    path("checkout/<int:pk>/", views.Checkout.as_view(), name="checkout"),
    path("bill/<int:obj_id>/", views.calculateBill, name="bill"),
    path("test/", views.testjwt, name="testing_jwt"),
]
