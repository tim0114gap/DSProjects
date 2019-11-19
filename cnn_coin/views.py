from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import ImageModel
from .forms import ImageForm

class PicCreateView(CreateView):
    model = ImageModel
    form_class = ImageForm
    template_name = 'cnn_coin/index.html'
    success_url = reverse_lazy('view')

class ModelListView(ListView):
    model = ImageModel
    template_name = "cnn_coin/view.html"

