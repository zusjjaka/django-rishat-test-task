from django.db import models
from django.conf import settings
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from decimal import Decimal


class Item(models.Model):
    """Item model."""
    name: str = models.CharField(
        verbose_name=_('название'),
        max_length=30
    )
    description: str = models.TextField(
        verbose_name=_('описание')
    )
    price: Decimal = models.DecimalField(
        verbose_name=_('цена'),
        max_digits=8,
        decimal_places=2
    )
    currency: str = models.SmallIntegerField(
        verbose_name=_('валюта'),
        default=1,
        choices=settings.CURRENCIES
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = (
            'id',
        )


class Order(models.Model):
    """Bucket of items model."""
    def total_sum(self) -> Decimal:
        order_item_list: QuerySet[OrderItem] = self.items.select_related("item")
        total: Decimal = 0

        for order_item in order_item_list:
            total += order_item.item.price * order_item.quantity

        return total

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'


class OrderItem(models.Model):
    """Item in the bucket."""
    order: Order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    item: 'Item' = models.ForeignKey(
        Item,
        on_delete = models.CASCADE
    )
    quantity: int = models.SmallIntegerField(
        verbose_name=_('количество'),
        default=1
    )

    class Meta:
        verbose_name = 'позиция'
        verbose_name_plural = 'позиции'
