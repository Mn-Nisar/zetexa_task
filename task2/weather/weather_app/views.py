from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny

from .models import Weather

@api_view(['GET'])
@permission_classes([AllowAny])

def report_weather(request):
    city = request.GET.get('city')

    if not city:
        return Response({'error': 'City name is required'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        
        try:
            weather_data = Weather.objects.get(city=city)
            return Response({
                'city': weather_data.city,
                'temperature': weather_data.temperature,
                'humidity': weather_data.humidity
            })
        except Weather.DoesNotExist:
            return Response({'error': f'No weather data found for {city}'}, status=status.HTTP_404_NOT_FOUND)

    