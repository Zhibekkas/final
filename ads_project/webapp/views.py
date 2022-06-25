from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Advertisement


class IndexView(ListView):
    model = Advertisement
    template_name = 'index_view.html'
    context_object_name = 'ads'
    ordering = ['-created_at']
