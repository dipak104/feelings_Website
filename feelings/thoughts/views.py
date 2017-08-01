from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .forms import ThoughtForm

# Create your views here.

class CreateThought(CreateView):
    form_class = ThoughtForm
    success_url = reverse_lazy('users:dashboard')



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
