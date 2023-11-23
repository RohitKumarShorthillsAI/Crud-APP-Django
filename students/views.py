from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from authentication.models import Student
from .permissions import IsOwnerOrReadOnly
from .serializers import StudentSerializer
from .pagination import CustomPagination
from .filters import StudentFilter
from rest_framework.response import Response


class ListCreateStudentAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyStudentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, *args, **kwargs):
        # print(kwargs['pk'])
        std=Student.objects.filter(id=kwargs['pk'])
        std.delete()
        return Response("deleted")

    def patch(self, request, *args, **kwargs):
        std=Student.objects.filter(id=kwargs['pk'])[0]
        std.address=request.data['address']
        std.name=request.data['name']
        std.age=request.data['age']
        std.save()
        return Response("Updated")
       




