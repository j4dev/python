from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student

class StudentAPITest(APITestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone="+1234567890",
            date_of_birth="2000-01-01",
            grade=8
        )
        self.student_url = f'/students/{self.student.pk}/'
        self.students_url = '/students/'

    def test_student_creation(self):
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@example.com",
            "phone": "+0987654321",
            "date_of_birth": "2001-01-01",
            "grade": 9
        }
        response = self.client.post(self.students_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 2)
        self.assertEqual(Student.objects.get(email="janedoe@example.com").first_name, "Jane")

    def test_student_read(self):
        response = self.client.get(self.student_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], "John")
        self.assertEqual(response.data['last_name'], "Doe")

    def test_student_update(self):
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone": "+1234567890",
            "date_of_birth": "2000-01-01",
            "grade": 8
        }
        response = self.client.put(self.student_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get(email="johndoe@example.com").first_name, "Jane")

    def test_student_not_found(self):
        non_existent_url = '/students/999/'
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)