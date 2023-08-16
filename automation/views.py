from django.db import transaction
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.core import serializers

from django.core.serializers import serialize
from django.db.models.query import QuerySet

from .models import *
from .CONSTANTS import *
import jdatetime
import json
from django.db.models import Q

from itertools import groupby
from operator import attrgetter
from functools import reduce
from operator import or_
from django.db.models import F
from operator import itemgetter

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re

from django.db.models import Case, When, Value, IntegerField

def temp(request):
    # template = get_template('pdf_A4_dailyReport_inDetails_humanresources_portrait.html')
    #
    # context = {'title': 'Sample PDF Report', 'content': 'This is a sample PDF report content.'}
    # html = template.render(context)
    #
    # pdf = HTML(string=html).write_pdf()
    #
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="report.pdf"'

    # buffer = BytesIO()
    # p = canvas.Canvas(buffer)
    #
    # # Draw the text content onto the PDF
    # p.drawString(100, 750, "PDF Report Example")
    # p.drawString(100, 700, context['title'])
    # p.drawString(100, 650, context['content'])
    #
    # p.showPage()
    # p.save()

    # pdf = buffer.getvalue()
    # buffer.close()
    # response.write(pdf)

    # return response



    return render(request, "pdf_A4_dailyReport_inDetails_humanresources_portrait.html",)

def temp2(request):
    return render(request, "pdf_A4_dailyReport_inDetails_machines_materials_portrait.html",)

def temp3(request):
    return render(request, "pdf_A4_dailyReport_inDetails_materials_portrait.html",)

def temp4(request):
    return render(request, "pdf_A4_dailyReport_inDetails_tasks_landscape.html",)

def temp5(request):
    return render(request, "pdf_A4_dailyReport_inDetails_issues_portrait.html",)


def home(request):
    if request.user.is_authenticated:
        my_user = MyUser.objects.get(user=request.user)
        context = {
            "my_user": my_user
        }
    else:
        context = {

        }
    return render(request, "home.html", context=context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password, )
        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to a specific page after login

    return redirect('/home/')


def logout_view(request):
    logout(request)
    return redirect('/home/')  # Redirect to the login page after logout


