#! python
from packtDjangoApp.models import Address, Product, Invoice, Account, CurrencyEnum
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

ADDRESS_STREET='Street 1'
ADDRESS_NUMBER=22
ADDRESS_CITY='City 1'
ADDRESS_POSTALCODE='A0001'

def buildAddress():
    return Address.build(ADDRESS_STREET, ADDRESS_NUMBER, ADDRESS_CITY, ADDRESS_POSTALCODE) 

def persistAddress():
    return Address.objects.create(street=ADDRESS_STREET, number=ADDRESS_NUMBER, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)

def findAddress():
    return Address.objects.get(street=ADDRESS_STREET, number=ADDRESS_NUMBER, postal_code=ADDRESS_POSTALCODE)

def populateAddresses():
    persistAddress()
    Address.objects.create(street=ADDRESS_STREET, number=2, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)
    Address.objects.create(street=ADDRESS_STREET, number=3, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)
    Address.objects.create(street=ADDRESS_STREET, number=4, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)
    Address.objects.create(street=ADDRESS_STREET, number=5, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)
    Address.objects.create(street=ADDRESS_STREET, number=6, city=ADDRESS_CITY, postal_code=ADDRESS_POSTALCODE)

USER_EMAIL='user1@packt.com'
USER_PASSWORD='P_assw0rd***'
USER_NAME='user1Name'
USER_FIRSTNAME='user1 Firstname'
USER_LASTNAME='user1 Lastname'

def persistUser(userName):
    try:
        return findUser(userName)
    except:    
        return User.objects.create(email=USER_EMAIL, password=make_password(USER_PASSWORD), username=userName, is_active=True)
    
def populateUsers():
    persistUser(USER_NAME)    
    persistUser('user2Name')
    persistUser('user3Name')
    persistUser('user4Name')
    persistUser('user5Name')
    persistUser('user6Name')

def findUser(userName):
    return User.objects.get(username=userName)

PRODUCT_NAME='Product 1'
PRODUCT_PRICE=55.20
PRODUCT_CURRENCY= CurrencyEnum.EUR

def buildProduct():
    return Product.build(PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_CURRENCY)

def persistProduct():
    return Product.objects.create(name=PRODUCT_NAME, price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)

def findProduct(productName):
    return Product.objects.get(name=productName)

def populateProducts():
    persistProduct()
    Product.objects.create(name='Product 2', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)
    Product.objects.create(name='Product 3', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)
    Product.objects.create(name='Product 4', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)
    Product.objects.create(name='Product 5', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)
    Product.objects.create(name='Product 6', price=PRODUCT_PRICE, currency=PRODUCT_CURRENCY)

def persistAccount():
    instance: Account = Account.objects.create(address=persistAddress(), user=persistUser(USER_NAME))
    return instance

def populateAccounts():
    persistAddress()
    populateUsers()
    Account.objects.create(address=findAddress(), user=findUser(USER_NAME))
    Account.objects.create(address=findAddress(), user=findUser('user2Name'))
    Account.objects.create(address=findAddress(), user=findUser('user3Name'))
    Account.objects.create(address=findAddress(), user=findUser('user4Name'))
    Account.objects.create(address=findAddress(), user=findUser('user5Name'))
    Account.objects.create(address=findAddress(), user=findUser('user6Name'))

INVOICE_NUMBER = 1

def persistInvoice():
    product1: Product = persistProduct()
    product2: Product = Product.objects.create(name='Product 2', price=32.45, currency=CurrencyEnum.USD)
    account: Account = persistAccount()
    instance: Invoice = Invoice.objects.create(invoice_number=INVOICE_NUMBER, account=account)
    instance.products.add(product1)
    instance.products.add(product2)
    return instance

def populateInvoices():
    populateProducts()
    account: Account = persistAccount()
    invoice: Invoice = Invoice.objects.create(invoice_number=INVOICE_NUMBER, account=account)
    invoice.products.add(findProduct(PRODUCT_NAME))
    invoice.products.add(findProduct('Product 2'))
    Invoice.objects.create(invoice_number=2, account=account)
    Invoice.objects.create(invoice_number=3, account=account)
    Invoice.objects.create(invoice_number=4, account=account)
    Invoice.objects.create(invoice_number=5, account=account)
    Invoice.objects.create(invoice_number=6, account=account)

def findAddressByStreetAndNumberAndPostalCode(addressStreet, addressNumber, addressPostalCode):
    return Address.objects.get(street=addressStreet, number=addressNumber ,postal_code=addressPostalCode)