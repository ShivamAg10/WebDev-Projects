from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("editList/<int:id>", views.editList, name="editList"),
    path("deleteList/<int:id>", views.deleteList, name="deleteList"),
]
