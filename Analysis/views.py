from django.db.models import Lookup, Avg
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student, Exams, School, LGA
from .serializer import ExamSerializer, StudentSerializer, SchoolSerializer
from django_filters.rest_framework import DjangoFilterBackend


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
    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
    'year': ['exact'],
    'exam_type': ['exact', 'iexact'],
    'subject': ['exact', 'iexact'],
    'student__school__lga__name': ['exact', 'iexact']
    }


class ExamUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamSerializer
    lookup_field = "pk"



class PerformanceTrendView(APIView):

    def get(self, request):
        queryset = Exams.objects.select_related('student__school__lga')

        exam_type = request.query_params.get('exam_type')
        subject = request.query_params.get('subject')
        lga = request.query_params.get('lga')

        if exam_type:
            queryset = queryset.filter(exam_type__iexact=exam_type)

        if subject:
            queryset = queryset.filter(subject__iexact=subject)

        if lga:
            queryset = queryset.filter(
                student__school__lga__name__iexact=lga
            )

        data = (
            queryset
            .values('year')
            .annotate(avg_score=Avg('score'))
            .order_by('year')
        )

        return Response(data)