from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from webapp.models import Advertisement
from webapp.forms import AdForm
from django.urls import reverse, reverse_lazy


class IndexView(ListView):
    model = Advertisement
    template_name = 'index_view.html'
    context_object_name = 'ads'
    ordering = ['-created_at']
    paginate_by = 3


class AdView(DetailView):
    template_name = 'view.html'
    model = Advertisement
    context_object_name = 'ad'


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdForm
    template_name = 'ad_create.html'

    def get_success_url(self):
        return reverse('webapp:index')


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advertisement
    template_name = "delete.html"
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'ad'
    permission_required = 'webapp.delete_ad'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdForm
    template_name = "update.html"
    context_object_name = 'ad'
    permission_required = 'webapp.change_ad'

    def get_success_url(self):
        return reverse('webapp:index')

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author
