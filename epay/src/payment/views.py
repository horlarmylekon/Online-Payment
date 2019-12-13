# mypaymentapp/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from payments import get_payment_model, RedirectNeeded

from . import forms


class performPayment(LoginRequiredMixin, generic.TemplateView):
    template_name = "payment/perform_payment.html"
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        if "payment_form" not in kwargs:
            kwargs["payment_form"] = forms.PaymentForm()
        return super().get(request, *args, **kwargs)


def showAllPayment(request):
    return render(request, template_name='payment/record/view.html')
