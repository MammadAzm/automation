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
    machines = Machine.objects.filter(project=project)
    materials = Material.objects.filter(project=project)
    contractors = Contractor.objects.filter(project=project)
    equipes = Equipe.objects.filter(project=project)
    zones = Zone.objects.filter(project=project)
    tasks = Task.objects.filter(project=project)
    parentTasks = ParentTask.objects.filter(project=project)
    units = Unit.objects.filter(project=project).order_by('parent', 'name')

    materialproviders = MaterialProvider.objects.filter(project=project)
    machineproviders = MachineProvider.objects.filter(project=project)

    operations = Operation.objects.filter(project=project)
    suboperations = SubOperation.objects.filter(project=project)

    if not professions.exists():
        professions = []
    if not positions.exists():
        positions = []
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
    if not operations.exists():
        operations = []
    if not suboperations.exists():
        suboperations = []

    context = {
        "project": project,
        "positions": positions,
        "professions": professions,
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
        "operations": operations,
        "suboperations": suboperations,

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
            if amount and float(amount) != float(object.amount):
                object.amount = amount
                for task in Task.objects.filter(suboperation=object, project=project):
                    task.totalVolume = (float(task.parent.totalVolume)/float(operation.amount))*float(object.amount)
                    task.save()
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

            "machine_types": MACHINE_TYPES,
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
def add_machine_to_db(request,):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machine = request.POST.get("machine")
        type = request.POST.get("machineType")

        new_machine = Machine.objects.create(name=machine, type=type, project=project)

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
def del_machine_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        name = request.POST.get("machine")
        obj = Machine.objects.get(name=name, project=project)
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

    # TODO : Modify this service usage in the front-side to be called through AJAX Request
    if request.method == "POST":
        data = dict(request.POST)

        positions = {}
        professions = {}
        machines = {}
        materials = {}
        equipes = {}
        contractors = {}
        tasks = {}

        # print(data.items())
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
            if count[0] > 0 or count[1] > 0:
                machine = machine.strip()
                # machine = machine.split("-")[1].strip()
                mach = Machine.objects.get(name=machine, project=project)
                provider = MachineProvider.objects.get(name=count[3], project=project)
                obj = MachineCount.objects.create(
                    project=project,
                    machine=mach,
                    dailyReport=report,
                    activeCount=count[1],
                    inactiveCount=count[2],
                    workHours=count[0],
                    provider=provider,
                    totalCount=sum(count[1:3]),
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

        return redirect(to="/home/daily-reports")
    else:
        return -1


@login_required
def del_daily_report_from_db(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        rep = DailyReport.objects.get(id=request.POST["id"], project=project)

        if rep.deletable:
            for item in rep.taskreport_set.all():
                item.update_percentage(True, date=rep.date)
            rep.delete()
            return redirect(to="/home/daily-reports")
        else:
            raise PermissionDenied
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
                date=jdatetime.datetime.strptime(data['date'][0], format="%Y/%m/%d").strftime(
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
                if count[0] > 0 or count[1] > 0:
                    machine = machine.strip()
                    # machine = machine.split("-")[1].strip()
                    mach = Machine.objects.get(name=machine, project=project)
                    provider = MachineProvider.objects.get(name=count[3], project=project)
                    obj = MachineCount.objects.create(
                        project=project,
                        machine=mach,
                        dailyReport=report,
                        activeCount=count[1],
                        inactiveCount=count[2],
                        workHours=count[0],
                        provider=provider,
                        totalCount=sum(count[1:3]),
                    )
                    report.machines.add(obj.machine)

                else:
                    continue

            for material, amount in materials.items():
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

            return redirect(to="/home/daily-reports")


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
            parentTaskPercents[task.task.parent.id] += (task.preDoneVolume / task.task.totalVolume * 100 + task.todayVolume / task.task.totalVolume * 100) * task.task.suboperation.weight / 100
        else:
            parentTaskPercents[task.task.parent.id] = (task.preDoneVolume/task.task.totalVolume*100 + task.todayVolume/task.task.totalVolume*100)*task.task.suboperation.weight/100

    # [item for item in parentTaskPercents.items()]

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

    history = TaskReport.objects.filter(operation_id__in=operation_ids, created_at__lt=report.created_at, project=project)
    history = history.exclude(id__in=tasks.values('id'), project=project)

    tsks = {}
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

    for key, value in tsks.items():
        tsks[key]['entire_item_done'] = tsks[key]['todayVolume'] + tsks[key]['preDoneVolume']
        tsks[key]['entire_item_done_percent'] = tsks[key]['entire_item_done'] / tsks[key]['entire_item_vol'] * 100

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
        opr_name = request.GET.get("operation", project=project)
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
            'start_date': subtask.start_date,
            'completion_date': subtask.completion_date,
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
            zone = request.GET.get('zone')
            zoneoperation = ZoneOperation.objects.get(
                project=project,
                operation=Operation.objects.get(name=operation, project=project),
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


def group_queryset(queryset, pivot_fields, target, analyzeType):
    if not pivot_fields:
        return list(queryset)
    pivot_field = pivot_fields[0]

    grouped_results = {}
    for key, group in groupby(queryset, key=lambda obj: getattr(obj, pivot_field)):

        # Recursively group the remaining queryset for the next pivot fields
        nested_results = group_queryset(group, pivot_fields[1:], target, analyzeType=analyzeType)

        if type(nested_results) is list:
            if analyzeType == "Ahjam":
                data = {
                    "totalVolume": 0,
                    "doneVolume": 0,
                    "donePercentage": 0,
                    "unit":"unit",
                }
                finalAttribute = "TOTALVOLUME"
            elif analyzeType == "machine":
                data = {
                    "workHours": 0,
                    "unit": "ساعت",
                }
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

    return grouped_results


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

        query = {
            "operation": None,
            "zone": None,
            "contractor": None,
            "machine": None,
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
            tree = group_queryset(taskReports, requested_models, target=target, analyzeType=data["analyze-type"][0])

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

            if "machine" not in query_formula:
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
                    project=project,
                    date__lt=jdatetime.datetime.strptime(query["upper-date"], format="%Y-%m-%d").togregorian(),
                    date__gt=jdatetime.datetime.strptime(query["lower-date"], format="%Y-%m-%d").togregorian(),
                )
                # print(">>>", type(query["lower-date"]), query["lower-date"])
                dates_filters = {
                    "lower": query["lower-date-jalali"].replace("-", "/"),
                    "upper": query["upper-date-jalali"].replace("-", "/"),
                }

            requested_models.append("dailyReportMachine")
            requested_instances["dailyReportMachine"] = dailyReports.values_list("id", flat=True)

            machineCounts = MachineCount.objects.filter(project=project)

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
            requested_models.remove("dailyReportMachine")
            machineCounts = machineCounts.order_by(*requested_models)
            target = MachineCount
            # target = findOutputTarget(requested_models)
            tree = group_queryset(machineCounts, requested_models, target=target, analyzeType=data["analyze-type"][0])

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
                    project=project,
                    date__lt=jdatetime.datetime.strptime(query["upper-date"], format="%Y-%m-%d").togregorian(),
                    date__gt=jdatetime.datetime.strptime(query["lower-date"], format="%Y-%m-%d").togregorian(),
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
            tree = group_queryset(materialCounts, requested_models, target=target, analyzeType=data["analyze-type"][0])

        # print(type(list(tree.keys())[0]))
        # print(tree)
        # print(dates_filters if 'dates_filters' in locals() else False, )
        # print(priorities_values)

        if len(list(tree.values())) > 0:
            isRecord = True
        else:
            isRecord = False
        context = {
            'context': True,
            'isRecord': isRecord,
            'analyzeType': data["analyze-type"][0],
            'priority_depths': priority_depth-1,
            'priorities_values': priorities_values,
            'priorityTypes': requested_models_persian,
            'tree': tree,
            'dates_filters': dates_filters if 'dates_filters' in locals() else False,
        }
        return render(request, 'analyzer.html', context=context)


@login_required
def get_options_in_priority(request):
    user = MyUser.objects.get(user=request.user)
    project = user.projects.all()[0]

    if request.method == "POST":
        priority = request.POST['priority']
        providerType = request.POST['providerType']
        if priority == "time":
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
