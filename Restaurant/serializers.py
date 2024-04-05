from rest_framework import serializers
from .models import Booking, Menu


class BookingSerializer(serializers.ModelSerializer):
    
    booking_date = serializers.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M',  # Format that matches datetime-local input
                       '%Y-%m-%dT%H:%M:%S',  # Other possible formats you want to accept
                       '%Y-%m-%dT%H:%M:%S.%f',  # If you want to accept microseconds
                       'iso-8601']  # ISO format
    )
    
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
