from django.urls import path
from . import views

app_name = "payment"
urlpatterns = [
    path("payment/all", views.showAllPayment,name="show_payment"),
    path("", views.performPayment.as_view(), name="perform_payment"),

]
