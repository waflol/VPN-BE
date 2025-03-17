from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView

from payment.models import Subscription
from payment.serializers import SubscriptionSerializer


# Create your views here.
class SubscriptionListView(ListAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
