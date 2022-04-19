from django.urls import path

from template_names.views import index

urlpatterns = [
    path('', index),
]
