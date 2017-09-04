from django.shortcuts import render, redirect
from .models import Course

def start(request):
    return redirect('/')

def index(request):
    course = Course.objects.show_course()
    context = {
        'items':course
    }
    return render(request, "course_list/index.html", context)

def create(request):
    Course.objects.make_course(request.POST['name'], request.POST['description'])
    return redirect('/')

def remove(request, id):
    to_delete = Course.objects.show_course_by_id(id)
    context = {
        'to_delete':to_delete
    }
    return render(request,'course_list/delete.html', context)
def delete(request, id):
    Course.objects.remove(id)
    return redirect('/')


# Create your views here.
