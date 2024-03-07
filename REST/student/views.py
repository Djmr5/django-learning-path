from .serializers import StudentSerializer
from rest_framework import generics
from .models import Student
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSameUserOrAdmin
from rest_framework.response import Response

# Create your views here.
class StudentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSameUserOrAdmin]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()