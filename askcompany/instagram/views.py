from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, CreateView, UpdateView, \
    DeleteView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get( 'q' , '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/template/instagram/post_list.html
    return render(request , 'instagram/post_list.html', {

        'post_list':qs,
    })

