from django.urls import path

from text_translator.api.views import translate

urlpatterns = [
    path("translate/", view=translate)
]