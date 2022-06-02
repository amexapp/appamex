from django.urls import path
from .views import PostDetailView

app_name = "people"


urlpatterns = [
    path('', PostDetailView.as_view(), name="people")
]
