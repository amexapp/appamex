from django.urls import path

from work.views import home

app_name = "work"


urlpatterns = [
    path('', home, name="work")
]
