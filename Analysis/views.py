from django.db.models import Lookup
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from .models import Student, Exams, School, LGA
from .serializer import ExamSerializer, StudentSerializer, SchoolSerializer


# Create your views here.

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()[:5]
    serializer_class = StudentSerializer

class StudentListCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"


class SchoolCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = "pk"

class ExamCreateView(generics.CreateAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamSerializer

class ExamListView(generics.ListAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamSerializer


class ExamUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamSerializer
    lookup_field = "pk"
