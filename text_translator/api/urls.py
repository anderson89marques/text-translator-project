from django.urls import path

from text_translator.api.views import hello_world

urlpatterns = [
    path("hello/", view=hello_world)
]