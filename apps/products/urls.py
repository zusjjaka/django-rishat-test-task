from django.urls import path

from .views import (
    ItemView,
    BuyView,
    HomePageView,
)


urlpatterns = (
    path('', HomePageView.as_view()),
    path('item/<int:id>/', ItemView.as_view()),
    path('item/', ItemView.as_view()),
    path('buy/<int:id>/', BuyView.as_view()),
)