@login_required
def add_base_data_template(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    professions = Profession.objects.filter(project=project)
    positions = Position.objects.filter(project=project)
    hardwares = Hardware.objects.filter(project=project)
    machineFamilies = MachineFamily.objects.filter(project=project)
    machines = Machine.objects.filter(project=project)
    materials = Material.objects.filter(project=project)
    contractors = Contractor.objects.filter(project=project)
    equipes = Equipe.objects.filter(project=project)
    zones = Zone.objects.filter(project=project)
    tasks = Task.objects.filter(project=project)
    parentTasks = ParentTask.objects.filter(project=project)
    units = Unit.objects.filter(project=project).order_by('parent', 'name')
    projectFields = ProjectField.objects.filter(project=project)

    materialproviders = MaterialProvider.objects.filter(project=project)
    machineproviders = MachineProvider.objects.filter(project=project)

    issues = Issue.objects.filter(project=project)

    operations = Operation.objects.filter(project=project)
    suboperations = SubOperation.objects.filter(project=project)

    if not professions.exists():
        professions = []
    if not positions.exists():
        positions = []
    if not hardwares.exists():
        hardwares = []
    if not machineFamilies.exists():
        machineFamilies = []
    if not machines.exists():
        machines = []
    if not materials.exists():
        materials = []
    if not contractors.exists():
        contractors = []
    if not equipes.exists():
        equipes = []
    if not zones.exists():
        zones = []
    if not tasks.exists():
        tasks = []
    if not parentTasks.exists():
        tasks = []
    if not units.exists():
        units = []
    if not materialproviders.exists():
        materialproviders = []
    if not machineproviders.exists():
        machineproviders = []
    if not issues.exists():
        issues = []
    if not operations.exists():
        operations = []
    if not suboperations.exists():
        suboperations = []
    if not projectFields.exists():
        projectFields = []

    context = {
        "project": project,
        "positions": positions,
        "professions": professions,
        "hardwares": hardwares,
        "machineFamilys": machineFamilies,
        "machines": machines,
        "materials": materials,
        "contractors": contractors,
        "equipes": equipes,
        "zones": zones,
        "tasks": tasks,
        "parentTasks": parentTasks,
        "units": units,
        "materialproviders": materialproviders,
        "machineproviders": machineproviders,
        "issues": issues,
        "operations": operations,
        "suboperations": suboperations,
        "projectFields": projectFields,

        "machine_types": MACHINE_TYPES,
    }

    return render(request, "modify-base-data.html", context=context)


@login_required
def edit_base_data(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        new_data = request.POST
        model = EDIT_BASE_DATA[new_data["model"]]
        if new_data["model"] in ONLY_NAME_MODELS:
            instance = new_data["instance"]
            object = get_object_or_404(model, name=instance, project=project)
            object.name = new_data['name']
            object.save()

            return HttpResponse(True)

        elif new_data["model"] == "equipe":
            instance = new_data["instance"]
            profession = new_data.get("profession")
            contractor = new_data.get("contractor")
            object = get_object_or_404(
                model,
                name=instance,
                project=project,
            )
            if profession:
                object.profession = Profession.objects.get(name=profession, project=project)
            if contractor:
                object.contractor = Contractor.objects.get(name=contractor, project=project)

            object.set_name()

            object.save()

            return HttpResponse(True)

        elif new_data["model"] == "operation":
            instance = new_data.get("instance")
            name = new_data.get("name")
            amount = new_data.get("amount")
            unit = new_data.get("unit")
            object = get_object_or_404(
                model,
                name=instance,
                project=project,
            )
            if name and name.strip() != object.name:
                object.name = name.strip()

            if amount and amount.strip() != str(object.amount):
                object.amount = amount.strip()

                for zone in object.zones.all():
                    for task in zone.tasks.all():
                        task.totalVolume = (float(task.parent.totalVolume) / float(object.amount)) * float(task.suboperation.amount)
                        task.save()

                object.update_percentage()
                object.update_assignedAmount()

                for item in TaskReport.objects.filter(operation=object, project=project):
                    item.update_due_to_base_data_edits()

            if unit and unit.strip() != object.unit:
                for zone in object.zones.all():
                    zone.unit = Unit.objects.get(name=unit, project=project)
                    zone.save()

                    for parentTask in zone.parentTasks.all():
                        parentTask.unit = Unit.objects.get(name=unit, project=project)
                        parentTask.save()
                    for task in zone.tasks.all():
                        if task.unit.name == object.unit.name:
                            task.unit = Unit.objects.get(name=unit, project=project)
                            task.save()

                for suboperation in object.suboperations.all():
                    if suboperation.unit.name == object.unit.name:
                        suboperation.unit = Unit.objects.get(name=unit, project=project)
                        suboperation.save()

                object.unit = Unit.objects.get(name=unit, project=project)

            object.save()

            return HttpResponse(True)

        elif new_data["model"] == "zoneoperation":
            instance = new_data.get("instance")
            zone = new_data.get("zone")
            amount = new_data.get("amount")

            old_zone, operation = instance.split("-")
            old_zone, operation = Zone.objects.get(name=old_zone, project=project), Operation.objects.get(name=operation, project=project)
            object = get_object_or_404(
                model,
                operation=operation,
                zone=old_zone,
                project=project,
            )

            if zone:
                object.zone = Zone.objects.get(name=zone, project=project)
            if amount:
                object.amount = amount
            object.save()

            operation.update_assignedAmount()

            # object.update_assignedAmount()
            object.update_freeAmount()
            object.update_donePercentage()

            return HttpResponse(True)

        elif new_data["model"] == "suboperation":
            instance = new_data.get("instance")
            name = new_data.get("name")
            weight = new_data.get("weight")
            amount = new_data.get("amount")
            unit = new_data.get("unit")

            ref_sub, operation = instance.split("-")
            operation = Operation.objects.get(name=operation, project=project)
            object = get_object_or_404(
                model,
                parent=operation,
                name=ref_sub,
                project=project,
            )

            if name and name != object.name:
                object.name = name
            if weight and float(weight) != float(object.weight):
                object.weight = weight
                object.save()
                for zoneoperation in object.parent.zones.all():
                    for parentTask in zoneoperation.parentTasks.all():
                        parentTask.update_doneVolume()
                    zoneoperation.update_doneAmount()
                object.parent.update_doneAmount()

            operation.refresh_from_db()
            if amount and float(amount) != float(object.amount):
                object.amount = amount
                for task in Task.objects.filter(suboperation=object, project=project):
                    task.totalVolume = (float(task.parent.totalVolume)/float(operation.amount))*float(object.amount)
                    task.save()
                    task.update_percentage()
                object.save()

                for item in TaskReport.objects.filter(operation=object.parent, project=project):
                    item.update_due_to_base_data_edits()

            if unit and unit != object.unit.name:
                for task in Task.objects.filter(suboperation=object, project=project):
                    if task.unit.name == object.unit.name:
                        task.unit = Unit.objects.get(name=unit, project=project)
                        task.save()

                object.unit = Unit.objects.get(name=unit, project=project)

            object.save()

            operation.update_assignedWeight()

            return HttpResponse(True)

        elif new_data["model"] == "machineFamily":
            instance = new_data.get("instance")
            name = new_data.get("name")
            hardware = new_data.get("hardware")

            ref_name, ref_hardware = instance.split("-")

            ref_hardware = Hardware.objects.get(name=ref_hardware, project=project)

            object = get_object_or_404(
                model,
                hardware=ref_hardware,
                name=ref_name,
                project=project,
            )

            if name and name != object.name:
                object.name = name
            if hardware and hardware != object.hardware:
                hardware = Hardware.objects.get(name=hardware, project=project)
                object.hardware = hardware

            object.save()

            return HttpResponse(True)

        elif new_data["model"] == "machine":
            instance = new_data.get("instance")
            name = new_data.get("name")

            if new_data.get("family"):
                family, hardware = new_data.get("family").split("-")
                hardware = Hardware.objects.get(id=hardware, project=project)
                family = MachineFamily.objects.get(name=family,
                                                   hardware=hardware,
                                                   project=project)
            else:
                family = None


            ref_hardware = new_data.get("hardware")

            ref_name, ref_family = instance.split("-")

            ref_hardware = Hardware.objects.get(
                project=project,
                name=ref_hardware,
            )

            ref_family = MachineFamily.objects.get(name=ref_family,
                                                   hardware=ref_hardware,
                                                   project=project)

            object = get_object_or_404(
                model,
                type=ref_family,
                hardware=ref_hardware,
                name=ref_name,
                project=project,
            )

            if name and name != object.name:
                object.name = name

            if family and family != object.type:
                object.type = family
                object.hardware = hardware

            object.save()

            return HttpResponse(True)


@login_required
def create_report_template(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if DailyReport.objects.filter(project=project).count() == 0:
        # positions = Position.objects.all()
        # professions = Profession.objects.all()
        # machines = Machine.objects.all()
        # materials = Material.objects.all()
        # equipes = Equipe.objects.all()
        # units = Unit.objects.all()
        # materialproviders = MaterialProvider.objects.all()
        # machineproviders = MachineProvider.objects.all()
        # tasks = Task.objects.all()
        issueReports = IssueReport.objects.filter(project=project, solved=False)

        # context = {
        #     "positions": positions,
        #     "professions": professions,
        #     "machines": machines,
        #     "materials": materials,
        #     "equipes": equipes,
        #     "units": units,
        #     "materialproviders": materialproviders,
        #     "machineproviders": machineproviders,
        #     "tasks": tasks,
        #     "machine_types": MACHINE_TYPES,
        # }

        context = {
            "project": project,
            "machine_types": MACHINE_TYPES,
            "issueReports": issueReports,
        }

    else:
        report = DailyReport.objects.filter(project=project).last()
        positions = PositionCount.objects.filter(dailyReport=report, project=project)
        professions = ProfessionCount.objects.filter(dailyReport=report, project=project)
        machines = MachineCount.objects.filter(dailyReport=report, project=project)
        materials = MaterialCount.objects.filter(dailyReport=report, project=project)
        equipes = EquipeCount.objects.filter(dailyReport=report, project=project)
        units = Unit.objects.filter(project=project)
        materialproviders = MaterialProvider.objects.filter(project=project)
        machineproviders = MachineProvider.objects.filter(project=project)
        tasks = TaskReport.objects.filter(dailyReport=report, project=project)
        issueReports = IssueReport.objects.filter(project=project, solved=False)

        other = {
            "weekday": report.get_weekday_display(),
            "date": report.date.strftime('%Y/%m/%d'),
        }

        context = {
            "project": project,
            "report": report,
            "positions": positions,
            "professions": professions,
            "machines": machines,
            "materials": materials,
            "equipes": equipes,
            "units": units,
            "materialproviders": materialproviders,
            "machineproviders": machineproviders,
            "issueReports": issueReports,
            "tasks": tasks,
            "machine_types": MACHINE_TYPES,
            "other": other,
        }

    return render(request, "daily-report.html", context=context)


@login_required
def add_position_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        position = request.POST.get("position")

        new_position = Position.objects.create(name=position, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_unit_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        unit = request.POST.get("unit")
        parent = request.POST.get("parent-unit")
        coef = request.POST.get("parent-coef")

        if parent:
            parent = Unit.objects.get(name=parent, project=project)

        new_unit = Unit.objects.create(
            project=project,
            name=unit,
            parent=parent if parent else None,
            coef=coef if coef else 1.0,
        )

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_materialprovider_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        materialprovider = request.POST.get("materialprovider")

        new_materialprovider = MaterialProvider.objects.create(name=materialprovider, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_machineprovider_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machineprovider = request.POST.get("machineprovider")

        new_machineprovider = MachineProvider.objects.create(name=machineprovider, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_issue_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        issue = request.POST.get("issue")

        new_issue = Issue.objects.create(name=issue, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_issueReport_to_project(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        issue = request.POST.get("issue")
        projectField = request.POST.get("projectField")
        zone = request.POST.get("zone")
        description = request.POST.get("description")

        issue = Issue.objects.get(
            project=project,
            name=issue
        )
        projectField = ProjectField.objects.get(
            project=project,
            name=projectField,
        )
        zone = Zone.objects.get(
            project=project,
            name=zone,
        )
        issueReport, new = IssueReport.objects.get_or_create(project=project,
                                                             issue=issue,
                                                             projectField=projectField,
                                                             zone=zone,
                                                             description=description,
                                                             defaults={})
        if new:
            return HttpResponse(True)
        else:
            return HttpResponse("مشکل وارد شده قبلا در پروژه وجود دارد", status=500)

    elif request.method == "GET":
        pass


@login_required
def add_projectField_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        projectField = request.POST.get("projectField")

        new_projectField = ProjectField.objects.create(name=projectField, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_hardware_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        hardware = request.POST.get("hardware")

        new_hardware = Hardware.objects.create(name=hardware, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_machineFamily_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machineFamily = request.POST.get("machineFamily")
        hardware = request.POST.get("hardware-name")
        hardware = Hardware.objects.get(name=hardware, project=project)
        new_machineFamily = MachineFamily.objects.create(name=machineFamily, hardware=hardware, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_machine_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machine = request.POST.get("machine-name")
        type, hardware = request.POST.get("machineFamily-name").split("-")

        new_machine = Machine.objects.create(name=machine,
                                             type=MachineFamily.objects.get(
                                                 project=project,
                                                 name=type,
                                                 hardware=Hardware.objects.get(
                                                     name=hardware,
                                                     project=project,
                                                 )
                                             ),
                                             project=project)
        new_machine.hardware = Hardware.objects.get(
                                                     name=hardware,
                                                     project=project,
                                                 )
        new_machine.save()
        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_material_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        material = request.POST.get("material")
        # type = request.POST.get("machineType")

        new_material = Material.objects.create(name=material, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_profession_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        profession = request.POST.get("profession")

        new_profession = Profession.objects.create(name=profession, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_contractor_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        contractor = request.POST.get("contractor")

        new_contractor = Contractor.objects.create(name=contractor, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_zone_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        zone = request.POST.get("zone")

        new_zone = Zone.objects.create(name=zone, project=project)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def add_task_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')

        operation = request.POST.get("operation")
        # suboperation = request.POST.get("suboperation")
        zoneName = request.POST.get("zoneoperation")
        equipeName = request.POST.get("equipe")
        taskVol = float(request.POST.get("task-volume"))
        unitName = request.POST.get("unit")

        operation = Operation.objects.get(name=operation, project=project)
        zoneoperation = ZoneOperation.objects.get(
            operation=operation,
            zone=Zone.objects.get(name=zoneName, project=project),
            project=project
        )

        new_parent_task, new = ParentTask.objects.get_or_create(
            operation=zoneoperation,
            equipe=Equipe.objects.get(name=equipeName, project=project),
            zone=Zone.objects.get(name=zoneName, project=project),
            project=project,

            defaults={
                'totalVolume': taskVol,
                'unit': Unit.objects.get(name=unitName, project=project),
            }
        )

        if not new:
            return JsonResponse(False, safe=False)

        new_parent_task.set_unique()
        new_parent_task.update_percentage()

        zoneoperation.parentTasks.add(new_parent_task)
        zoneoperation.update_assignedAmount()

        for suboperation in operation.suboperations.all():
            taskVol_for_subopr = (taskVol/zoneoperation.operation.amount) * suboperation.amount
            new_task, new = Task.objects.get_or_create(
                project=project,
                parent=new_parent_task,
                operation=zoneoperation,
                suboperation=SubOperation.objects.get(
                    project=project,
                    name=suboperation.name,
                    parent=operation,
                ),
                equipe=Equipe.objects.get(name=equipeName, project=project),
                zone=Zone.objects.get(name=zoneName, project=project),

                defaults={
                    'totalVolume': taskVol_for_subopr,
                    'unit': suboperation.unit,
                }
            )

            if not new:
                return JsonResponse(False, safe=False)

            new_task.set_unique()
            new_task.update_percentage()

            new_parent_task.subtasks.add(new_task)

            zoneoperation.tasks.add(new_task)
            zoneoperation.update_assignedAmount()

        return JsonResponse(new_parent_task.id, safe=False)
            # return redirect(redirect_url)

        # except:
        #     return HttpResponse(False)

    elif request.method == "GET":
        pass

        return HttpResponse("Problem")


@login_required
def add_equipe_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        # redirect_url = request.META.get('HTTP_REFERER', '/')
        prof = request.POST.get("profession")
        cont = request.POST.get("contractor")

        prof = Profession.objects.get(name=prof, project=project)
        cont = Contractor.objects.get(name=cont, project=project)

        # TODO : Make line below get_or_create
        obj , new = Equipe.objects.get_or_create(
            project=project,
            profession=prof,
            contractor=cont,
            defaults={
                "profession": prof,
                "contractor": cont,
            }
        )
        if new:
            obj.set_name()
            #obj.save()
            return JsonResponse(True, safe=False)
        else:
            return HttpResponse(False, status=500)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


@login_required
def shortcut_add(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        which = request.POST.get("which")
        value = request.POST.get("value")
        type = request.POST.get("type")

        if which == "position":
            new_obj = Position.objects.create(name=value, project=project)
        elif which == "profession":
            new_obj = Profession.objects.create(name=value, project=project)
        elif which == "machine":
            new_obj = Machine.objects.create(name=value, type=type, project=project)
        elif which == "material":
            new_obj = Material.objects.create(name=value, project=project)
        elif which == "contractor":
            new_obj = Contractor.objects.create(name=value, project=project)
        elif which == "zone":
            new_obj = Zone.objects.create(name=value, project=project)
        elif which == "unit":
            new_obj = Unit.objects.create(name=value, project=project)
        elif which == "materialprovider":
            new_obj = MaterialProvider.objects.create(name=value, project=project)
        elif which == "machineprovider":
            new_obj = MachineProvider.objects.create(name=value, project=project)

        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(False)


@login_required
def del_position_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("position")
        obj = Position.objects.get(name=name, project=project)
        objCount = PositionCount.objects.filter(position=obj.id, project=project)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_profession_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("profession")
        obj = Profession.objects.get(name=name, project=project)
        objCount = PositionCount.objects.filter(position=obj.id, project=project)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_hardware_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("hardware")
        obj = Hardware.objects.get(name=name, project=project)
        # objCount = MachineCount.objects.filter(machine=obj.id, project=project)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_machineFamily_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name, hardware = request.POST.get("machineFamily").split("-")
        obj = MachineFamily.objects.get(name=name,
                                        hardware=Hardware.objects.get(name=hardware, project=project),
                                        project=project)
        obj.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_machine_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name, family, hardware = request.POST.get("machine").split("-")
        obj = Machine.objects.get(name=name,
                                  type=MachineFamily.objects.get(
                                      project=project,
                                      name=family,
                                      hardware=Hardware.objects.get(
                                          project=project,
                                          name=hardware,
                                      )
                                  ),
                                  project=project)
        objCount = MachineCount.objects.filter(machine=obj.id, project=project)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_material_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("material")
        obj = Material.objects.get(name=name, project=project)
        objCount = MaterialCount.objects.filter(material=obj.id, project=project)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_contractor_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("contractor")
        obj = Contractor.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_zone_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("zone")
        obj = Zone.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_unit_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("unit")
        obj = Unit.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_operation_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("operation")

        obj = Operation.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_suboperation_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        suboperation = request.POST.get("suboperation")
        operation = request.POST.get("operation")
        obj = SubOperation.objects.get(name=suboperation, parent=operation, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        Operation.objects.get(id=operation, project=project).update_assignedWeight()
        # objCount.delete()
        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_zoneoperation_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        zone = request.POST.get("zoneoperation")
        zone = Zone.objects.get(name=zone, project=project)

        operation = request.POST.get("operation")

        obj = ZoneOperation.objects.get(zone=zone, operation=operation, project=project)
        obj.delete()

        Operation.objects.get(id=operation, project=project).update_assignedAmount()

        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def add_suboperation_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        operation_id = request.POST.get("operation-id")
        name = request.POST.get("name")
        unit_name = request.POST.get("unit").strip()
        amount = request.POST.get("amount")
        weight = request.POST.get("weight")

        operation = Operation.objects.get(id=operation_id, project=project)
        unit = Unit.objects.get(name=unit_name, project=project)

        new_obj = SubOperation.objects.create(
            project=project,
            name=name,
            unit=unit,
            parent=operation,
            weight=weight,
            amount=amount,
        )

        operation.suboperations.add(new_obj)

        operation.update_assignedWeight()


        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def add_operation_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("operation")
        unit_name = request.POST.get("unit-name").strip()
        amount = request.POST.get("amount")

        operation = Operation.objects.create(
            project=project,
            name=name,
            unit=Unit.objects.get(name=unit_name, project=project),
            amount=amount,
        )
        operation.update_assignedWeight()
        operation.update_assignedAmount()

        return HttpResponse(operation.id)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def add_zoneoperation_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        operation_id = request.POST.get("operation-id")
        zone = request.POST.get("zone").strip()
        amount = request.POST.get("amount")

        operation = Operation.objects.get(id=operation_id, project=project)
        if float(amount) > float(operation.freeAmount):
            return HttpResponse(f"حداکثر مقدار وارده {operation.freeAmount} می باشد", status=500)

        zone_operation = ZoneOperation.objects.create(
            project=project,
            operation=operation,
            zone=Zone.objects.get(name=zone, project=project),
            unit=operation.unit,
            amount=amount,
        )
        zone_operation.update_freeAmount()

        operation.zones.add(zone_operation)
        operation.update_assignedAmount()

        return HttpResponse(zone_operation.id)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_materialprovider_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("materialprovider")
        obj = MaterialProvider.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_machineprovider_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("machineprovider")
        obj = MachineProvider.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_issue_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("issue")
        obj = Issue.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_projectField_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("projectField")
        obj = ProjectField.objects.get(name=name, project=project)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_equipe_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        prof = request.POST.get("profession")
        cont = request.POST.get("contractor")

        obj = Equipe.objects.filter(
            project=project,
            profession=Profession.objects.get(name=prof, project=project),
            contractor=Contractor.objects.get(name=cont, project=project),
        )
        obj.delete()

        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def del_task_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        taskOperation = request.POST.get("taskOperation")
        # taskSubOperation = request.POST.get("taskSubOperation")
        equipeName = request.POST.get("equipeName")
        # taskVol = request.POST.get("taskVol")
        zoneName = request.POST.get("zoneName")
        # unitName = request.POST.get("unitName")
        operation = Operation.objects.get(name=taskOperation, project=project)
        zoneoperation = ZoneOperation.objects.get(
            project=project,
            operation=operation,
            zone=Zone.objects.get(name=zoneName, project=project),
        )

        obj = ParentTask.objects.filter(
            project=project,
            operation=zoneoperation.id,
            # suboperation=SubOperation.objects.get(
            #     name=taskSubOperation,
            #     parent=Operation.objects.get(name=taskOperation),
            # ),
            equipe=Equipe.objects.get(name=equipeName, project=project),
            zone=Zone.objects.get(name=zoneName, project=project),
        )
        obj.delete()

        zoneoperation.update_assignedAmount()
        zoneoperation.update_doneAmount()

        operation.update_doneAmount()

        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


@login_required
def save_daily_report_to_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        data = dict(request.POST)

        positions = {}
        professions = {}
        machines = {}
        materials = {}
        equipes = {}
        contractors = {}
        tasks = {}
        issues = {}

        for key, value in data.items():
            if "position" in key:
                positions[key.split("_")[1]] = int(value[0])
            elif "profession" in key:
                prof = key.split("_")[2].split("-")[0]
                if key.split("_")[2].split("-")[0] in professions.keys():
                    if "Semi" in key.split("_")[3]:
                        professions[prof][1] += int(value[0])
                    elif "Non" in key.split("_")[3]:
                        professions[prof][2] += int(value[0])
                    else:
                        professions[prof][0] += int(value[0])

                else:
                    professions[prof] = [0, 0, 0]
                    if "Semi" in key.split("_")[3]:
                        professions[prof][1] += int(value[0])
                    elif "Non" in key.split("_")[3]:
                        professions[prof][2] += int(value[0])
                    else:
                        professions[prof][0] += int(value[0])

                cont = key.split("_")[2].split("-")[1]
                if key.split("_")[2].split("-")[1] in contractors.keys():
                    if "Semi" in key.split("_")[3]:
                        contractors[cont][1] += int(value[0])
                    elif "Non" in key.split("_")[3]:
                        contractors[cont][2] += int(value[0])
                    else:
                        contractors[cont][0] += int(value[0])

                else:
                    contractors[cont] = [0, 0, 0]
                    if "Semi" in key.split("_")[3]:
                        contractors[cont][1] += int(value[0])
                    elif "Non" in key.split("_")[3]:
                        contractors[cont][2] += int(value[0])
                    else:
                        contractors[cont][0] += int(value[0])

                if key.split("_")[2] in equipes.keys():
                    equipes[key.split("_")[2]].append(int(value[0]))
                else:
                    equipes[key.split("_")[2]] = []
                    equipes[key.split("_")[2]].append(int(value[0]))

            elif "issueReport" in key:
                issues[key.split("_")[1]] = value[0]

            elif "machine" in key:
                if f"{key.split('_')[1]}_{key.split('_')[2]}" in machines.keys():
                    if "provider" in key:
                        machines[f"{key.split('_')[1]}_{key.split('_')[2]}"].append(value[0])
                    else:
                        machines[f"{key.split('_')[1]}_{key.split('_')[2]}"].append(int(value[0]))
                else:
                    machines[f"{key.split('_')[1]}_{key.split('_')[2]}"] = []
                    machines[f"{key.split('_')[1]}_{key.split('_')[2]}"].append(int(value[0]))

            elif "material" in key:
                if "count" in key:
                    materials[f"{key.split('_')[1]}_{key.split('_')[2]}"] = [float(value[0]), None, None]
                elif "unit" in key:
                    materials[f"{key.split('_')[1]}_{key.split('_')[2]}"][1] = value[0]
                elif "provider" in key:
                    materials[f"{key.split('_')[1]}_{key.split('_')[2]}"][2] = value[0]
            elif "task" in key:
                tasks[key.split("_")[1]] = float(value[0])

        # print(positions)
        # print(professions)
        # print(machines)
        # print(materials)
        # print(equipes)
        # print(contractors)
        # print(tasks)

        # print(data)
        # print(data['date'])
        # print(materials.items())
        # return HttpResponse(1)

        try:
            with transaction.atomic():

                report = DailyReport.objects.create(
                    project=project,
                    project_name=data['project_name'][0],
                    employer=data["employer"][0],
                    employee=data["employee"][0],
                    contract_number=data["contract_no"][0],
                    date=jdatetime.datetime.strptime(data['date'][0], format="%Y/%m/%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S"),
                    temperature_min=data["minTemp"][0],
                    temperature_max=data["maxTemp"][0],
                    weather=data["weather_status"][0],
                    dust_value=data["dust_value"][0],
                    consultor_name=data["consultor_name"][0],
                )
                report.set_weekday()

                for position, count in positions.items():
                    if count > 0:
                        pos = Position.objects.get(name=position, project=project)
                        obj = PositionCount.objects.create(
                            project=project,
                            position=pos,
                            dailyReport=report,
                            count=count,
                        )
                        report.positions.add(obj.position)
                    else:
                        continue

                for profession, count in professions.items():
                    if sum(count) > 0:
                        prof = Profession.objects.get(name=profession, project=project)
                        obj = ProfessionCount.objects.create(
                            project=project,
                            profession=prof,
                            dailyReport=report,
                            countExpert=count[0],
                            countSemiExpert=count[1],
                            countNonExpert=count[2],
                        )
                        obj.cal_countTotal()

                        report.professions.add(obj.profession)

                    else:
                        continue

                for machine, count in machines.items():
                    machine = machine.split("_")[0]
                    if count[0] >= 0 or count[1] > 0:
                        machine = machine.strip()
                        machine = re.sub(r'[\[\]]', '', machine)
                        machine, family, hardware = machine.split("-")

                        hardware = Hardware.objects.get(
                            project=project,
                            name=hardware
                        )
                        family = MachineFamily.objects.get(
                            project=project,
                            name=family,
                            hardware=hardware,
                        )
                        mach = Machine.objects.get(name=machine,
                                                   type=family,
                                                   hardware=hardware,
                                                   project=project)

                        provider = MachineProvider.objects.get(name=count[3], project=project)
                        if provider.name == "شرکتی":
                            obj = MachineCount.objects.create(
                                project=project,
                                machine=mach,
                                dailyReport=report,
                                activeCount=count[1],
                                inactiveCount=count[2],
                                workHours=count[0],
                                provider=provider,
                                totalCount=sum(count[1:3]),
                                onRent=False,
                                hardware=hardware,
                                type=family,
                            )
                        else:
                            obj = MachineCount.objects.create(
                                project=project,
                                machine=mach,
                                dailyReport=report,
                                activeCount=1 if count[0] > 0 else 0,
                                inactiveCount=0 if count[0] > 0 else 1,
                                workHours=count[0],
                                provider=provider,
                                totalCount=1,
                                onRent=True,
                                hardware=hardware,
                                type=family,

                            )

                        report.machines.add(obj.machine)

                    else:
                        continue

                for material, amount in materials.items():
                    material = material.split("_")[0]
                    if amount[0] > 0:
                        material = material.strip()

                        mat = Material.objects.get(name=material, project=project)
                        unit = Unit.objects.get(name=amount[1], project=project)
                        materialprovider = MaterialProvider.objects.get(name=amount[2], project=project)
                        obj = MaterialCount.objects.create(
                            project=project,
                            material=mat,
                            dailyReport=report,
                            amount=amount[0],
                            unit=unit,
                            provider=materialprovider,
                        )
                        report.materials.add(obj.material)
                    else:
                        continue

                for contractor, count in contractors.items():
                    if sum(count) > 0:
                        cont = Contractor.objects.get(name=contractor, project=project)
                        obj = ContractorCount.objects.create(
                            project=project,
                            contractor=cont,
                            dailyReport=report,
                            countExpert=count[0],
                            countSemiExpert=count[1],
                            countNonExpert=count[2],
                        )
                        obj.cal_countTotal()

                        report.contractors.add(obj.contractor)
                    else:
                        continue

                for equipe, count in equipes.items():
                    if sum(count) > 0:
                        prof, cont = equipe.split("-")
                        equ = Equipe.objects.get(
                            project=project,
                            profession=Profession.objects.get(name=prof, project=project),
                            contractor=Contractor.objects.get(name=cont, project=project),
                        )
                        obj = EquipeCount.objects.create(
                            project=project,
                            equipe=equ,
                            dailyReport=report,
                            countExpert=count[0],
                            countSemiExpert=count[1],
                            countNonExpert=count[2],
                        )
                        obj.cal_countTotal()

                        report.equipes.add(obj.equipe)
                    else:
                        continue

                for task, amount in tasks.items():
                    if amount > 0:
                        tsk = Task.objects.get(unique_str=task, project=project)

                        if not tsk.started:
                            tsk.start(date=report.date)

                        parent = TaskReport.objects.filter(task=tsk, project=project).last()
                        tsk_rep = TaskReport.objects.create(
                            project=project,
                            task=tsk,
                            operation=tsk.operation.operation,
                            parent=parent,
                            dailyReport=report,
                            todayVolume=amount,
                            reportDate=report.date,
                            parentTask=tsk.parent,
                        )

                        tsk_rep.update_percentage(False, date=report.date)
                        tsk_rep.update_filtering_fields()
                        report.tasks.add(tsk_rep.task)

                report.cal_countPeople()
                report.cal_countMachines()

                for issue, status in issues.items():
                    issue_name, projectField, zone, description = issue.split(" - ")

                    issue = Issue.objects.get(
                        project=project,
                        name=issue_name
                    )
                    projectField = ProjectField.objects.get(
                        project=project,
                        name=projectField,
                    )
                    zone = Zone.objects.get(
                        project=project,
                        name=zone,
                    )

                    issueReport = IssueReport.objects.get(project=project,
                                                          issue=issue,
                                                          projectField=projectField,
                                                          zone=zone,
                                                          description=description)

                    if not issueReport.started:
                        issueReport.start(report.date)

                    if status == "solved":
                        issueReport.complete(report.date)

                    obj = IssueCount.objects.create(
                        project=project,
                        dailyReport=report,
                        issue=issueReport,
                    )
                    report.issues.add(obj.issue)

                    issueReport.issueCounts.add(obj)

        # return redirect(to="/home/daily-reports")
            return HttpResponse(True)

        except:
            return HttpResponse("Something went wrong", status=500)
    else:
        return -1


@login_required
def del_daily_report_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]


    if request.method == "POST":

        rep = DailyReport.objects.get(id=request.POST["id"], project=project)

        if rep.deletable:
            try:
                with transaction.atomic():
                    for item in rep.taskreport_set.all():
                        item.update_percentage(True, date=rep.date)

                    for issue in rep.issues.all():
                        if issue.solved:
                            issue.solved = False
                            issue.save()

                        if len(issue.issueCounts.all()) > 1:
                            continue
                        else:
                            if issue.started:
                                issue.started = False
                                issue.save()

                    rep.delete()

                return redirect(to="/home/daily-reports")

            except:
                return HttpResponse("Something went wrong", status=500)

        else:
            return HttpResponse(PermissionDenied, status=500)
    else:
            return -1


@login_required
def edit_daily_report_in_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        if request.POST.get("template"):
            report = DailyReport.objects.get(id=request.POST["id"], project=project)

            if report.editable:

                positions = PositionCount.objects.filter(dailyReport=report, project=project)
                professions = ProfessionCount.objects.filter(dailyReport=report, project=project)
                machines = MachineCount.objects.filter(dailyReport=report, project=project)
                materials = MaterialCount.objects.filter(dailyReport=report, project=project)
                equipes = EquipeCount.objects.filter(dailyReport=report, project=project)
                units = Unit.objects.filter(project=project)
                materialproviders = MaterialProvider.objects.filter(project=project)
                machineproviders = MachineProvider.objects.filter(project=project)
                tasks = TaskReport.objects.filter(dailyReport=report, project=project)

                other = {
                    "weekday": report.get_weekday_display(),
                    "date": report.date.strftime('%Y/%m/%d'),
                }

                context = {
                    "project": project,
                    "report": report,
                    "positions": positions,
                    "professions": professions,
                    "machines": machines,
                    "materials": materials,
                    "equipes": equipes,
                    "units": units,
                    "materialproviders": materialproviders,
                    "machineproviders": machineproviders,
                    "tasks": tasks,
                    "machine_types": MACHINE_TYPES,
                    "other": other,
                }
                return render(request, "daily-report-edit.html", context=context)

            else:
                raise PermissionDenied

        else:
            data = dict(request.POST)

            positions = {}
            professions = {}
            machines = {}
            materials = {}
            equipes = {}
            contractors = {}
            tasks = {}
            issues = {}

            for key, value in data.items():
                if "position" in key:
                    positions[key.split("_")[1]] = int(value[0])
                elif "profession" in key:
                    prof = key.split("_")[2].split("-")[0]
                    if key.split("_")[2].split("-")[0] in professions.keys():
                        if "Semi" in key.split("_")[3]:
                            professions[prof][1] += int(value[0])
                        elif "Non" in key.split("_")[3]:
                            professions[prof][2] += int(value[0])
                        else:
                            professions[prof][0] += int(value[0])

                    else:
                        professions[prof] = [0, 0, 0]
                        if "Semi" in key.split("_")[3]:
                            professions[prof][1] += int(value[0])
                        elif "Non" in key.split("_")[3]:
                            professions[prof][2] += int(value[0])
                        else:
                            professions[prof][0] += int(value[0])

                    cont = key.split("_")[2].split("-")[1]
                    if key.split("_")[2].split("-")[1] in contractors.keys():
                        if "Semi" in key.split("_")[3]:
                            contractors[cont][1] += int(value[0])
                        elif "Non" in key.split("_")[3]:
                            contractors[cont][2] += int(value[0])
                        else:
                            contractors[cont][0] += int(value[0])

                    else:
                        contractors[cont] = [0, 0, 0]
                        if "Semi" in key.split("_")[3]:
                            contractors[cont][1] += int(value[0])
                        elif "Non" in key.split("_")[3]:
                            contractors[cont][2] += int(value[0])
                        else:
                            contractors[cont][0] += int(value[0])

                    if key.split("_")[2] in equipes.keys():
                        equipes[key.split("_")[2]].append(int(value[0]))
                    else:
                        equipes[key.split("_")[2]] = []
                        equipes[key.split("_")[2]].append(int(value[0]))

                elif "issueReport" in key:
                    issues[key.split("_")[1]] = value[0]

                elif "machine" in key:
                    if key.split("_")[1] in machines.keys():
                        if "provider" in key:
                            machines[key.split("_")[1]].append(value[0])
                        else:
                            machines[key.split("_")[1]].append(int(value[0]))
                    else:
                        machines[key.split("_")[1]] = []
                        machines[key.split("_")[1]].append(int(value[0]))
                elif "material" in key:
                    if "count" in key:
                        materials[key.split("_")[1]] = [float(value[0]), None, None]
                    elif "unit" in key:
                        materials[key.split("_")[1]][1] = value[0]
                    elif "provider" in key:
                        materials[key.split("_")[1]][2] = value[0]
                elif "task" in key:
                    tasks[key.split("_")[1]] = float(value[0])

            try:
                with transaction.atomic():
                    report = DailyReport.objects.get(id=request.POST.get("report_id"), project=project)
                    ID = report.id
                    DATE_CREATED = report.date_created

                    if report.deletable and report.editable:
                        for item in report.taskreport_set.all():
                            item.update_percentage(True, date=report.date)
                        report.delete()
                    else:
                        raise PermissionDenied

                    report = DailyReport.objects.create(
                        project=project,
                        id=ID,
                        project_name=data['project_name'][0],
                        employer=data["employer"][0],
                        employee=data["employee"][0],
                        contract_number=data["contract_no"][0],
                        date=jdatetime.datetime.strptime(data['date'][0], format="%Y-%m-%d").strftime(
                            "%Y-%m-%d %H:%M:%S"),
                        temperature_min=data["minTemp"][0],
                        temperature_max=data["maxTemp"][0],
                        weather=data["weather_status"][0],
                        dust_value=data["dust_value"][0],
                        consultor_name=data["consultor_name"][0],
                        date_created=DATE_CREATED,
                        edited=True,
                    )
                    report.set_weekday()

                    report.project_name = data['project_name'][0]
                    report.employer = data["employer"][0]
                    report.employee = data["employee"][0]
                    report.contract_number = data["contract_no"][0]
                    # report.date =
                    report.temperature_min = data["minTemp"][0]
                    report.temperature_max = data["maxTemp"][0]
                    report.weather = data["weather_status"][0]
                    report.dust_value = data["dust_value"][0]
                    report.consultor_name = data["consultor_name"][0]
                    report.save()
                    report.set_weekday()

                    for position, count in positions.items():
                        if count > 0:
                            pos = Position.objects.get(name=position, project=project)
                            obj = PositionCount.objects.create(
                                project=project,
                                position=pos,
                                dailyReport=report,
                                count=count,
                            )
                            report.positions.add(obj.position)
                        else:
                            continue

                    for profession, count in professions.items():
                        if sum(count) > 0:
                            prof = Profession.objects.get(name=profession, project=project)
                            obj = ProfessionCount.objects.create(
                                project=project,
                                profession=prof,
                                dailyReport=report,
                                countExpert=count[0],
                                countSemiExpert=count[1],
                                countNonExpert=count[2],
                            )
                            obj.cal_countTotal()

                            report.professions.add(obj.profession)

                        else:
                            continue

                    for machine, count in machines.items():
                        machine = machine.split("_")[0]
                        if count[0] > 0 or count[1] > 0:
                            machine = machine.strip()
                            machine = re.sub(r'[\[\]]', '', machine)
                            machine, family, hardware = machine.split("-")

                            hardware = Hardware.objects.get(
                                project=project,
                                name=hardware
                            )
                            family = MachineFamily.objects.get(
                                project=project,
                                name=family,
                                hardware=hardware,
                            )
                            mach = Machine.objects.get(name=machine,
                                                       type=family,
                                                       hardware=hardware,
                                                       project=project)

                            provider = MachineProvider.objects.get(name=count[3], project=project)
                            if provider.name == "شرکتی":
                                obj = MachineCount.objects.create(
                                    project=project,
                                    machine=mach,
                                    dailyReport=report,
                                    activeCount=count[1],
                                    inactiveCount=count[2],
                                    workHours=count[0],
                                    provider=provider,
                                    totalCount=sum(count[1:3]),
                                    onRent=False,
                                    hardware=hardware,
                                    type=family,
                                )
                            else:
                                obj = MachineCount.objects.create(
                                    project=project,
                                    machine=mach,
                                    dailyReport=report,
                                    activeCount=1 if count[0] > 0 else 0,
                                    inactiveCount=0 if count[0] > 0 else 1,
                                    workHours=count[0],
                                    provider=provider,
                                    totalCount=1,
                                    onRent=True,
                                    hardware=hardware,
                                    type=family,

                                )

                            report.machines.add(obj.machine)

                        else:
                            continue

                    for material, amount in materials.items():
                        material = material.split("_")[0]
                        if amount[0] > 0:
                            material = material.strip()

                            mat = Material.objects.get(name=material, project=project)
                            unit = Unit.objects.get(name=amount[1], project=project)
                            materialprovider = MaterialProvider.objects.get(name=amount[2], project=project)
                            obj = MaterialCount.objects.create(
                                project=project,
                                material=mat,
                                dailyReport=report,
                                amount=amount[0],
                                unit=unit,
                                provider=materialprovider,
                            )
                            report.materials.add(obj.material)
                        else:
                            continue

                    for contractor, count in contractors.items():
                        if sum(count) > 0:
                            cont = Contractor.objects.get(name=contractor, project=project)
                            obj = ContractorCount.objects.create(
                                project=project,
                                contractor=cont,
                                dailyReport=report,
                                countExpert=count[0],
                                countSemiExpert=count[1],
                                countNonExpert=count[2],
                            )
                            obj.cal_countTotal()

                            report.contractors.add(obj.contractor)
                        else:
                            continue

                    for equipe, count in equipes.items():
                        if sum(count) > 0:
                            prof, cont = equipe.split("-")
                            equ = Equipe.objects.get(
                                project=project,
                                profession=Profession.objects.get(name=prof, project=project),
                                contractor=Contractor.objects.get(name=cont, project=project),
                            )
                            obj = EquipeCount.objects.create(
                                project=project,
                                equipe=equ,
                                dailyReport=report,
                                countExpert=count[0],
                                countSemiExpert=count[1],
                                countNonExpert=count[2],
                            )
                            obj.cal_countTotal()

                            report.equipes.add(obj.equipe)
                        else:
                            continue

                    for task, amount in tasks.items():
                        if amount > 0:
                            tsk = Task.objects.get(unique_str=task, project=project)

                            if not tsk.started:
                                tsk.start(date=report.date)

                            parent = TaskReport.objects.filter(task=tsk, project=project).last()
                            tsk_rep = TaskReport.objects.create(
                                project=project,
                                task=tsk,
                                operation=tsk.operation.operation,
                                parent=parent,
                                dailyReport=report,
                                todayVolume=amount,
                                reportDate=report.date,
                                parentTask=tsk.parent,
                            )
                            tsk_rep.update_percentage(False, date=report.date)
                            tsk_rep.update_filtering_fields()
                            report.tasks.add(tsk_rep.task)

                    report.cal_countPeople()
                    report.cal_countMachines()

                # return redirect(to="/home/daily-reports")
                return HttpResponse(True)

            except:
                return HttpResponse("Something went wrong", status=500)


@login_required
def reports_daily(request):
    user = MyUser.objects.get(user=request.user,)
    project = user.projects.all()[0]

    reports = DailyReport.objects.filter(project=project)
    for report in reports:
        report.check_deletability()

    context = {
        "reports": reports,
    }

    return render(request, "reports-list.html", context=context)


@login_required
def report_on_day(request, idd):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd, project=project)

    positions = PositionCount.objects.filter(dailyReport=report, project=project,)
    professions = ProfessionCount.objects.filter(dailyReport=report, project=project,)
    machines = MachineCount.objects.filter(dailyReport=report, project=project,)
    materials = MaterialCount.objects.filter(dailyReport=report, project=project,)
    equipes = EquipeCount.objects.filter(dailyReport=report, project=project,)
    tasks = TaskReport.objects.filter(dailyReport=report, project=project,)

    done_task_zone = []
    parentTaskPercents = {}
    for task in tasks:
        ids = Equipe.objects.filter(profession=task.task.equipe.profession, project=project).values_list('id', flat=True)
        objs = Task.objects.filter(equipe__id__in=ids, project=project)
        entire_item_vol = 0
        entire_item_done = 0
        for obj in objs:
            entire_item_vol += obj.totalVolume
            entire_item_done += obj.doneVolume

        done_task_zone.append([task.id, entire_item_done / entire_item_vol * 100, entire_item_vol])

        if task.task.parent.id in parentTaskPercents.keys():
            parentTaskPercents[task.task.parent.id] += (task.preDoneVolume / task.task.parent.totalVolume * 100 + task.todayVolume / task.task.parent.totalVolume * 100) * task.task.suboperation.weight / 100
        else:
            parentTaskPercents[task.task.parent.id] = (task.preDoneVolume/task.task.parent.totalVolume*100 + task.todayVolume/task.task.parent.totalVolume*100)*task.task.suboperation.weight/100

    machines = machines.order_by('-provider',)

    other = {
        "weather": report.get_weather_display(),
        "weekday": report.get_weekday_display(),
        "date": report.date.strftime('%Y/%m/%d'),
        "entire_items": done_task_zone,
        "parentTaskPercents": parentTaskPercents,
    }

    context = {
        "report": report,
        "positions": positions,
        "professions": professions,
        "machines": machines,
        "materials": materials,
        "equipes": equipes,
        "tasks": tasks,
        "other": other,
    }
    return render(request, "print-report.html", context=context)


@login_required
def print_report_on_day(request, idd):
    context = {}
    POSITION_MAX_COUNT = 31 #30
    PROFESSION_MAX_COUNT = 31 #30
    MACHINE_MAX_COUNT = 34 #33
    MATERIAL_MAX_COUNT = 34 #33
    TASK_MAX_COUNT = 16 #8

    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd, project=project)

    context["headers"] = {
        "project": project,
        "report": report,
        "helper": {
            "weekday": report.get_weekday_display(),
            "weather": report.get_weather_display(),
        },
    }
    context["report"] = report
    context["helper"] = {}


    positions = PositionCount.objects.filter(dailyReport=report, project=project,)
    # professions = ProfessionCount.objects.filter(dailyReport=report, project=project,)
    professions = EquipeCount.objects.filter(dailyReport=report, project=project)

    page_count = max(int(len(positions)/POSITION_MAX_COUNT)+1, int(len(professions) / PROFESSION_MAX_COUNT) + 1)

    distributed_objs = []
    for i in range(page_count):
        if i != page_count-1:
            distributed_objs.append(
                positions[i * POSITION_MAX_COUNT:(i + 1) * POSITION_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                positions[i * POSITION_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
            distributed_objs.append([])

    context_positions = {
        "page_count": int(len(positions)/POSITION_MAX_COUNT)+1,
        "obj_count": len(positions),
        "max_count": POSITION_MAX_COUNT,
        "rem_rows": [POSITION_MAX_COUNT-len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    equipes = Equipe.objects.filter(project=project,)
    desired_instances = equipes.filter(
        contractor=Contractor.objects.get(project=project, name="شرکتی")
    )
    rest_instances = equipes.exclude(
        contractor=Contractor.objects.get(project=project, name="شرکتی")
    )
    rest_instances = rest_instances.order_by("contractor")
    professions = professions.annotate(
        custom_order=Case(
            *[When(equipe=instance, then=Value(i)) for i, instance in enumerate(desired_instances)],
            *[When(equipe=instance, then=Value(len(desired_instances)+i)) for i, instance in enumerate(rest_instances)],
            default=Value(len(desired_instances)+len(rest_instances)),
            output_field=IntegerField(),
        )
    ).order_by('custom_order')

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                professions[i * PROFESSION_MAX_COUNT:(i + 1) * PROFESSION_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                professions[i * PROFESSION_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_professions = {
        "page_count": int(len(professions) / PROFESSION_MAX_COUNT) + 1,
        "obj_count": len(professions),
        "max_count": PROFESSION_MAX_COUNT,
        "rem_rows": [PROFESSION_MAX_COUNT-len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["humanresources"] = {
        "page_count": page_count,
        "positions": context_positions,
        "professions": context_professions,
    },

    # providers = MachineProvider.objects.all(project=project)
    # onOwn = providers.filter(name="شرکتی")
    # onRent = providers.exclude(name="شرکتی")

    machines = MachineCount.objects.filter(project=project, dailyReport=report)
    page_count = int(len(machines) / MACHINE_MAX_COUNT) + 1

    # desired_instances = MachineProvider.objects.filter(
    #     project=project,
    #     name="شرکتی",
    # )
    # machines = machines.annotate(
    #     custom_order=Case(
    #         *[When(provider=instance, then=Value(i)) for i, instance in enumerate(desired_instances)],
    #         default=Value(len(desired_instances)),
    #         output_field=IntegerField(),
    #     )
    # ).order_by('custom_order')
    machines = machines.order_by('onRent')

    # =================================================================================
    # =================================================================================
    # ---------------------Splitting onOwn and onRent machines-------------------------
    # =================================================================================
    """
    onOwn = machines.filter(onRent=False)
    onRent_machines = machines.filter(onRent=True)
    page_count = max(int(len(onOwn) / MACHINE_MAX_COUNT) + 1, int(len(onRent_machines) / MACHINE_MAX_COUNT) + 1)

    onOwn_machines = {}
    for machine in onOwn:
        if machine.machine.type not in onOwn_machines.keys():
            onOwn_machines[machine.machine.type] = {
                "name": machine.machine.type,
                "activeCount": machine.activeCount,
                "inactiveCount": machine.inactiveCount,
                "totalCount": machine.totalCount,
            }
        else:
            onOwn_machines[machine.machine.type]["activeCount"] += machine.activeCount
            onOwn_machines[machine.machine.type]["inactiveCount"] += machine.inactiveCount
            onOwn_machines[machine.machine.type]["totalCount"] += machine.totalCount

    onOwn_machines = list(onOwn_machines.values())

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                onOwn_machines[i * MACHINE_MAX_COUNT:(i + 1) * MACHINE_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                onOwn_machines[i * MACHINE_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_onOwnMachines = {
        "page_count": int(len(onOwn_machines) / MACHINE_MAX_COUNT) + 1,
        "obj_count": len(onOwn_machines),
        "max_count": MACHINE_MAX_COUNT,
        "rem_rows": [MACHINE_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                onRent_machines[i * MACHINE_MAX_COUNT:(i + 1) * MACHINE_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                onRent_machines[i * MACHINE_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_onRentMachines = {
        "page_count": int(len(onRent_machines) / MACHINE_MAX_COUNT) + 1,
        "obj_count": len(onRent_machines),
        "max_count": MACHINE_MAX_COUNT,
        "rem_rows": [MACHINE_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["machines"] = {
        "page_count": page_count,
        "onOwn_machines": context_onOwnMachines,
        "onRent_machines": context_onRentMachines,
    }
    """
    # =================================================================================
    # ------------------End of Splitting onOwn and onRent machines---------------------
    # =================================================================================
    # =================================================================================

    # =================================================================================
    # =================================================================================
    # ------------------------else all machines in one table---------------------------
    # =================================================================================

    # data = {}
    # for machine in machines:
    #     data[machine.machine.type] = {
    #         "name": machine.machine.type,
    #         "provider": machine.provider.name,
    #         "activeCount": machine.activeCount,
    #         "inactiveCount": machine.inactiveCount,
    #         "totalCount": machine.totalCount,
    #         "workHours": machine.workHours,
    #     }
    #
    # machines = list(data.values())

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                machines[i * MACHINE_MAX_COUNT:(i + 1) * MACHINE_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                machines[i * MACHINE_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_machines = {
        "page_count": int(len(machines) / MACHINE_MAX_COUNT) + 1,
        "obj_count": len(machines),
        "max_count": MACHINE_MAX_COUNT,
        "rem_rows": [MACHINE_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["machines"] = {
        "page_count": page_count,
        "machines": context_machines,
    }

    # =================================================================================
    # ------------------------------------End else-------------------------------------
    # =================================================================================
    # =================================================================================

    materials = MaterialCount.objects.filter(project=project, dailyReport=report)
    page_count = int(len(materials) / MATERIAL_MAX_COUNT) + 1

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                materials[i * MATERIAL_MAX_COUNT:(i + 1) * MATERIAL_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                materials[i * MATERIAL_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])


    context_materials = {
        "page_count": int(len(materials) / MATERIAL_MAX_COUNT) + 1,
        "obj_count": len(materials),
        "max_count": MATERIAL_MAX_COUNT,
        "rem_rows": [MATERIAL_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["materials"] = {
        "page_count": page_count,
        "materials": context_materials,
    }

    tasks = TaskReport.objects.filter(dailyReport=report, project=project)
    page_count = int(len(tasks) / TASK_MAX_COUNT) + 1

    done_task_zone = []
    parentTaskPercents = {}
    for task in tasks:
        ids = Equipe.objects.filter(profession=task.task.equipe.profession, project=project).values_list('id', flat=True)
        objs = Task.objects.filter(equipe__id__in=ids, project=project)
        entire_item_vol = 0
        entire_item_done = 0
        for obj in objs:
            entire_item_vol += obj.totalVolume
            entire_item_done += obj.doneVolume

        done_task_zone.append([task.id, entire_item_done / entire_item_vol * 100, entire_item_vol])

        if task.task.parent.id in parentTaskPercents.keys():
            parentTaskPercents[task.task.parent.id] += (task.preDoneVolume / task.task.totalVolume * 100 + task.todayVolume / task.task.totalVolume * 100) * task.task.suboperation.weight / 100
        else:
            parentTaskPercents[task.task.parent.id] = (task.preDoneVolume/task.task.totalVolume*100 + task.todayVolume/task.task.totalVolume*100)*task.task.suboperation.weight/100

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                tasks[i * TASK_MAX_COUNT:(i + 1) * TASK_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                tasks[i * TASK_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_tasks = {
        "page_count": int(len(tasks) / TASK_MAX_COUNT) + 1,
        "obj_count": len(tasks),
        "max_count": TASK_MAX_COUNT,
        "rem_rows": [TASK_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["tasks"] = {
        "page_count": page_count,
        "tasks": context_tasks,
    }

    context["helper"]["entire_items"] = done_task_zone
    context["helper"]["parentTaskPercents"] = parentTaskPercents




    return render(request, "pdf_A4_dailyReport_inDetails.html", context=context)

    # context = {
    #     "report": report,
    #     "positions": positions,
    #     "professions": professions,
    #     "machines": machines,
    #     "materials": materials,
    #     "equipes": equipes,
    #     "tasks": tasks,
    #     "other": other,
    # }
    # return render(request, "print-report.html", context=context)


@login_required
def print_report_compact_on_day(request, idd):
    context = {}
    POSITION_MAX_COUNT = 31 #30
    PROFESSION_MAX_COUNT = 31 #30
    MACHINE_MAX_COUNT = 34 #33
    MATERIAL_MAX_COUNT = 34 #33
    TASK_MAX_COUNT = 16 #8

    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd, project=project)

    context["headers"] = {
        "project": project,
        "report": report,
        "helper": {
            "weekday": report.get_weekday_display(),
            "weather": report.get_weather_display(),
        },
    }
    context["report"] = report
    context["helper"] = {}


    positions = PositionCount.objects.filter(dailyReport=report, project=project,)
    # professions = ProfessionCount.objects.filter(dailyReport=report, project=project,)
    professions = EquipeCount.objects.filter(dailyReport=report, project=project)

    page_count = max(int(len(positions)/POSITION_MAX_COUNT)+1, int(len(professions) / PROFESSION_MAX_COUNT) + 1)

    distributed_objs = []
    for i in range(page_count):
        if i != page_count-1:
            distributed_objs.append(
                positions[i * POSITION_MAX_COUNT:(i + 1) * POSITION_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                positions[i * POSITION_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
            distributed_objs.append([])

    context_positions = {
        "page_count": int(len(positions)/POSITION_MAX_COUNT)+1,
        "obj_count": len(positions),
        "max_count": POSITION_MAX_COUNT,
        "rem_rows": [POSITION_MAX_COUNT-len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    equipes = Equipe.objects.filter(project=project,)
    desired_instances = equipes.filter(
        contractor=Contractor.objects.get(project=project, name="شرکتی")
    )
    rest_instances = equipes.exclude(
        contractor=Contractor.objects.get(project=project, name="شرکتی")
    )
    rest_instances = rest_instances.order_by("contractor")
    professions = professions.annotate(
        custom_order=Case(
            *[When(equipe=instance, then=Value(i)) for i, instance in enumerate(desired_instances)],
            *[When(equipe=instance, then=Value(len(desired_instances)+i)) for i, instance in enumerate(rest_instances)],
            default=Value(len(desired_instances)+len(rest_instances)),
            output_field=IntegerField(),
        )
    ).order_by('custom_order')

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                professions[i * PROFESSION_MAX_COUNT:(i + 1) * PROFESSION_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                professions[i * PROFESSION_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_professions = {
        "page_count": int(len(professions) / PROFESSION_MAX_COUNT) + 1,
        "obj_count": len(professions),
        "max_count": PROFESSION_MAX_COUNT,
        "rem_rows": [PROFESSION_MAX_COUNT-len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["humanresources"] = {
        "page_count": page_count,
        "positions": context_positions,
        "professions": context_professions,
    },

    # providers = MachineProvider.objects.all(project=project)
    # onOwn = providers.filter(name="شرکتی")
    # onRent = providers.exclude(name="شرکتی")

    machines = MachineCount.objects.filter(project=project, dailyReport=report)
    temp = {}
    for machine in machines:
        if machine.machine.type.name not in temp.keys():
            temp[machine.machine.type.name] = {
                "machine": machine.machine.type.name,
                "activeCount": machine.activeCount,
                "inactiveCount": machine.inactiveCount,
                "totalCount": machine.totalCount,
            }
        else:
            temp[machine.machine.type.name]["activeCount"] += machine.activeCount
            temp[machine.machine.type.name]["inactiveCount"] += machine.inactiveCount
            temp[machine.machine.type.name]["totalCount"] += machine.totalCount

    machines = list(temp.values())
    page_count = int(len(machines) / MACHINE_MAX_COUNT) + 1

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                machines[i * MACHINE_MAX_COUNT:(i + 1) * MACHINE_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                machines[i * MACHINE_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_machines = {
        "page_count": int(len(machines) / MACHINE_MAX_COUNT) + 1,
        "obj_count": len(machines),
        "max_count": MACHINE_MAX_COUNT,
        "rem_rows": [MACHINE_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["machines"] = {
        "page_count": page_count,
        "machines": context_machines,
    }

    # =================================================================================
    # ------------------------------------End else-------------------------------------
    # =================================================================================
    # =================================================================================

    materials = MaterialCount.objects.filter(project=project, dailyReport=report)
    temp = {}
    for material in materials:
        if material.material.name not in temp.keys():
            temp[material.material.name] = {
                "material": material.material.name,
                "amount": material.amount * material.unit.coef,
                "unit": material.unit.parent.name if material.unit.parent else material.unit.name,
            }
        else:
            temp[material.material.name]["amount"] += material.amount * material.unit.coef

    materials = list(temp.values())
    page_count = int(len(materials) / MATERIAL_MAX_COUNT) + 1

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                materials[i * MATERIAL_MAX_COUNT:(i + 1) * MATERIAL_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                materials[i * MATERIAL_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])


    context_materials = {
        "page_count": int(len(materials) / MATERIAL_MAX_COUNT) + 1,
        "obj_count": len(materials),
        "max_count": MATERIAL_MAX_COUNT,
        "rem_rows": [MATERIAL_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["materials"] = {
        "page_count": page_count,
        "materials": context_materials,
    }

    tasks = TaskReport.objects.filter(dailyReport=report, project=project)
    operation_ids = TaskReport.objects.filter(dailyReport=report, project=project).values_list('operation',
                                                                                               flat=True).distinct()

    # TODO : Modify the history variable so that instead of created_at feature, it filters report date
    history = TaskReport.objects.filter(operation_id__in=operation_ids, created_at__lt=report.created_at,
                                        project=project)
    history = history.exclude(id__in=tasks.values('id'), project=project)

    tsks = {}

    # if you want it based on Operation model==============================================
    """
    for task in tasks:
        if task.task.operation.operation.name in tsks.keys():
            tsks[task.task.operation.operation.name]['todayVolume'] += task.todayVolume * task.task.suboperation.weight / 100

        else:
            tsks[task.task.operation.operation.name] = {
                'name': task.task.operation.operation.name,
                'todayVolume': task.todayVolume * task.task.suboperation.weight / 100,
                'preDoneVolume': 0.0,
                'entire_item_vol': task.task.operation.operation.amount,
                'entire_item_done': 0.0,
                'entire_item_done_percent': 0.0,
                'unit': task.task.unit,
            }

    for task in history:
        if task.task.operation.operation.name in tsks.keys():
            tsks[task.task.operation.operation.name]['preDoneVolume'] += task.todayVolume * task.task.suboperation.weight / 100

    # endif--------------------------------------------------------------------------------
    """
    # if you want it based on ZoneOperation model==============================================
    for task in tasks:
        if task.task.operation in tsks.keys():
            tsks[task.task.operation][
                'todayVolume'] += task.todayVolume * task.task.suboperation.weight / 100

            if task.parentTask.completed:
                if task.parentTask.completion_date > tsks[task.task.operation]['completion_date']:
                    tsks[task.task.operation][
                        'completion_date'] = task.parentTask.completion_date
            else:
                tsks[task.task.operation][
                    'completion_date'] = None

        else:
            tsks[task.task.operation] = {
                'parentID': task.task.parent.id,
                'name': task.task.operation.operation.name,
                'zone': task.task.operation.zone.name,
                'todayVolume': task.todayVolume * task.task.suboperation.weight / 100,
                'preDoneVolume': 0.0,
                'entire_item_vol': task.task.operation.amount,
                'entire_item_done': 0.0,
                'entire_item_done_percent': 0.0,
                'unit': task.task.unit,
                'start_date': task.task.start_date,
                'completion_date': task.parentTask.completion_date if task.parentTask.completed else None,
            }

    for task in history:
        if task.task.operation in tsks.keys():
            tsks[task.task.operation][
                'preDoneVolume'] += task.todayVolume * task.task.suboperation.weight / 100

    # endif--------------------------------------------------------------------------------

    for key, value in tsks.items():
        tsks[key]['entire_item_done'] = tsks[key]['todayVolume'] + tsks[key]['preDoneVolume']
        tsks[key]['entire_item_done_percent'] = tsks[key]['entire_item_done'] / tsks[key]['entire_item_vol'] * 100

    tasks = list(tsks.values())

    tasks = sorted(tasks, key=lambda x:x['name'])

    page_count = int(len(tasks) / TASK_MAX_COUNT) + 1

    distributed_objs = []
    for i in range(page_count):
        if i != page_count - 1:
            distributed_objs.append(
                tasks[i * TASK_MAX_COUNT:(i + 1) * TASK_MAX_COUNT]
            )
        else:
            distributed_objs.append(
                tasks[i * TASK_MAX_COUNT:]
            )
    while len(distributed_objs) != page_count:
        distributed_objs.append([])

    context_tasks = {
        "page_count": int(len(tasks) / TASK_MAX_COUNT) + 1,
        "obj_count": len(tasks),
        "max_count": TASK_MAX_COUNT,
        "rem_rows": [TASK_MAX_COUNT - len(distributed_objs[i]) for i in range(page_count)],
        "objects": distributed_objs,
    }

    context["tasks"] = {
        "page_count": page_count,
        "tasks": context_tasks,
    }

    # context["helper"]["entire_items"] = done_task_zone
    # context["helper"]["parentTaskPercents"] = parentTaskPercents

    return render(request, "pdf_A4_dailyReport_compact.html", context=context)

    # context = {
    #     "report": report,
    #     "positions": positions,
    #     "professions": professions,
    #     "machines": machines,
    #     "materials": materials,
    #     "equipes": equipes,
    #     "tasks": tasks,
    #     "other": other,
    # }
    # return render(request, "print-report.html", context=context)


@login_required
def compact_report_on_day(request, idd):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd, project=project)

    positions = PositionCount.objects.filter(dailyReport=report, project=project)
    professions = ProfessionCount.objects.filter(dailyReport=report, project=project)
    machines = MachineCount.objects.filter(dailyReport=report, project=project)
    materials = MaterialCount.objects.filter(dailyReport=report, project=project)
    equipes = EquipeCount.objects.filter(dailyReport=report, project=project)

    tasks = TaskReport.objects.filter(dailyReport=report, project=project)
    operation_ids = TaskReport.objects.filter(dailyReport=report, project=project).values_list('operation', flat=True).distinct()

    # TODO : Modify the history variable so that instead of created_at feature, it folters report date
    history = TaskReport.objects.filter(operation_id__in=operation_ids, created_at__lt=report.created_at, project=project)
    history = history.exclude(id__in=tasks.values('id'), project=project)
    tsks = {}

    # if you want it based on Operation model==============================================
    """
    for task in tasks:
        if task.task.operation.operation.name in tsks.keys():
            tsks[task.task.operation.operation.name]['todayVolume'] += task.todayVolume * task.task.suboperation.weight / 100

        else:
            tsks[task.task.operation.operation.name] = {
                'name': task.task.operation.operation.name,
                'todayVolume': task.todayVolume * task.task.suboperation.weight / 100,
                'preDoneVolume': 0.0,
                'entire_item_vol': task.task.operation.operation.amount,
                'entire_item_done': 0.0,
                'entire_item_done_percent': 0.0,
                'unit': task.task.unit,
            }

    for task in history:
        if task.task.operation.operation.name in tsks.keys():
            tsks[task.task.operation.operation.name]['preDoneVolume'] += task.todayVolume * task.task.suboperation.weight / 100
    
    # endif--------------------------------------------------------------------------------
    """
    # if you want it based on ZoneOperation model==============================================
    for task in tasks:
        if task.task.operation in tsks.keys():
            tsks[task.task.operation][
                'todayVolume'] += task.todayVolume * task.task.suboperation.weight / 100

        else:
            tsks[task.task.operation] = {
                'name': task.task.operation.operation.name,
                'zone': task.task.operation.zone.name,
                'todayVolume': task.todayVolume * task.task.suboperation.weight / 100,
                'preDoneVolume': 0.0,
                'entire_item_vol': task.task.operation.amount,
                'entire_item_done': 0.0,
                'entire_item_done_percent': 0.0,
                'unit': task.task.unit,
            }

    for task in history:
        if task.task.operation in tsks.keys():
            tsks[task.task.operation][
                'preDoneVolume'] += task.todayVolume * task.task.suboperation.weight / 100

    # endif--------------------------------------------------------------------------------

    for key, value in tsks.items():
        tsks[key]['entire_item_done'] = tsks[key]['todayVolume'] + tsks[key]['preDoneVolume']
        tsks[key]['entire_item_done_percent'] = tsks[key]['entire_item_done'] / tsks[key]['entire_item_vol'] * 100


    temp = {}
    for machine in machines:
        if machine.machine.type.name not in temp.keys():
            temp[machine.machine.type.name] = {
                "machine": machine.machine.type.name,
                "activeCount": machine.activeCount,
                "inactiveCount": machine.inactiveCount,
                "totalCount": machine.totalCount,
            }
        else:
            temp[machine.machine.type.name]["activeCount"] += machine.activeCount
            temp[machine.machine.type.name]["inactiveCount"] += machine.inactiveCount
            temp[machine.machine.type.name]["totalCount"] += machine.totalCount

    machines = [value for key, value in temp.items()]

    temp = {}
    for material in materials:
        if material.material.name not in temp.keys():
            temp[material.material.name] = {
                "material": material.material.name,
                "amount": material.amount*material.unit.coef,
                "unit": material.unit.parent.name if material.unit.parent else material.unit.name,
            }
        else:
            temp[material.material.name]["amount"] += material.amount*material.unit.coef

    materials = list(temp.values())

    other = {
        "weather": report.get_weather_display(),
        "weekday": report.get_weekday_display(),
        "date": report.date.strftime('%Y/%m/%d'),
    }

    context = {
        "report": report,
        "positions": positions,
        "professions": professions,
        "machines": machines,
        "materials": materials,
        "equipes": equipes,
        "tasks": tsks.values(),
        "other": other,
    }
    return render(request, "print-short-report.html", context=context)


@login_required
def get_options(request, typee):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        if typee == "unitforunit":
            data = Unit.objects.filter(parent__isnull=True, project=project)

            if data.exists():
                data = json.dumps(list(data.values()))
            else:
                data = "[]"

            context = {
                typee: data,
            }
            return JsonResponse(context)

        elif "filtering" in typee:
            model = request.POST.get("model").split("-")[1]
            data = EDIT_BASE_DATA[model].objects.filter(project=project)

            if model == "task":
                data = Operation.objects.filter(project=project)
            elif model == "contractor":
                data = Contractor.objects.filter(project=project)

            if data.exists():
                data = json.dumps(list(data.values()))
            else:
                data = "[]"

            context = {
                "options": data,
            }
            return JsonResponse(context)

        elif typee == "hardware":
            data = Hardware.objects.filter(project=project)

            if data.exists():
                data = json.dumps(list(data.values()))
            else:
                data = "[]"

            context = {
                typee: data,
            }
            return JsonResponse(context)

        elif typee == "machineFamily":
            data = MachineFamily.objects.filter(project=project)
            objs = []
            for item in data:
                objs.append({
                    "name": item.name,
                    "hardware": item.hardware.name,
                })

            context = {
                typee: objs,
            }

            return JsonResponse(context, safe=False)

        data = json.loads(request.POST['options'])["options"]
        data = [item.strip().strip() for item in data]
        if "equipe" in typee:
            data = [f"{item.strip().split('-')[0].strip()}-{item.split('-')[-1].strip()}" for item in data]
        else:
            pass
        if typee == "profession":
            data = Profession.objects.exclude(name__in=data).filter(project=project)
        elif "provider" in typee:
            if "machineprovider" == typee:
                data = MachineProvider.objects.filter(project=project)
            elif "materialprovider" == typee:
                data = MaterialProvider.objects.filter(project=project)
        elif typee == "unit":
            data = Unit.objects.exclude(name__in=data).filter(project=project)
        elif typee == "position":
            data = Position.objects.exclude(name__in=data).filter(project=project)
        elif typee == "machine":
            data = Machine.objects.exclude(name__in=data).filter(project=project)
        elif typee == "material":
            data = Material.objects.exclude(name__in=data).filter(project=project)
        elif typee == "contractor":
            data = Contractor.objects.exclude(name__in=data).filter(project=project)
        elif typee == "task":
            data = Equipe.objects.exclude(name__in=data).filter(project=project)
        elif typee == "zone":
            data = Zone.objects.exclude(name__in=data).filter(project=project)
        elif typee == "equipe":
            data = Equipe.objects.exclude(name__in=data).filter(project=project)
            if len(data) > 0:
                final = {}
                for item in data:
                    prof = item.profession.name
                    cont = item.contractor.name
                    final[f"{prof}-{cont}"] = [prof, cont]
                context = {
                    typee: data,
                }
                return JsonResponse(final)
            else:
                data = "[]"
                context = {
                    typee: data,
                }
                return JsonResponse(context)


        if data.exists():
            data = json.dumps(list(data.values()))
        else:
            data = "[]"

        context = {
            typee: data,
        }
        return JsonResponse(context)

    else:
        pass


@login_required
def get_tasks(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        data = json.loads(request.POST['options'])["options"]
        # data = [item.strip().split("-") for item in data]
        data = list(
            map(
                lambda x: "".join([x[0].strip(), "-", x[1].strip(), "-", x[2].strip(), "-", x[3].strip()]),
                [item.strip().split("-") for item in data]
            )
        )
        data = Task.objects.exclude(unique_str__in=data).filter(project=project)
        if data.exists():
            out = []
            for item in data:
                obj = {
                    "name": item.name,
                    "equipe": item.equipe.name,
                    "zone": item.zone.name,
                    "totalVolume": item.totalVolume,
                    "unit": item.unit.name,
                    "doneVolume": item.doneVolume,
                    "donePercentage": item.donePercentage,
                }
                out.append(obj)

            data = json.dumps(out)
        else:
            data = "[]"
            data = {
                "task": data,
            }
            data = json.dumps(data)
        return JsonResponse(data, safe=False)

    else:
        pass


@login_required
def get_task(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name, prof, cont, zone = [item.strip() for item in request.POST['options'].split("-")]

        item = Task.objects.filter(
            project=project,
            name=name,
            zone=Zone.objects.get(name=zone, project=project),
            equipe=Equipe.objects.get(name=f"{prof}-{cont}", project=project),
        )
        if item.exists():
            item = item[0]
            data = {
                "name": item.name,
                "equipe": item.equipe.name,
                "zone": item.zone.name,
                "totalVolume": item.totalVolume,
                "unit": item.unit.name,
                "doneVolume": item.doneVolume,
                "donePercentage": item.donePercentage,
            }
            # data = json.dumps(data)
        else:
            data = []

        return JsonResponse(data,)

    else:
        pass


@login_required
def get_units(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        units = Unit.objects.filter(project=project)
        if units.exists():
            data = json.dumps(list(units.values()))
        else:
            data = "[]"
        context = {
            "units": data
        }
        return JsonResponse(context)


@login_required
def get_professions(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        professions = Profession.objects.filter(project=project)
        if professions.exists():
            data = json.dumps(list(professions.values()))
        else:
            data = "[]"
        context = {
            "professions": data
        }
        return JsonResponse(context)


@login_required
def get_machines(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        data = Machine.objects.filter(project=project)
        objs = []
        for item in data:
            objs.append({
                "name": item.name,
                "type": item.type.name,
                "hardware": item.hardware.name,
            })

        context = {
            "machines": objs,
        }

        return JsonResponse(context)



@login_required
def get_machineFamilies(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        machineFamilies = MachineFamily.objects.filter(project=project)
        if machineFamilies.exists():
            data = json.dumps(list(machineFamilies.values()))
        else:
            data = "[]"
        context = {
            "machineFamilies": data
        }
        return JsonResponse(context)


@login_required
def get_hardwares(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        hardwares = Hardware.objects.filter(project=project)
        if hardwares.exists():
            data = json.dumps(list(hardwares.values()))
        else:
            data = "[]"
        context = {
            "hardwares": data
        }
        return JsonResponse(context)


@login_required
def get_contractors(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        contractors = Contractor.objects.filter(project=project)
        if contractors.exists():
            data = json.dumps(list(contractors.values()))
        else:
            data = "[]"
        context = {
            "contractors": data
        }
        return JsonResponse(context)


@login_required
def get_issues(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        issues = Issue.objects.filter(project=project)
        if issues.exists():
            data = json.dumps(list(issues.values()))
        else:
            data = "[]"
        context = {
            "issues": data
        }
        return JsonResponse(context)


@login_required
def get_projectFields(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        projectFields = ProjectField.objects.filter(project=project)
        if projectFields.exists():
            data = json.dumps(list(projectFields.values()))
        else:
            data = "[]"
        context = {
            "projectFields": data
        }
        return JsonResponse(context)


@login_required
def get_operations(request, ID=None):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        if ID:
            opr = Operation.objects.get(id=ID, project=project)
            return HttpResponse(opr)
        else:
            operations = Operation.objects.filter(project=project)
            if operations.exists():
                data = json.dumps(list(operations.values()))
            else:
                data = "[]"
            context = {
                "operations": data
            }
            return JsonResponse(context)


@login_required
def get_suboperations(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        opr_name = request.GET.get("operation")
        suboperations = SubOperation.objects.filter(
            project=project,
            parent=Operation.objects.get(name=opr_name, project=project)
        )
        if suboperations.exists():
            data = json.dumps(list(suboperations.values()))
        else:
            data = "[]"
        context = {
            "suboperations": data
        }
        return JsonResponse(context)


@login_required
def get_subtasks_of(request, ID):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        subtasks = Task.objects.filter(
            project=project,
            parent=ParentTask.objects.get(id=ID, project=project)
        )
        data = []
        for subtask in subtasks:
            foreign_key_fields = {
                'name': subtask.suboperation.name,
                'weight': subtask.suboperation.weight,
                'unit': subtask.suboperation.unit.name,
                # Add more fields as needed
            }
            instance_fields = {
                'totalVolume': subtask.totalVolume,
                'doneVolume': subtask.doneVolume,
                'donePercentage': subtask.donePercentage,
                'started': subtask.started,
                'completed': subtask.completed,
                'start_date': subtask.start_date,
                'completion_date': subtask.completion_date,

                # Add more fields as needed
                'foreigns': foreign_key_fields
            }
            data.append(instance_fields)

        # if subtasks.exists():
        #     data = json.dumps(list(subtasks.values()))
        # else:
        #     data = "[]"
        # context = {
        #     "subtasks": data
        # }

        return JsonResponse(data, safe=False)


@login_required
def get_subtask_in_report(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        operation = request.POST.get("operation")
        suboperation = request.POST.get("suboperation")
        zone = request.POST.get("zone")
        equipe = request.POST.get("equipe")


        operation = Operation.objects.get(name=operation, project=project)
        zone = Zone.objects.get(name=zone, project=project)
        equipe = Equipe.objects.get(name=equipe, project=project)
        suboperation = SubOperation.objects.get(name=suboperation, parent=operation, project=project)

        zoneoperation = ZoneOperation.objects.get(operation=operation, zone=zone, project=project)

        subtask = Task.objects.get(
            project=project,
            operation=zoneoperation,
            suboperation=suboperation,
            equipe=equipe,
            zone=zone,
        )

        data = []
        operation_fields = {
            'name': subtask.parent.operation.operation.name,
            'totalVolume': subtask.parent.totalVolume,
            'doneVolume': subtask.parent.doneVolume,
            'donePercentage': subtask.parent.donePercentage,
            # Add more fields as needed
        }

        suboperation_fields = {
            'name': subtask.suboperation.name,
        }

        instance_fields = {
            'equipe': subtask.equipe.name,
            'unit': subtask.unit.name,
            'zone': subtask.zone.name,
            'totalVolume': subtask.totalVolume,
            'doneVolume': subtask.doneVolume,
            'donePercentage': subtask.donePercentage,
            'started': subtask.started,
            'completed': subtask.completed,
            'start_date': subtask.start_date.strftime(format="%Y/%m/%d") if subtask.start_date is not None else None,
            'completion_date': subtask.completion_date.strftime(format="%Y/%m/%d") if subtask.completion_date is not None else None,
            'freeVolume': subtask.totalVolume - subtask.doneVolume,

            # Add more fields as needed
            'operation': operation_fields,
            'suboperation': suboperation_fields,
        }

        data.append(instance_fields)

        return JsonResponse(data, safe=False)


@login_required
def get_zoneoperations(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        opr_name = request.GET.get("operation")
        operation = Operation.objects.get(name=opr_name, project=project)
        zoneoperations = operation.zones.filter(project=project)
        data = [
            {
                "operation": item.operation.name,
                "zone": item.zone.name,
                "unit": item.unit.name,
            } for item in zoneoperations
        ]
        # zoneoperations = ZoneOperation.objects.filter(
        #     operation=Operation.objects.get(name=opr_name)
        # )
        # if zoneoperations.exists():
        #     data = json.dumps(list(zoneoperations.values()))
        # else:
        #     data = "[]"
        context = {
            "zoneoperations": data
        }
        return JsonResponse(context)


@login_required
def get_all_equipes(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        equipes = Equipe.objects.filter(project=project)
        if equipes.exists():
            data = json.dumps(list(equipes.values()))
        else:
            data = "[]"
        context = {
            "equipes": data
        }
        return JsonResponse(context)


@login_required
def get_equipes_in_report(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        operation = request.POST.get('operation')
        suboperation = request.POST.get('suboperation')
        zone = request.POST.get('zone')

        tasks = Task.objects.filter(
            project=project,
            operation=ZoneOperation.objects.get(
                project=project,
                operation=Operation.objects.get(name=operation, project=project),
                zone=Zone.objects.get(name=zone, project=project),
            ),
            suboperation=SubOperation.objects.get(
                project=project,
                name=suboperation,
                parent=Operation.objects.get(name=operation, project=project),
            ),
            zone=Zone.objects.get(name=zone, project=project),
        ).values_list('unique_str')

        if tasks.exists():
            # data = json.dumps(list(tasks.values()))
            data = [item[0] for item in list(tasks)]
        else:
            data = []
        context = {
            "tasks": data,
        }
        return JsonResponse(context)


@login_required
def get_freeAmount(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        model = request.GET.get('model')
        if model == "zoneoperation":
            operation = request.GET.get('operation')
            operation = Operation.objects.get(name=operation, project=project)
            zone = request.GET.get('zone')
            zoneoperation = ZoneOperation.objects.get(
                project=project,
                operation=operation,
                zone=Zone.objects.get(name=zone, project=project),
            )

            if request.GET.get('mode') == "assigned":
                assignedAmount = zoneoperation.assignedAmount
                return HttpResponse(assignedAmount)

            else:
                freeAmount = zoneoperation.freeAmount
                return HttpResponse(freeAmount)

        elif model == "operation":
            if request.GET.get('mode') == "free":
                operation = request.GET.get('operation')
                operation = Operation.objects.get(name=operation, project=project)
                freeAmount = operation.freeAmount

                zone = request.GET.get('zone')
                zoneoperation = ZoneOperation.objects.get(
                    project=project,
                    operation=operation,
                    zone=Zone.objects.get(name=zone, project=project)
                )
                # print(f"free amount for {operation} is:{freeAmount} + {zoneoperation.amount} = {freeAmount + zoneoperation.amount}")
                freeAmount += zoneoperation.amount

                return HttpResponse(freeAmount)

            else:
                operation = request.GET.get('operation')
                operation = Operation.objects.get(name=operation, project=project)
                assigendAmount = operation.assignedAmount

                return HttpResponse(assigendAmount)

        elif model == "suboperation":
            if request.GET.get('mode') == "weight":
                operation = request.GET.get('operation')
                suboperation = request.GET.get('suboperation')

                operation = Operation.objects.get(name=operation, project=project)
                suboperation = SubOperation.objects.get(name=suboperation, parent=operation, project=project)

                freeWeight = operation.freeWeight + suboperation.weight

                return HttpResponse(freeWeight)

            elif request.GET.get('mode') == "free":
                operation = request.GET.get('operation')
                suboperation = request.GET.get('suboperation')

                operation = Operation.objects.get(name=operation, project=project)
                suboperation = SubOperation.objects.get(name=suboperation, parent=operation, project=project)

                freeAmount = operation.freeAmount + suboperation.amount

                return HttpResponse(freeAmount)


@login_required
def get_zones(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        zones = Zone.objects.filter(project=project)
        if zones.exists():
            data = json.dumps(list(zones.values()))
        else:
            data = "[]"
        context = {
            "zones": data
        }
        return JsonResponse(context)


@login_required
def get_materialproviders(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        materialproviders = MaterialProvider.objects.filter(project=project)
        if materialproviders.exists():
            data = json.dumps(list(materialproviders.values()))
        else:
            data = "[]"
        context = {
            "materialproviders": data
        }
        return JsonResponse(context)


@login_required
def get_machineproviders(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        machineproviders = MachineProvider.objects.filter(project=project)
        if machineproviders.exists():
            data = json.dumps(list(machineproviders.values()))
        else:
            data = "[]"
        context = {
            "machineproviders": data
        }
        return JsonResponse(context)


@login_required
def check_deletability(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        idd = request.POST['id']
        rep = DailyReport.objects.get(id=idd, project=project)

        return HttpResponse(rep.deletable)


@login_required
def check_editability(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        idd = request.POST['id']
        rep = DailyReport.objects.get(id=idd, project=project)

        return HttpResponse(rep.editable)


@login_required
def check_dailyreport_existence(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":

        date = request.POST.get("date")
        date, time = date.split(" ")
        date = date.replace("/", "-")

        if jdatetime.datetime.strptime(date, format="%Y-%m-%d").date() > jdatetime.date.today():
            return HttpResponse("تاریخ نامعتبر. تاریخ ورودی نمیتواند مربوط به روزهای آینده باشد.", status=500)

        if len(DailyReport.objects.filter(project=project)):
            if jdatetime.datetime.strptime(date, format="%Y-%m-%d").date() < DailyReport.objects.filter(project=project).last().short_date:
                return HttpResponse("تاریخ نامعتبر. تاریخ ورودی نمیتواند قبل تر از آخرین گزارش ثبت شده باشد.", status=500)

        report = get_object_or_404(DailyReport, short_date=date, project=project)
        if report:
            return HttpResponse(True)

def findOutputTarget(pivot_fields):
    target = 0
    # print(">>>>>>>>", pivot_fields)
    for pivot in pivot_fields:
        # print(">>>>", target, FILTERS_WEIGHTS[pivot])
        target += FILTERS_WEIGHTS[pivot]

    target = FILTERS_OUTPUT_PIVOT[target]

    return target


def group_queryset(queryset, pivot_fields, target, analyzeType, headers=[]):
    if not pivot_fields:
        return list(queryset), headers
    pivot_field = pivot_fields[0]
    hdrs = headers.copy()
    grouped_results = {}
    for key, group in groupby(queryset, key=lambda obj: getattr(obj, pivot_field)):
        hdrs = headers.copy()
        hdrs.append(key.name)
        # Recursively group the remaining queryset for the next pivot fields
        nested_results, hdrs = group_queryset(group, pivot_fields[1:], target, analyzeType=analyzeType, headers=hdrs)

        if type(nested_results) is list:
            if analyzeType == "Ahjam":
                data = {
                    "totalVolume": 0,
                    "doneVolume": 0,
                    "donePercentage": 0,
                    "unit": "unit",
                }
                finalAttribute = "TOTALVOLUME"
            elif analyzeType == "machine":
                data = {
                    "workHours": 0,
                    "activeCount": 0,
                    "inactiveCount": 0,
                    "totalCount": 0,
                    "unit": "ساعت",
                    "headers": hdrs,
                    # "hardware": nested_results[0].hardware.name,
                    # "type": nested_results[0].type.name,
                    # "machine": nested_results[0].type.name,
                }
                # headers =
                finalAttribute = "WORKHOURS"
            elif analyzeType == "material":
                data = {
                    "amount": 0,
                }
                finalAttribute = "AMOUNT"


            cache_ids = []
            # print(nested_results)
            for result_obj in nested_results:

                instance = result_obj
                for attribute in OUTPUT_TARGETS[target]["ID"]:
                    instance = getattr(instance, attribute)

                if instance not in cache_ids:
                    instance_2 = result_obj
                    for feature in OUTPUT_TARGETS[target]["VALUES"][finalAttribute]:
                        instance_2 = getattr(instance_2, feature)

                    if analyzeType == "Ahjam":
                        data["totalVolume"] += instance_2
                        data["unit"] = result_obj.operation.unit
                    elif analyzeType == "machine":
                        data["workHours"] += instance_2
                        data["activeCount"] += result_obj.activeCount
                        data["inactiveCount"] += result_obj.inactiveCount
                        data["totalCount"] += result_obj.totalCount
                    elif analyzeType == "material":
                        data["amount"] += instance_2*result_obj.unit.coef
                        if result_obj.unit.parent:
                            data["unit"] = result_obj.unit.parent
                        else:
                            data["unit"] = result_obj.unit

                    cache_ids.append(instance)
                else:
                    pass

                if analyzeType == "Ahjam":
                    data["doneVolume"] += (result_obj.todayVolume * result_obj.task.suboperation.weight / 100)
                    data["donePercentage"] = data["doneVolume"] / data["totalVolume"] * 100

            for k in FILTER_KEY_NAMES[type(key)]:
                key = getattr(key, k)
            # print(">>> ", type(key), key)
            grouped_results[key] = data
        else:
            for k in FILTER_KEY_NAMES[type(key)]:
                key = getattr(key, k)
            # print(">>> ", type(key), key)
            grouped_results[key] = nested_results


    return grouped_results, hdrs


@login_required
def analyzer(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":

        context = {
            'context': False,
        }
        return render(request, 'analyzer.html', context=context)

    elif request.method == "POST":
        data = dict(request.POST)
        # print(data)
        query = {
            "operation": None,
            "zone": None,
            "contractor": None,
            "machine": None,
            "hardware": None,
            "machineFamily": None,
            "material": None,
            "provider": None,
        }
        query_formula = []

        if data["analyze-type"][0] == "Ahjam":
            for key in sorted(list(data.keys())):
                if "priority" in key:
                    priority, typee, _ = key.split("_")
                    if '0' in data[key]:
                        data[key] = 0
                        objs = FILTERS[typee].objects.filter(project=project)
                    else:
                        objs = FILTERS[typee].objects.filter(id__in=data[key], project=project)
                    query[typee] = objs
                    query_formula.append(typee)

                elif "date-from" == key:
                    lowerDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d")
                    lowerDate = lowerDate.togregorian()
                    query["lower-date"] = lowerDate.strftime("%Y-%m-%d")
                    query["lower-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("lower-date")

                elif "date-through" == key:
                    one_day = jdatetime.timedelta(days=1)
                    upperDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d") + one_day
                    upperDate = upperDate.togregorian()
                    query["upper-date"] = upperDate.strftime("%Y-%m-%d")
                    query["upper-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("upper-date")

            if "operation" not in query_formula:
                query_formula.append("operation")
                query['operation'] = Operation.objects.filter(project=project)

            priorities_values = []
            requested_models = []
            requested_instances = {}
            for item in query_formula:
                if "date" in item:
                    continue
                priorities_values.append(
                    list(query[item].values_list('name', flat=True))
                )
                requested_models.append(item)
                requested_instances[item] = list(query[item].values_list('id', flat=True))

            priority_depth = len(priorities_values)

            requested_models_persian = []
            for item in requested_models:
                requested_models_persian.append(MODELS_PERSIAN[item])

            parentTasks = ParentTask.objects.filter(project=project)
            for model in requested_models:
                q_filter = Q()

                for step in MODELS_PATH_TO_EXCLUDE[model]['models']:
                    index = MODELS_PATH_TO_EXCLUDE[model]['models'].index(step)
                    field = getattr(step, f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}", None)
                    if field is not None:
                        q_filter |= Q(**{f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}_id__in": requested_instances[model]})
                        requested_instances[model] = step.objects.filter(q_filter).filter(project=project).values_list('id', flat=True)

                q_filter = Q()
                field = getattr(ParentTask, f"{model}", None)
                if field is not None:
                    q_filter |= Q(**{f"{model}_id__in": requested_instances[model]})
                    parentTasks = parentTasks.filter(q_filter).filter(project=project)

            parentTasks = parentTasks.filter(project=project).values_list('id', flat=True)
            taskReports = TaskReport.objects.filter(parentTask_id__in=parentTasks, project=project)

            if "lower-date" in query_formula and "upper-date" in query_formula:
                taskReports = taskReports.filter(
                    project=project,
                    reportDate__lt=query["upper-date"],
                    reportDate__gt=query["lower-date"],
                )
                dates_filters = {
                    "lower": query["lower-date-jalali"].replace("-", "/"),
                    "upper": query["upper-date-jalali"].replace("-", "/"),
                }

            # print(taskReports)

            taskReports = taskReports.order_by(*requested_models)
            target = findOutputTarget(requested_models)
            tree, _ = group_queryset(taskReports, requested_models, target=target, analyzeType=data["analyze-type"][0])

        elif data["analyze-type"][0] == "machine":
            for key in sorted(list(data.keys())):
                if "priority" in key:
                    priority, typee, _ = key.split("_")

                    if typee == "provider":
                        typee = data["analyze-type"][0]+"Provider"

                    if '0' in data[key]:
                        data[key] = 0
                        objs = FILTERS[typee].objects.filter(project=project)
                    else:
                        objs = FILTERS[typee].objects.filter(id__in=data[key], project=project)
                    query[typee] = objs
                    query_formula.append(typee)

                elif "date-from" == key:
                    lowerDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").togregorian()
                    query["lower-date"] = lowerDate.strftime("%Y-%m-%d")
                    query["lower-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("lower-date")

                elif "date-through" == key:
                    one_day = jdatetime.timedelta(days=1)
                    upperDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d") + one_day
                    upperDate = upperDate.togregorian()
                    query["upper-date"] = upperDate.strftime("%Y-%m-%d")
                    query["upper-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("upper-date")

            if "machine" not in query_formula and "machineFamily" not in query_formula and "hardware" not in query_formula:
                query_formula.append("machine")
                query['machine'] = Machine.objects.filter(project=project)

            priorities_values = []
            requested_models = []
            requested_instances = {}
            for item in query_formula:
                if "date" in item:
                    continue
                priorities_values.append(
                    list(query[item].values_list('name', flat=True))
                )
                requested_models.append(item)
                requested_instances[item] = list(query[item].values_list('id', flat=True))

            priority_depth = len(priorities_values)

            requested_models_persian = []
            for item in requested_models:
                requested_models_persian.append(MODELS_PERSIAN[item])

            dailyReports = DailyReport.objects.filter(project=project)
            if "lower-date" in query_formula and "upper-date" in query_formula:
                dailyReports = dailyReports.filter(
                    # date__lt=jdatetime.datetime.strptime(query["upper-date"], format="%Y-%m-%d").togregorian(),
                    # date__gt=jdatetime.datetime.strptime(query["lower-date"], format="%Y-%m-%d").togregorian(),
                    date__lt=query["upper-date"],
                    date__gt=query["lower-date"],
                )
                # print(">>>", type(query["lower-date"]), query["lower-date"])
                dates_filters = {
                    "lower": query["lower-date-jalali"].replace("-", "/"),
                    "upper": query["upper-date-jalali"].replace("-", "/"),
                }

            requested_models.append("dailyReportMachine")
            requested_instances["dailyReportMachine"] = dailyReports.values_list("id", flat=True)
            machineCounts = MachineCount.objects.filter(project=project)
            onRent = True if data.get("ownership")[0]=="onRent" else False if data.get("ownership")[0]=="onOwn" else None
            machineCounts = machineCounts.filter(onRent=onRent)
            for model in requested_models:
                q_filter = Q()
                for step in MODELS_PATH_TO_EXCLUDE[model]['models']:
                    index = MODELS_PATH_TO_EXCLUDE[model]['models'].index(step)
                    field = getattr(step, f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}", None)
                    if field is not None:
                        q_filter |= Q(
                            **{f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}_id__in": requested_instances[model]})
                        machineCounts = machineCounts.filter(q_filter).filter(project=project).values_list('id', flat=True)

                q_filter = Q()
                field = getattr(MachineCount, f"{model}", None)
                if field is not None:
                    q_filter |= Q(**{f"{model}_id__in": requested_instances[model]})
                    machineCounts = machineCounts.filter(q_filter).filter(project=project)

            machineCounts = MachineCount.objects.filter(id__in=machineCounts, project=project)
            # requested_models[requested_models.index("dailyReportMachine")] = "dailyReport"
            if "machineProvider" in requested_models:
                requested_models[requested_models.index("machineProvider")] = "provider"
            if "machineFamily" in requested_models:
                requested_models[requested_models.index("machineFamily")] = "type"
            requested_models.remove("dailyReportMachine")
            machineCounts = machineCounts.order_by(*requested_models)
            target = MachineCount
            # target = findOutputTarget(requested_models)
            tree, _ = group_queryset(machineCounts, requested_models, target=target, analyzeType=data["analyze-type"][0])

        elif data["analyze-type"][0] == "material":
            for key in sorted(list(data.keys())):
                if "priority" in key:
                    priority, typee, _ = key.split("_")

                    if typee == "provider":
                        typee = data["analyze-type"][0] + "Provider"

                    if '0' in data[key]:
                        data[key] = 0
                        objs = FILTERS[typee].objects.filter(project=project)
                    else:
                        objs = FILTERS[typee].objects.filter(id__in=data[key], project=project)
                    query[typee] = objs
                    query_formula.append(typee)

                elif "date-from" == key:
                    lowerDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").togregorian()
                    query["lower-date"] = lowerDate.strftime("%Y-%m-%d")
                    query["lower-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("lower-date")

                elif "date-through" == key:
                    one_day = jdatetime.timedelta(days=1)
                    upperDate = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d") + one_day
                    upperDate = upperDate.togregorian()
                    query["upper-date"] = upperDate.strftime("%Y-%m-%d")
                    query["upper-date-jalali"] = jdatetime.datetime.strptime(data[key][0], format="%Y/%m/%d").strftime("%Y-%m-%d")
                    query_formula.append("upper-date")

            if "material" not in query_formula:
                query_formula.append("material")
                query['material'] = Material.objects.filter(project=project)

            priorities_values = []
            requested_models = []
            requested_instances = {}
            for item in query_formula:
                if "date" in item:
                    continue
                priorities_values.append(
                    list(query[item].values_list('name', flat=True))
                )
                requested_models.append(item)
                requested_instances[item] = list(query[item].values_list('id', flat=True))

            priority_depth = len(priorities_values)

            requested_models_persian = []
            for item in requested_models:
                requested_models_persian.append(MODELS_PERSIAN[item])

            dailyReports = DailyReport.objects.filter(project=project)
            if "lower-date" in query_formula and "upper-date" in query_formula:
                dailyReports = dailyReports.filter(
                    # date__lt=jdatetime.datetime.strptime(query["upper-date"], format="%Y-%m-%d").togregorian(),
                    # date__gt=jdatetime.datetime.strptime(query["lower-date"], format="%Y-%m-%d").togregorian(),
                    date__lt=query["upper-date"],
                    date__gt=query["lower-date"],
                )
                # print(">>>", type(query["lower-date"]), query["lower-date"])
                dates_filters = {
                    "lower": query["lower-date-jalali"].replace("-", "/"),
                    "upper": query["upper-date-jalali"].replace("-", "/"),
                }

            requested_models.append("dailyReportMaterial")
            requested_instances["dailyReportMaterial"] = dailyReports.values_list("id", flat=True)

            materialCounts = MaterialCount.objects.filter(project=project)

            for model in requested_models:
                q_filter = Q()
                for step in MODELS_PATH_TO_EXCLUDE[model]['models']:
                    index = MODELS_PATH_TO_EXCLUDE[model]['models'].index(step)
                    field = getattr(step, f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}", None)
                    if field is not None:
                        q_filter |= Q(
                            **{f"{MODELS_PATH_TO_EXCLUDE[model]['attrs'][index]}_id__in": requested_instances[model]})
                        materialCounts = materialCounts.filter(q_filter).filter(project=project).values_list('id', flat=True)

                q_filter = Q()
                field = getattr(MaterialCount, f"{model}", None)
                if field is not None:
                    q_filter |= Q(**{f"{model}_id__in": requested_instances[model]})
                    materialCounts = materialCounts.filter(q_filter).filter(project=project)

            materialCounts = MaterialCount.objects.filter(id__in=materialCounts, project=project)

            # requested_models[requested_models.index("dailyReportMachine")] = "dailyReport"
            if "materialProvider" in requested_models:
                requested_models[requested_models.index("materialProvider")] = "provider"
            requested_models.remove("dailyReportMaterial")
            materialCounts = materialCounts.order_by(*requested_models)
            target = MaterialCount
            # target = findOutputTarget(requested_models)
            tree, _ = group_queryset(materialCounts, requested_models, target=target, analyzeType=data["analyze-type"][0])

        # print(type(list(tree.keys())[0]))
        # print(tree)
        # print(dates_filters if 'dates_filters' in locals() else False, )
        # print(priorities_values)

        if len(list(tree.values())) > 0:
            isRecord = True
        else:
            isRecord = False

        # used for day2day analyzer
        if "provider" in requested_models:
            requested_models[requested_models.index("provider")] = "machineProvider" if data["analyze-type"][0] == "machine" else "materialProvider" if data["analyze-type"][0] == "material" else None

        context = {
            'context': True,
            'isRecord': isRecord,
            'analyzeType': data["analyze-type"][0],
            'onRent': True if data["analyze-type"][0]=="machine" and onRent else False,
            'priority_depths': priority_depth-1,
            'priorities_values': priorities_values,
            'priorityTypes': requested_models_persian,
            'query_formula': requested_models,
            'tree': tree,
            'dates_filters': dates_filters if 'dates_filters' in locals() else False,
        }
        return render(request, 'analyzer.html', context=context)


@login_required
def get_onOwn_id(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "GET":
        idd = MachineProvider.objects.get(
            name="شرکتی",
            project=project,
        ).id

    return HttpResponse(idd)


@login_required
def get_options_in_priority(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        priority = request.POST['priority']
        providerType = request.POST['providerType']

        if priority == "time":
            pass
            pass
        elif priority == "zone":
            objs = Zone.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "operation":
            objs = Operation.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "suboperation":
            objs = SubOperation.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "contractor":
            objs = Contractor.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "equipe":
            objs = Contractor.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "machine":
            objs = Machine.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "machineFamily":
            objs = MachineFamily.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "hardware":
            objs = Hardware.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "material":
            objs = Material.objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

        elif priority == "provider":
            dilemma = {
                "machine": MachineProvider,
                "material": MaterialProvider,
            }
            objs = dilemma[providerType].objects.filter(project=project)
            if objs.exists():
                objs = json.dumps(list(objs.values()))
            else:
                objs = "[]"
            context = {
                priority: objs,
            }

    return JsonResponse(context)


@login_required
def get_task_filters(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        data = dict(request.POST)
        model = data.get("model")[0].split("-")[1]
        items = data.get("items[]")

        if model == "contractor":
            if '0' in items:
                tasks = ParentTask.objects.filter(
                    project=project,
                    equipe__in=Equipe.objects.filter(project=project,
                                                     contractor__in=Contractor.objects.filter(project=project))
                )
                items = Contractor.objects.filter(project=project).values_list("name", flat=True)
            else:
                tasks = ParentTask.objects.filter(
                    project=project,
                    equipe__in=Equipe.objects.filter(project=project, contractor__in=Contractor.objects.filter(name__in=items, project=project))
                )
        elif model == "task":
            if '0' in items:
                tasks = ParentTask.objects.filter(
                    project=project,
                    operation__in=ZoneOperation.objects.filter(project=project,
                                                               operation__in=Operation.objects.filter(project=project)),
                )
                items = Operation.objects.filter(project=project).values_list("name", flat=True)
            else:
                tasks = ParentTask.objects.filter(
                    project=project,
                    operation__in=ZoneOperation.objects.filter(project=project, operation__in=Operation.objects.filter(project=project, name__in=items)),
                )

        data = {
            "model": model
        }

        for item in items:
            data[item] = []

        for task in tasks:
            if model == "task":
                if task.equipe.contractor.name not in data[task.operation.operation.name]:
                    # data[task.operation.operation.name].append(task.equipe.contractor.name)
                    data[task.operation.operation.name].append({
                        "target": task.equipe.contractor.name,
                        "zone": task.operation.zone.name,
                        "amount": task.operation.amount,
                        "unit": task.operation.unit.name,
                    })
            elif model == "contractor":
                if task.operation not in data[task.equipe.contractor.name]:
                    # data[task.equipe.contractor.name].append(task.operation.operation.name)
                    data[task.equipe.contractor.name].append({
                        "target": task.operation.operation.name,
                        "zone": task.operation.zone.name,
                        "amount": task.operation.amount,
                        "unit": task.operation.unit.name,
                    })

        return JsonResponse(data)


@login_required
def day2day_analyzer_machine(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        prio_1 = request.POST.get("prio_1")
        prio_2 = request.POST.get("prio_2")
        prio_3 = request.POST.get("prio_3")
        prio_4 = request.POST.get("prio_4")
        prio_5 = request.POST.get("prio_5")

        item_1 = request.POST.get("item_1")
        item_2 = request.POST.get("item_2")
        item_3 = request.POST.get("item_3")
        item_4 = request.POST.get("item_4")
        item_5 = request.POST.get("item_5")

        onRent = request.POST.get("onRent")
        onRent = True if onRent == "True" else False

        prios = [prio_1, prio_2, prio_3, prio_4, prio_5, ]
        items = [item_1, item_2, item_3, item_4, item_5, ]
        prios = [item for item in prios if item is not None and item != ""]
        items = [item for item in items if item is not None and item != ""]
        lower_date = request.POST.get("lower_date")
        upper_date = request.POST.get("upper_date")
        analyzeType = request.POST.get("analyzeType")

        if analyzeType == "machine":
            model = MODELS["MachineCount"]

        objs = model.objects.filter(project=project)
        objs = objs.filter(onRent=onRent)

        if lower_date and upper_date:
            reps = DailyReport.objects.filter(
                project=project,
                date__lt=jdatetime.datetime.strptime(upper_date, format="%Y/%m/%d").togregorian()+jdatetime.timedelta(days=1),
                date__gt=jdatetime.datetime.strptime(lower_date, format="%Y/%m/%d").togregorian(),
            )
            objs = objs.filter(
                dailyReport__in=reps,
            )
        if len(prios) > 1:
            data = {
                "onRent": onRent,
                "mode": "multiple",
                "model": "تجهیز",
                "item": None,
                "provider": None,
                "days": []
            }

            if "hardware" in prios:
                data["item"] = items[prios.index("hardware")]
            if "type" in prios:
                data["item"] = items[prios.index("type")]
            if "machine" in prios:
                data["item"] = items[prios.index("machine")]

            for i in range(len(prios)):
                q_filter = Q()
                if "machineProvider" == prios[i]:
                    q_filter |= Q(**{"provider": MODELS[prios[i]].objects.get(project=project, name=items[i])})
                    data["provider"] = items[i]
                else:
                    q_filter |= Q(**{f"{prios[i]}": MODELS[prios[i]].objects.get(project=project, name=items[i])})

                objs = objs.filter(q_filter)

            days = {}
            for obj in objs:
                if obj.dailyReport.date.strftime(format="%Y/%m/%d") not in days.keys():
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")] = {
                        "date": obj.dailyReport.date.strftime(format="%Y/%m/%d"),
                        "value": obj.workHours,
                        "activeCount": obj.activeCount,
                        "inactiveCount": obj.inactiveCount,
                        "totalCount": obj.totalCount,
                        "unit": "ساعت",
                    }
                else:
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["value"] += obj.workHours
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["activeCount"] += obj.activeCount
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["inactiveCount"] += obj.inactiveCount
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["totalCount"] += obj.totalCount

            data["days"] = list(days.values())

            return JsonResponse(data)

        elif len(prios) == 1:
            data = {
                "onRent": onRent,
                "mode": "single",
                "model": "تجهیز",
                "item": None,
                "provider": None,
                "days": []
            }

            if "hardware" in prios:
                data["item"] = items[prios.index("hardware")]
            if "type" in prios:
                data["item"] = items[prios.index("type")]
            if "machine" in prios:
                data["item"] = items[prios.index("machine")]

            q_filter = Q()
            if "machineProvider" == prios[0]:
                q_filter |= Q(**{"provider": MODELS[prios[0]].objects.get(project=project, name=items[0])})
                data["provider"] = items[0]
            else:
                q_filter |= Q(**{f"{prios[0]}": MODELS[prios[0]].objects.get(project=project, name=items[0])})

            objs = objs.filter(q_filter)

            days = {}
            for obj in objs:
                if obj.dailyReport.date.strftime(format="%Y/%m/%d") not in days.keys():
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")] = {
                        "date": obj.dailyReport.date.strftime(format="%Y/%m/%d"),
                        "value": obj.workHours,
                        "activeCount": obj.activeCount,
                        "inactiveCount": obj.inactiveCount,
                        "totalCount": obj.totalCount,
                        "unit": "ساعت",
                    }
                else:
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["value"] += obj.workHours
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["activeCount"] += obj.activeCount
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["inactiveCount"] += obj.inactiveCount
                    days[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["totalCount"] += obj.totalCount

            data["days"] = list(days.values())
            return JsonResponse(data)


@login_required
def day2day_analyzer_material(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        prio_1 = request.POST.get("prio_1")
        prio_2 = request.POST.get("prio_2")

        item_1 = request.POST.get("item_1")
        item_2 = request.POST.get("item_2")

        lower_date = request.POST.get("lower_date")
        upper_date = request.POST.get("upper_date")
        analyzeType = request.POST.get("analyzeType")

        if analyzeType == "machine":
            model = MODELS["MachineCount"]
        elif analyzeType == "material":
            model = MODELS["MaterialCount"]

        objs = model.objects.filter(project=project)

        if lower_date and upper_date:
            reps = DailyReport.objects.filter(
                project=project,
                date__lt=jdatetime.datetime.strptime(upper_date, format="%Y/%m/%d").togregorian()+jdatetime.timedelta(days=1),
                date__gt=jdatetime.datetime.strptime(lower_date, format="%Y/%m/%d").togregorian(),
            )
            objs = objs.filter(
                dailyReport__in=reps,
            )

        if prio_1 and prio_2:
            q_filter = Q()
            if "Provider" in prio_1:
                q_filter |= Q(**{"provider": MODELS[prio_1].objects.get(project=project, name=item_1)})
                provider = item_1
            else:
                q_filter |= Q(**{f"{prio_1}": MODELS[prio_1].objects.get(project=project, name=item_1)})
                item = item_1

            objs = objs.filter(q_filter)

            q_filter = Q()
            if "Provider" in prio_2:
                q_filter |= Q(**{"provider": MODELS[prio_2].objects.get(project=project, name=item_2)})
                provider = item_2
            else:
                q_filter |= Q(**{f"{prio_2}": MODELS[prio_2].objects.get(project=project, name=item_2)})
                item = item_2

            objs = objs.filter(q_filter)

            data = {
                "mode": "multiple",
                "model": "تجهیز" if analyzeType=="machine" else "مصالح" if analyzeType=="material" else None,
                "item": item,
                "provider": provider,
                "days": []
            }
            for obj in objs:
                temp = {
                    "date": obj.dailyReport.date.strftime(format="%Y/%m/%d"),
                    "value": obj.workHours if analyzeType=="machine" else obj.amount if analyzeType=="material" else None,
                    "unit": "ساعت" if analyzeType=="machine" else obj.unit.name if analyzeType=="material" else None,
                }
                data["days"].append(temp)

            return JsonResponse(data)

        elif prio_1:
            q_filter = Q()
            if "Provider" in prio_1:
                q_filter |= Q(**{"provider": MODELS[prio_1].objects.get(project=project, name=item_2)})
                provider = item_2
            else:
                q_filter |= Q(**{f"{prio_1}": MODELS[prio_1].objects.get(project=project, name=item_2)})
                provider = None
                item = item_2

            objs = objs.filter(q_filter)

            data = {
                "mode": "single",
                "model": "تجهیز" if analyzeType == "machine" else "مصالح" if analyzeType=="material" else None,
                "item": item,
                "provider": provider,
                "days": [],
            }
            trash = {}
            cached_dates = []
            for obj in objs:
                if obj.dailyReport.date.strftime(format="%Y/%m/%d") not in cached_dates:
                    if analyzeType == "machine":
                        temp = {
                            "date": obj.dailyReport.date.strftime(format="%Y/%m/%d"),
                            "value": obj.workHours,
                            "unit": "ساعت",
                        }
                    elif analyzeType == "material":
                        temp = {
                            "date": obj.dailyReport.date.strftime(format="%Y/%m/%d"),
                            "value":  obj.amount*obj.unit.coef,
                            "unit": obj.unit.parent.name if obj.unit.parent else obj.unit.name,
                        }

                    trash[obj.dailyReport.date.strftime(format="%Y/%m/%d")] = temp
                    cached_dates.append(obj.dailyReport.date.strftime(format="%Y/%m/%d"))

                else:
                    if analyzeType == "machine":
                        trash[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["value"] += obj.workHours
                    elif analyzeType == "material":
                        trash[obj.dailyReport.date.strftime(format="%Y/%m/%d")]["value"] += obj.amount*obj.unit.coef

            data["days"] = list(trash.values())

            return JsonResponse(data)

