from django.urls import path
from api import views

app_name = "api"
urlpatterns = [
    path("", views.get_api.as_view(), name="get_api"),
]
