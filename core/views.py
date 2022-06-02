from django import forms
from django.db.models.fields import files
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from people.models import People
from people.forms import PeopleForm

class HomeView( View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user

        posts = People.objects.all()
        form = PeopleForm()



        context={
            'posts':posts,
            'form':form
            
        }
        return render(request, 'pages/index.html', context)