import os
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee, Status


class EmployeeAPITests(APITestCase):

    def setUp(self):
        # 1. Create a test user for authentication
        self.user = User.objects.create_user(
            username='testuser', 
            password='password123'
        )

        # 2. Ensure test image file exists
        self.image_dir = str(os.path.join(settings.LOCAL_FILE_DIR, "images"))
        os.makedirs(self.image_dir, exist_ok=True)
        self.test_image_path = os.path.join(self.image_dir, "test.jpg")
        if not os.path.exists(self.test_image_path):
            with open(self.test_image_path, "w") as f:
                f.write("test")

        # 3. Seed initial employee records
        self.emp1 = Employee.objects.create(
            name="Alice Smith",
            address="123 Alpha St",
            image=self.test_image_path,
            status=Status.NORMAL
        )
        self.emp2 = Employee.objects.create(
            name="Bob Jones",
            address="456 Beta Ave",
            image=self.test_image_path,
            status=Status.PROBATION,
            manager=self.emp1
        )

    def test_get_employee_list(self):
        """Test retrieving the list of employees"""
        response = self.client.get('/api/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_employee_by_status(self):
        """Test filtering employees by status choice"""
        response = self.client.get('/api/employees/?status=normal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Alice Smith")

    def test_search_employee_by_name(self):
        """Test full-text search by employee name"""
        response = self.client.get('/api/employees/?search=Bob')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Bob Jones")

    def test_create_employee_authenticated(self):
        """Test creating an employee when logged in"""
        self.client.login(username='testuser', password='password123')
        data = {
            "name": "Charlie Brown",
            "address": "789 Gamma Rd",
            "image": self.test_image_path,
            "status": Status.RECRUITMENT_PROCESS
        }
        response = self.client.post('/api/employees/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 3)

    def test_delete_employee(self):
        """Test deleting an employee record"""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(f'/api/employees/{self.emp2.id}/')
        self.assertEqual(response.status_code, status.HTTP_24_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 1)