from .models import Student
from rest_framework import viewsets, permissions, status
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Delete operation is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)