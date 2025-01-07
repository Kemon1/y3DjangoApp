from django.shortcuts import render
from users.models import Student

def my_course(request):
    # Get the logged-in student's profile
    student = Student.objects.get(user=request.user)

    # Fetch the courses the student is enrolled in
    courses = student.course.all()

    return render(request, 'courses/course_detail.html', {'courses': courses})

