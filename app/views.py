from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from app.models import App
from django.urls import reverse_lazy
# Create your views here.
class HelloClass(TemplateView):
    template_name='index.html'

class AppList(ListView):
    template_name='app/app_list.html'
    model=App

class AppDetail(DetailView):
    template_name='app/app_detail.html'
    model=App

class AppCreate(CreateView):
    template_name='app/app_create.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('app-list')


class AppDelete(DeleteView):
    template_name='app/app_delete.html'
    model=App
    success_url=reverse_lazy('app-list')

class AppUpdate(UpdateView):
    template_name='app/app_update.html'
    model=App
    fields=('title','text','degree')
    success_url=reverse_lazy('app-list')


