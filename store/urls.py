from django.urls import path
from store.views import(
    CheckoutPage, home,
    cart, updateItem, processOrder,
    stripe_config, create_checkout_session,
    stripe_webhook,
)

urlpatterns = [
    path('', home, name='home'),
    path('checkout/', CheckoutPage.as_view(), name='checkout'),
    path('cart/', cart, name='cart'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('webhook/', stripe_webhook),
]
