from django.db.models import fields

from rest_framework import serializers 
from .models import Student, Exams, LGA, School


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exams
        fields = ['student', 'subject', 'score' 'year']


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'school', 'current_class']


class LGASerializer(serializers.ModelSerializer):

    class Meta:
        model = LGA
        fields = ['name', 'state']


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exams
        fields = ['student', 'exam_type', 'year', 'subject', 'score']
