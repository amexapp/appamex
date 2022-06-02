import imp
from typing import ClassVar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from requests import request
from .models import Work
from .models import People
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView


def home(request):
    queryset = request.GET.get("search")
    posts = Work.objects.filter(titulo=1)
    if queryset:
        posts = Work.objects.filter(
            Q(Residencia__name_residence=queryset) |
            Q(Representan__name=queryset)

        ).distinct()

    return render(request, 'pages/Work/index.html', {'posts': posts})
