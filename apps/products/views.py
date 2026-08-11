from django.shortcuts import render
from django.db.models import QuerySet
from django.views import View
from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.conf import settings

import stripe

import typing as t

from .models import Item


stripe.api_key = settings.STRIPE_SEC_KEY

class HomePageView(View):
    """HomePage."""
    def get(self,
            request: HttpRequest,
            *args: t.Any,
            **kwargs: t.Any) -> HttpResponse:
        return render(request, 'home.html')


class ItemView(View):
    """Show items info."""
    def get(self,
            request: HttpRequest,
            id: int = None,
            *args: t.Any,
            **kwargs: t.Any) -> HttpResponse:
        if id is None:
            item_queryset: QuerySet[Item] = Item.objects.all()
            return render(request, 'item.html', {'item_list': item_queryset})

        item: Item = get_object_or_404(Item, id=id)
        return render(request, 'item.html', 
                      {'item': item,
                       'stripe_pub_key': settings.STRIPE_PUB_KEY})


class BuyView(View):
    """Create Stripe session."""
    def get(self,
            request: HttpRequest,
            id: int,
            *args: t.Any,
            **kwargs: t.Any) -> HttpResponse:
        item: Item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            line_items= [{
                'price_data': {
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'currency': 'RUB',
                    'unit_amount': int(item.price * 100)
                },
                'quantity': 1
            }],
            mode='payment',
            success_url=f'http://127.0.0.1:8000/item/{item.id}/?success=true'
        )

        return JsonResponse({'session_id': session.id})
