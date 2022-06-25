from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView
from django.core.paginator import Paginator
from accounts.forms import UserCreationForm, ProfileChangeForm, UserChangeForm
from accounts.models import Profile
User = get_user_model()


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        ads = self.get_object().ads.all()
        kwargs['ads'] = ads
        paginator = Paginator(
            self.get_object().ads.all(),
            self.paginate_related_by,
            self.paginate_related_orphans,
            )
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['ads'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super(UserDetailView, self).get_context_data(**kwargs)


class RegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = ProfileChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileChangeForm(**form_kwargs)

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user == self.get_object()