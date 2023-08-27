from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from company.models import Employees, Departments
from company.serializers import EmployeesSerializer, DepartmentsSerializer


class EmployeesAPIView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Employees.objects.filter(id=pk)
            if queryset.exists():
                serializer = EmployeesSerializer(queryset, many=True)
                data = serializer.data
                return Response({'Employees': data})
            else:
                return Response({'error': 'User with provided pk does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Employees.objects.all()
            serializer = EmployeesSerializer(queryset, many=True)
            return Response({'Employees': serializer.data})


class DepartmentsAPIView(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Departments.objects.filter(id=pk)
            if queryset.exists():
                serializer = DepartmentsSerializer(queryset, many=True)
                data = serializer.data
                return Response({'Departments': data})
            else:
                return Response({'error': 'Departments with provided pk does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = Departments.objects.all()
            serializer = DepartmentsSerializer(queryset, many=True)
            return Response({'Departments': serializer.data})
