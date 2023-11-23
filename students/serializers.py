from rest_framework import serializers
from authentication.models import Student
from django.contrib.auth.models import User


class StudentSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Student
        fields = ( 'name', 'degree', 'age', 'sex', 'address', 'creator')




class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    students = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ( 'username', 'students')
