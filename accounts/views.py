from django.contrib.auth import authenticate, login,logout, views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from django.contrib.auth.mixins import LoginRequiredMixin

