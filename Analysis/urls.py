from django.urls import path
from .import views

urlpatterns = [
    #urls for Students
    path('Students/', views.StudentListView.as_view(), name='all_students'),
    path('create_student/', views.StudentListCreateView.as_view(), name='student_create'),
    path('update_student/<int:pk>', views.StudentUpdateview.as_view(), name='update_student'),
    #urls for Exam
    path('Exams/', views.ExamListView.as_view(), name='all_exams'),
    path('create_exam/', views.ExamCreateView.as_view(), name='create_exam'),
    path('update_exam/', views.ExamUpdateView.as_view(), name='update_exam')
 ]