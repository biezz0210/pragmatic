from django.urls import path

from subscribeapp.views import SubscriptionView, SubscriptionListVeiw

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListVeiw.as_view(), name='list'),
]
