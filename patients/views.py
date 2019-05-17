from django.shortcuts import render
from .models import Patients
from .forms import PatientsForm, PatientsEditForm


def patients_add(request):
    form = PatientsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatientsForm()
    context = {
        "form": form
            }

    return render(request, "patients/add_patients.html", context)


def patients_list_view(request):
    queryset = Patients.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "patients/list_of_patients.html", context)


def patients_edit(request, my_id):
    obj = Patients.objects.get(id=my_id)

    if request.POST:
        form = PatientsEditForm(request.POST, instance=obj)
        form.save()
        form = PatientsEditForm()
    else:
        form = PatientsEditForm(instance=obj)
    context = {
        "object": obj,
        "form": form
    }
    return render(request, "patients/edit_patients.html", context)