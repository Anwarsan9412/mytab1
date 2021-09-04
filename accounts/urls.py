from django.urls import path 
# from .views import logout_view
from django.contrib.auth import views as auth_views

from .decorators import unauthenticated_user

urlpatterns = [
    # path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    
    path('accounts/login/', unauthenticated_user(auth_views.LoginView.as_view(template_name='registration/login.html')), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]
