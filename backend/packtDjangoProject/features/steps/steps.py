from behave import given, when, then
from packtDjangoApp.models import Product
from tests.BaseUnitTest import buidProduct

@given("an instance")
def step_given(context):
    context.product = buidProduct()

@when("saving the instance")
def step_when(context):
    context.product.save()

@then("the instance is saved in the DB")
def step_then(context):
        context.persistedProducts = Product.objects.all()
        assert context.persistedProducts.count() == 1