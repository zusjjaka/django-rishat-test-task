from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    """Item model."""
    name: str = models.CharField(
        verbose_name=_('название'),
        max_length=30
    )
    description: str = models.TextField(
        verbose_name=_('описание')
    )
    price: float = models.DecimalField(
        verbose_name=_('цена'),
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = (
            'id',
        )
