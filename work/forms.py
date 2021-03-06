from django import forms
from django.forms import fields
from .models import Work


class Work(forms.ModelForm):

    name = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
        'rows': '3',
        'placeholder': 'Say Something...'
    }),
        required=True)

    signature = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        'multiple': True
    }),
        required=False
    )

    class Meta:
        model = People
        fields = ['name']
