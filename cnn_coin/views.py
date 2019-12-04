# from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.template import loader
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from django.conf import settings
from .models import ImageModel
from .forms import ImageForm


# class PicCreateView(CreateView):
#     model = ImageModel
#     form_class = ImageForm
#     template_name = 'cnn_coin/index.html'
#     success_url = reverse_lazy('cnn_coin:view')

# class ModelListView(ListView):
#     model = ImageModel
#     print(model)
#     template_name = "cnn_coin/view.html"


def index(request):
    template=loader.get_template("cnn_coin/index.html")
    context={"form":ImageForm()}
    return HttpResponse(template.render(context,request))

def predict(request):
    if not request.method=="POST":
        return redirect("cnn_coin:index")
    form=ImageForm(request.POST,request.FILES)
    if not form.is_valid():
        raise ValueError("Formが不正です")

    obj = ImageModel.objects.all()
    obj.delete()
    photo=ImageModel(image=form.cleaned_data["image"])
    photo.save()
    predicted, percentage, time, rupee, won= photo.predict()
    obj = ImageModel.objects.order_by('image')[0]
    template=loader.get_template("cnn_coin/index.html")
    context={
        "photo_name":photo.image.name,
        "photo_data":"/media/"+str(obj.image),
        "predicted":predicted,
        "percentage":percentage,
        "rupee":rupee,
        "won":won,
        "time":time,
        "form":ImageForm()
    }
    return HttpResponse(template.render(context,request))