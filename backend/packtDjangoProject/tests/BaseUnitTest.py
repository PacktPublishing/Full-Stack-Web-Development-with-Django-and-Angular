#! python
from packtDjangoApp.models import Address, Product, Invoice, Account, CurrencyEnum
from django.contrib.auth.models import User

ADDRESS_STREET='Street 1'
ADDRESS_NUMBER=22
ADDRESS_CITY='City 1'
ADDRESS_POSTALCODE='A0001'

def buildAddress():
    return Address.build(ADDRESS_STREET, ADDRESS_NUMBER, ADDRESS_CITY, ADDRESS_POSTALCODE) 

def persistAddress():
    return Address.objects.create(street=ADDRESS_STREET, number=ADDRESS_NUMBER, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)

USER_EMAIL='user1@packt.com'
USER_PASSWORD='P_assw0rd***'
USER_NAME='user1Name'
USER_FIRSTNAME='user1 Firstname'
USER_LASTNAME='user1 Lastname'

def persistUser():
    return User.objects.create(email=USER_EMAIL, password=USER_PASSWORD, username=USER_NAME)

PRODUCT_NAME='Product 1'
PRODUCT_PRICE=55.20
PRODUCT_CURRENCY= CurrencyEnum.EUR

def buildProduct():
    return Product.build(PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CURRENCY)

def persistProduct():
    return Product.objects.create(name=PRODUCT_NAME, price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)

INVOICE_NUMBER = 1

def persistAccount():
    instance: Account = Account.objects.create(address=persistAddress(), user=persistUser())
    return instance

def persistInvoice():
    product1: Product = persistProduct()
    product2: Product = Product.objects.create(name='Product 2', price=32.45, currency=CurrencyEnum.USD)
    instance: Invoice = Invoice.objects.create(invoice_number=INVOICE_NUMBER, account=persistAccount())
    instance.products.add(product1)
    instance.products.add(product2)
    return instance

def findAddressByStreetAndNumberAndPostalCode(addressStreet, addressNumber, addressPostalCode):
    return Address.objects.get(street=addressStreet, number=addressNumber ,postal_code=addressPostalCode)