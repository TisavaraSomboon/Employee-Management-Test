from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Employee, Position, Department
from .serializers import EmployeeSerializer, PositionSerializer, DepartmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-createdAt')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Enable filtering and searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Exact-match filter parameters (e.g. ?status=normal&manager=1)
    filterset_fields = ['status', 'manager']
    
    # Full-text search fields (e.g. ?search=John)
    search_fields = ['name', 'address']
    
    # Ordering options (e.g. ?ordering=-createdAt or ?ordering=name)
    ordering_fields = ['createdAt', 'name']


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]