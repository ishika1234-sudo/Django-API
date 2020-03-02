from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.order_by('-score')
    yes=models.Employee.objects.filter(score=90).count()
    dis=models.Employee.objects.distinct()
    serializer_class=serializers.EmployeeSerializers
