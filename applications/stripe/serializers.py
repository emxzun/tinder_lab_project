from rest_framework import serializers

from applications.stripe.models import UserPayment


class StripeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPayment
        fields = '__all__'

