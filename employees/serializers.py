from rest_framework import serializers
from .models import Employee, Position, Department


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    # Optional: Display nested manager and department names in GET responses
    manager_name = serializers.ReadOnlyField(source='manager.name')

    class Meta:
        model = Employee
        fields = '__all__'