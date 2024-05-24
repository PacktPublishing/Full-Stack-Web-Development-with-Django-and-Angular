from django.contrib import admin

from .models import Address
from .models import Product
from .models import Invoice
from .models import Account

admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Account)
