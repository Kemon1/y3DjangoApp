from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Module
from django.contrib.auth.models import Group
from registrations.models import Registration
from django.contrib import messages

class ModuleListView(ListView): 
    model = Module
    template_name = 'modules/module_list.html' 
    context_object_name = 'modules'
    paginate_by = 5

class ModuleDetailView(DetailView):
    model = Module
    template_name = 'modules/module_detail.html'

def enroll_in_module(request,module_id):
    module = get_object_or_404(Module, id=module_id)
    student = request.user

    group, created = Group.objects.get_or_create(name=module.name)
    if not student.groups.filter(name=module.name).exists():
        student.groups.add(group)

        Registration.objects.get_or_create(
            student=student.student,
            module=module
        )
        messages.success(request, f"You have succeffully enrolled in {module.name}")
    else:
        messages.info(request, f"You have already enrolled in {module.name}")

    return redirect('module-detail', module_id)