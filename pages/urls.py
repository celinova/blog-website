from django.urls import path
from . import views

urlpatterns = [
    path("", views.entries_index, name="index"),
    path("<str:entry_title>/", views.entry_view, name="entry"),
]
