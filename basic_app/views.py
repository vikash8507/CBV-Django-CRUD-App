from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from basic_app.models import School


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school'
    model = School
