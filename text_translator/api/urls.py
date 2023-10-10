from django.urls import path

from text_translator.api.views import translate, translate_cache

urlpatterns = [
    path("translate/", view=translate),
    path("translate_cache/", view=translate_cache),
]
