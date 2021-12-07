from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderItemForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderItemForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JwqOHEY5X68cltujg3p45sJHa7Vme4bpIpNU8NMPapPQ7PAxFVZmHaMfWIpAsJaXlkUJ6O8JzMQyDvr0TmHDxQY00S3Izhfz1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
