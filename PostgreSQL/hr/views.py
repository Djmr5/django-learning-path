from rest_framework.generics import ListCreateAPIView
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = [EmployeeSerializer]
