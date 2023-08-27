from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from company.models import Employees, Branches, Departments


class TestCaseUserAPIView(TestCase):
    def setUp(self):
        self.client = APIClient()
        branch = Branches.objects.create(address="Address", short_name="Short name")
        department = Departments.objects.create(department_name="Department", floor=1, branch=branch)
        self.url = reverse('get_post_employees')

        # Создание тестовых данных
        Employees.objects.create(
            full_name="John Doe",
            position="Manager",
            phone_number="123456789",
            birthdate="1990-01-01",
            email="john.doe@example.com",
            department=department
        )

    def test_get_all_employees(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
