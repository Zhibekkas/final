from django.urls import path
from webapp.views import IndexView, AdCreateView, AdView, AdDeleteView, AdUpdateView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('ad/add/', AdCreateView.as_view(), name="create_ad"),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name="delete_ad"),
    path('ad/<int:pk>/edit/', AdUpdateView.as_view(), name="change_ad"),
    path('photo/<int:pk>/', AdView.as_view(), name="view"),
]