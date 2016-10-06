from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from frontend import models

class IndexView(generic.TemplateView, LoginRequiredMixin ):
    template_name = 'members/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        context['machine_count'] = models.SignOff.objects.filter(member = self.request.user.id )
        context['Machines'] = models.SignOff.objects.filter(member = self.request.user.id)

