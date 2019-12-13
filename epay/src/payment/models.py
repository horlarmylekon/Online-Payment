from decimal import Decimal

from django.db import models
from payments import PurchasedItem
from payments.models import BasePayment

# Create your models here.


class Payment(BasePayment):

    currency = models.CharField(max_length=10)

    def get_failure_url(self):
        return 'failure.html'
    
    def get_success_url(self):
        return 'success.html'

    def get_purchased_items(self):

        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV',
                    quantity=9, price=Decimal(10), currency='USD')
