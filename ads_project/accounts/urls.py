from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import UserDetailView, UserUpdateView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('<int:pk>/', UserDetailView.as_view(), name="detail"),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='change'),
    path('register/', RegisterView.as_view(), name='register'),

]
