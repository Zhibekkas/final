from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.core.paginator import Paginator
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
