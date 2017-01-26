from django.shortcuts import render, redirect
from .import models
# Create your views here.
def index(request):
    models.Courses.objects.all()
    courses_list = models.Courses.objects.all()
    models.Courses.objects.filter(id=16).delete()
    # courses_list[0].course_name
    # courses_list[0].description
    # for x in bill:
    #     print x.course_name
    #     print x.description
    # print bill[0].course_name

    context = {
        "views_html_connection_variable": courses_list
    }

    return render(request, "courses/index.html", context)

def delete(request, course_id):
    # print course_id
    models.Courses.objects.filter(id=course_id).delete()
    return redirect("/")


def process(request):
    models.Courses.objects.create(course_name = request.POST['course_name'], description =request.POST['description'])
    # print request.POST['course_name']
    # print request.POST['description']
    return redirect("/")
