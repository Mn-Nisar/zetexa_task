from rest_framework import serializers
from .models import User,Task

class taskSerializer(serializers.ModelSerializer):
     class Meta:
          model = Task
          fields = '__all__'