from django.urls import path

from payment.views import SubscriptionListView

app_name = "payment"
urlpatterns = [
    path("subscriptions/", SubscriptionListView.as_view(), name="subscription_list"),
]
