from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.display_entry, name="display_entry"),
    path("search/", views.search, name="search"),
    path("new_entry/", views.new_entry, name="new_entry"),
]
