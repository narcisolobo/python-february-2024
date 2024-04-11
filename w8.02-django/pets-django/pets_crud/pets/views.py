from .models import Pet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


# Create your views here.
def index(request):
    """Function based view"""
    return render(request, "index.html")


class PetListView(ListView):
    """The pet list view."""

    model = Pet
    template_name = "pet_list.html"
    context_object_name = "pets"


class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_detail.html"


class PetCreateView(CreateView):
    """This view is for the creation of a pet."""

    model = Pet
    fields = ["name", "type", "age"]
    success_url = reverse_lazy("pet_list")
    template_name = "pet_create.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )
            if field_name in form.errors:
                field.widget.attrs["class"] += " is-invalid"
        return form


class PetUpdateView(UpdateView):
    """This view is for the creation of a pet."""

    model = Pet
    fields = ["name", "type", "age"]
    template_name = "pet_update.html"

    def get_success_url(self) -> str:
        return reverse_lazy("pet_detail", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field_name, field in form.fields.items():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )
            if field_name in form.errors:
                field.widget.attrs["class"] += " is-invalid"
        return form


class PetDeleteView(DeleteView):
    model = Pet
    success_url = reverse_lazy("pet_list")
    template_name = "pet_confirm_delete.html"
