from django.urls import path

from .views import (
    ItemView,
    BuyView,
)


urlpatterns = (
    path('item/<int:id>/', ItemView.as_view()),
    path('buy/<int:id>/', BuyView.as_view()),
)
