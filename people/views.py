from typing import ClassVar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from .models import People
from .forms import PeopleForm
from django.views.generic.edit import UpdateView, DeleteView


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user = request.user

        posts = People.objects.all()
        form = PeopleForm()

        context = {
            'posts': posts,
            'form': form

        }
        return render(request, 'pages/People/index.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = People.objects.get(pk=pk)
        context = {
            'post': post,

        }
        return render(request, 'pages/people/index.html', context)
