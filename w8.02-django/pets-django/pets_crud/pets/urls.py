from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("pets", views.PetListView.as_view(), name="pet_list"),
    path("pets/create/", views.PetCreateView.as_view(), name="pet_create"),
    path("pets/<int:pk>", views.PetDetailView.as_view(), name="pet_detail"),
    path("pets/<int:pk>/update/", views.PetUpdateView.as_view(), name="pet_update"),
    path("pets/<int:pk>/delete/", views.PetDeleteView.as_view(), name="pet_delete"),
]
