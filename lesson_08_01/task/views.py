from django.shortcuts import render
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .models import UserProfile, Course
# Create your views here.


class TeacherTest(UserPassesTestMixin):

    def test_func(self):
        user_type = self.request.user.userprofile.user_profile_type
        if user_type == 't':
            return True
        else:
            return False


class CourseList(TeacherTest, ListView):
    model = Course
    template_name = 'task/course_list.html'
    permission_required = ['task.add_course', 'task.view_course']


class CourseDetail(DetailView):
    model = Course


class CourseCreate(CreateView):
    model = Course
    fields = '__all__'
    success_url = '/'


class CourseUpdate(UpdateView):
    model = Course
    fields = '__all__'
    success_url = '/'


class CourseDelete(DeleteView):
    model = Course
    success_url = '/'
    template_name = 'task/course_form.html'

