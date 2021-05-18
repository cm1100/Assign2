from django.contrib import admin
from django.urls import path,include
from .views import Url_view,Result_View

app_name="freq_counter"

urlpatterns = [
path("",Url_view.as_view(),name="url_view"),
path("../result/<int:pk>",Result_View.as_view(),name="Result_View")
]