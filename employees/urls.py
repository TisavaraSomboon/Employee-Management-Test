from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, PositionViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'positions', PositionViewSet, basename='position')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = router.urls