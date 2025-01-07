from django.shortcuts import render
from users.models import Student

def my_course(request):
    student = Student.objects.get(user=request.user)
    courses = student.course.all()

    return render(request, 'courses/course_detail.html', {'courses': courses})

