from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.core import serializers

from .models import *
from .converters import *
import jdatetime
import json


# TODO : Bug Fix ; error raises for adding already existing objects to base data


def home(request):
    return render(request, "base.html")


def add_base_data_template(request):
    professions = Profession.objects.all()
    positions = Position.objects.all()
    machines = Machine.objects.all()
    materials = Material.objects.all()
    contractors = Contractor.objects.all()
    equipes = Equipe.objects.all()
    zones = Zone.objects.all()
    tasks = Task.objects.all()
    units = Unit.objects.all()

    materialproviders = MaterialProvider.objects.all()
    machineproviders = MachineProvider.objects.all()

    operations = Operation.objects.all()
    suboperations = SubOperation.objects.all()



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
        "positions": positions,
        "professions": professions,
        "machines": machines,
        "materials": materials,
        "contractors": contractors,
        "equipes": equipes,
        "zones": zones,
        "tasks": tasks,
        "units": units,
        "materialproviders": materialproviders,
        "machineproviders": machineproviders,
        "operations": operations,
        "suboperations": suboperations,

        "machine_types": MACHINE_TYPES,
    }

    return render(request, "modify-base-data.html", context=context)


def operation_break_template(request):
    operations = Operation.objects.all()
    units = Unit.objects.all()

    if not operations.exists():
        operations = []
    if not units.exists():
        units = []

    context = {
        "operations": operations,
        "units": units,
    }

    return render(request, "operation-breaks.html", context=context)


def create_report_template(request):
    if DailyReport.objects.all().count() == 0:
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
        context = {}

    else:
        report = DailyReport.objects.last()
        positions = PositionCount.objects.filter(dailyReport=report)
        professions = ProfessionCount.objects.filter(dailyReport=report)
        machines = MachineCount.objects.filter(dailyReport=report)
        materials = MaterialCount.objects.filter(dailyReport=report)
        equipes = EquipeCount.objects.filter(dailyReport=report)
        units = Unit.objects.all()
        materialproviders = MaterialProvider.objects.all()
        machineproviders = MachineProvider.objects.all()
        tasks = TaskReport.objects.filter(dailyReport=report)

        other = {
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
            "units": units,
            "materialproviders": materialproviders,
            "machineproviders": machineproviders,
            "tasks": tasks,
            "machine_types": MACHINE_TYPES,
            "other": other,
        }

    return render(request, "daily-report.html", context=context)


def add_position_to_db(request):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        position = request.POST.get("position")

        new_position = Position.objects.create(name=position)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_unit_to_db(request):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        unit = request.POST.get("unit")
        new_unit = Unit.objects.create(name=unit)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_materialprovider_to_db(request):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        materialprovider = request.POST.get("materialprovider")

        new_materialprovider = MaterialProvider.objects.create(name=materialprovider)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_machineprovider_to_db(request):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machineprovider = request.POST.get("machineprovider")

        new_machineprovider = MachineProvider.objects.create(name=machineprovider)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_machine_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machine = request.POST.get("machine")
        type = request.POST.get("machineType")

        new_machine = Machine.objects.create(name=machine, type=type)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_material_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        material = request.POST.get("material")
        # type = request.POST.get("machineType")

        new_material = Material.objects.create(name=material)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_profession_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        profession = request.POST.get("profession")

        new_profession = Profession.objects.create(name=profession)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_contractor_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        contractor = request.POST.get("contractor")

        new_contractor = Contractor.objects.create(name=contractor)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_zone_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        zone = request.POST.get("zone")

        new_zone = Zone.objects.create(name=zone)

        return JsonResponse(True, safe=False)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_task_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')

        operation = request.POST.get("operation")
        suboperation = request.POST.get("suboperation")
        zoneName = request.POST.get("zoneoperation")
        equipeName = request.POST.get("equipe")
        taskVol = request.POST.get("task-volume")
        unitName = request.POST.get("unit")

        zoneoperation = ZoneOperation.objects.get(
                operation=Operation.objects.get(name=operation),
                zone=Zone.objects.get(name=zoneName),
        )
        # try:
        new_task, new = Task.objects.get_or_create(
            operation=zoneoperation,
            suboperation=SubOperation.objects.get(
                name=suboperation,
                parent=Operation.objects.get(name=operation),
            ),
            equipe=Equipe.objects.get(name=equipeName),
            zone=Zone.objects.get(name=zoneName),

            defaults= {
                'totalVolume': float(taskVol),
                'unit': Unit.objects.get(name=unitName),
            }
        )

        if not new:
            return JsonResponse(False, safe=False)

        new_task.set_unique()
        new_task.update_percentage()

        zoneoperation.tasks.add(new_task)
        zoneoperation.update_assignedAmount()



        return JsonResponse(True, safe=False)
            # return redirect(redirect_url)

        # except:
        #     return HttpResponse(False)

    elif request.method == "GET":
        pass

        return HttpResponse("Problem")


def add_equipe_to_db(request,):
    if request.method == "POST":
        # redirect_url = request.META.get('HTTP_REFERER', '/')
        prof = request.POST.get("profession")
        cont = request.POST.get("contractor")

        prof = Profession.objects.get(name=prof)
        cont = Contractor.objects.get(name=cont)

        # TODO : Make line below get_or_create
        obj , new = Equipe.objects.get_or_create(
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
            return JsonResponse(False, safe=False)
        # return redirect(to=redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def shortcut_add(request,):
    if request.method == "POST":
        which = request.POST.get("which")
        value = request.POST.get("value")
        type = request.POST.get("type")

        if which == "position":
            new_obj = Position.objects.create(name=value)
        elif which == "profession":
            new_obj = Profession.objects.create(name=value)
        elif which == "machine":
            new_obj = Machine.objects.create(name=value, type=type)
        elif which == "material":
            new_obj = Material.objects.create(name=value)
        elif which == "contractor":
            new_obj = Contractor.objects.create(name=value)
        elif which == "zone":
            new_obj = Zone.objects.create(name=value)
        elif which == "unit":
            new_obj = Unit.objects.create(name=value)
        elif which == "materialprovider":
            new_obj = MaterialProvider.objects.create(name=value)
        elif which == "machineprovider":
            new_obj = MachineProvider.objects.create(name=value)

        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(False)


def del_position_from_db(request):
    if request.method == "POST":
        name = request.POST.get("position")
        obj = Position.objects.get(name=name)
        objCount = PositionCount.objects.filter(position=obj.id)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_profession_from_db(request):
    if request.method == "POST":
        name = request.POST.get("profession")
        obj = Profession.objects.get(name=name)
        objCount = PositionCount.objects.filter(position=obj.id)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_machine_from_db(request):
    if request.method == "POST":
        name = request.POST.get("machine")
        obj = Machine.objects.get(name=name)
        objCount = MachineCount.objects.filter(machine=obj.id)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_material_from_db(request):
    if request.method == "POST":
        name = request.POST.get("material")
        obj = Material.objects.get(name=name)
        objCount = MaterialCount.objects.filter(material=obj.id)
        obj.delete()
        objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_contractor_from_db(request):
    if request.method == "POST":
        name = request.POST.get("contractor")
        obj = Contractor.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_zone_from_db(request):
    if request.method == "POST":
        name = request.POST.get("zone")
        obj = Zone.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_unit_from_db(request):
    if request.method == "POST":
        name = request.POST.get("unit")
        obj = Unit.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_operation_from_db(request):
    if request.method == "POST":
        name = request.POST.get("operation")

        obj = Operation.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_suboperation_from_db(request):
    if request.method == "POST":
        suboperation = request.POST.get("suboperation")
        operation = request.POST.get("operation")
        obj = SubOperation.objects.get(name=suboperation, parent=operation)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        Operation.objects.get(id=operation).update_assignedWeight()
        # objCount.delete()
        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_zoneoperation_from_db(request):
    if request.method == "POST":
        zone = request.POST.get("zoneoperation")
        zone = Zone.objects.get(name=zone)

        operation = request.POST.get("operation")

        obj = ZoneOperation.objects.get(zone=zone, operation=operation)
        obj.delete()

        Operation.objects.get(id=operation).update_assignedAmount()

        return HttpResponse(True)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def add_suboperation_to_db(request):
    if request.method == "POST":
        operation_id = request.POST.get("operation-id")
        name = request.POST.get("name")
        unit_name = request.POST.get("unit").strip()
        amount = request.POST.get("amount")
        weight = request.POST.get("weight")

        operation = Operation.objects.get(id=operation_id)
        unit = Unit.objects.get(name=unit_name)

        new_obj = SubOperation.objects.create(
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


def add_operation_to_db(request):
    if request.method == "POST":
        name = request.POST.get("operation")
        unit_name = request.POST.get("unit-name").strip()
        amount = request.POST.get("amount")

        operation = Operation.objects.create(
            name=name,
            unit=Unit.objects.get(name=unit_name),
            amount=amount,
        )
        operation.update_assignedWeight()
        operation.update_assignedAmount()


        return HttpResponse(operation.id)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def add_zoneoperation_to_db(request):
    if request.method == "POST":
        operation_id = request.POST.get("operation-id")
        zone = request.POST.get("zone").strip()
        amount = request.POST.get("amount")

        operation = Operation.objects.get(id=operation_id)

        zone_operation = ZoneOperation.objects.create(
            operation=operation,
            zone=Zone.objects.get(name=zone),
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


def del_materialprovider_from_db(request):
    if request.method == "POST":
        name = request.POST.get("materialprovider")
        obj = MaterialProvider.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_machineprovider_from_db(request):
    if request.method == "POST":
        name = request.POST.get("machineprovider")
        obj = MachineProvider.objects.get(name=name)
        # objCount = .objects.filter(material=obj.id)
        obj.delete()
        # objCount.delete()
        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_equipe_from_db(request):
    if request.method == "POST":
        prof = request.POST.get("profession")
        cont = request.POST.get("contractor")

        obj = Equipe.objects.filter(
            profession=Profession.objects.get(name=prof),
            contractor=Contractor.objects.get(name=cont),
        )
        obj.delete()

        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def del_task_from_db(request):
    if request.method == "POST":
        taskOperation = request.POST.get("taskOperation")
        taskSubOperation = request.POST.get("taskSubOperation")
        equipeName = request.POST.get("equipeName")
        # taskVol = request.POST.get("taskVol")
        zoneName = request.POST.get("zoneName")
        # unitName = request.POST.get("unitName")

        operation = Operation.objects.get(name=taskOperation)
        zoneoperation = ZoneOperation.objects.get(
            operation=operation,
            zone=Zone.objects.get(name=zoneName),
        )

        obj = Task.objects.filter(
            operation=zoneoperation.id,
            suboperation=SubOperation.objects.get(
                name=taskSubOperation,
                parent=Operation.objects.get(name=taskOperation),
            ),
            equipe=Equipe.objects.get(name=equipeName),
            zone=Zone.objects.get(name=zoneName),
        )
        obj.delete()

        zoneoperation.update_assignedAmount()
        zoneoperation.update_doneAmount()

        operation.update_doneAmount()

        return HttpResponse(1)

    elif request.method == "GET":
        pass

    return HttpResponse(-1)


def save_daily_report_to_db(request):
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
                pos = Position.objects.get(name=position)
                obj = PositionCount.objects.create(
                    position=pos,
                    dailyReport=report,
                    count=count,
                )
                report.positions.add(obj.position)
            else:
                continue

        for profession, count in professions.items():
            if sum(count) > 0:
                prof = Profession.objects.get(name=profession)
                obj = ProfessionCount.objects.create(
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
                mach = Machine.objects.get(name=machine)
                provider = MachineProvider.objects.get(name=count[3])
                obj = MachineCount.objects.create(
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

                mat = Material.objects.get(name=material)
                unit = Unit.objects.get(name=amount[1])
                materialprovider = MaterialProvider.objects.get(name=amount[2])
                obj = MaterialCount.objects.create(
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
                cont = Contractor.objects.get(name=contractor)
                obj = ContractorCount.objects.create(
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
                    profession=Profession.objects.get(name=prof),
                    contractor=Contractor.objects.get(name=cont),
                )
                obj = EquipeCount.objects.create(
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
                tsk = Task.objects.get(unique_str=task)

                if not tsk.started:
                    tsk.start(date=report.date)

                parent = TaskReport.objects.filter(task=tsk).last()
                tsk_rep = TaskReport.objects.create(
                    task=tsk,
                    parent=parent,
                    dailyReport=report,
                    todayVolume=amount,
                )
                tsk_rep.update_percentage(False, date=report.date)
                report.tasks.add(tsk_rep.task)

        report.cal_countPeople()
        report.cal_countMachines()

        return redirect(to="/home/daily-reports")
    else:
        return -1


def del_daily_report_from_db(request):
    if request.method == "POST":
        rep = DailyReport.objects.get(id=request.POST["id"])

        if rep.deletable:
            for item in rep.taskreport_set.all():
                item.update_percentage(True, date=rep.date)
            rep.delete()
            return redirect(to="/home/daily-reports")
        else:
            raise PermissionDenied
    else:
        return -1


def edit_daily_report_in_db(request):
    if request.method == "POST":
        if request.POST.get("template"):
            report = DailyReport.objects.get(id=request.POST["id"])

            if report.editable:

                positions = PositionCount.objects.filter(dailyReport=report)
                professions = ProfessionCount.objects.filter(dailyReport=report)
                machines = MachineCount.objects.filter(dailyReport=report)
                materials = MaterialCount.objects.filter(dailyReport=report)
                equipes = EquipeCount.objects.filter(dailyReport=report)
                units = Unit.objects.all()
                materialproviders = MaterialProvider.objects.all()
                machineproviders = MachineProvider.objects.all()
                tasks = TaskReport.objects.filter(dailyReport=report)

                other = {
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


            report = DailyReport.objects.get(id=request.POST.get("report_id"))
            ID = report.id
            DATE_CREATED = report.date_created

            if report.deletable and report.editable:
                for item in report.taskreport_set.all():
                    item.update_percentage(True, date=report.date)
                report.delete()
            else:
                raise PermissionDenied

            report = DailyReport.objects.create(
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
                    pos = Position.objects.get(name=position)
                    obj = PositionCount.objects.create(
                        position=pos,
                        dailyReport=report,
                        count=count,
                    )
                    report.positions.add(obj.position)
                else:
                    continue

            for profession, count in professions.items():
                if sum(count) > 0:
                    prof = Profession.objects.get(name=profession)
                    obj = ProfessionCount.objects.create(
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
                    mach = Machine.objects.get(name=machine)
                    provider = MachineProvider.objects.get(name=count[3])
                    obj = MachineCount.objects.create(
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

                    mat = Material.objects.get(name=material)
                    unit = Unit.objects.get(name=amount[1])
                    materialprovider = MaterialProvider.objects.get(name=amount[2])
                    obj = MaterialCount.objects.create(
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
                    cont = Contractor.objects.get(name=contractor)
                    obj = ContractorCount.objects.create(
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
                        profession=Profession.objects.get(name=prof),
                        contractor=Contractor.objects.get(name=cont),
                    )
                    obj = EquipeCount.objects.create(
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
                    tsk = Task.objects.get(unique_str=task)

                    if not tsk.started:
                        tsk.start(date=report.date)

                    parent = TaskReport.objects.filter(task=tsk).last()
                    tsk_rep = TaskReport.objects.create(
                        task=tsk,
                        parent=parent,
                        dailyReport=report,
                        todayVolume=amount,
                    )
                    tsk_rep.update_percentage(False, date=report.date)
                    report.tasks.add(tsk_rep.task)

            report.cal_countPeople()
            report.cal_countMachines()

            return redirect(to="/home/daily-reports")


def reports_daily(request):
    reports = DailyReport.objects.all()
    for report in reports:
        report.check_deletability()

    context = {
        "reports": reports,
    }

    return render(request, "reports-list.html", context=context)


def report_on_day(request, idd):
    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd)

    positions = PositionCount.objects.filter(dailyReport=report)
    professions = ProfessionCount.objects.filter(dailyReport=report)
    machines = MachineCount.objects.filter(dailyReport=report)
    materials = MaterialCount.objects.filter(dailyReport=report)
    equipes = EquipeCount.objects.filter(dailyReport=report)
    tasks = TaskReport.objects.filter(dailyReport=report)

    done_task_zone = []

    for task in tasks:
        ids = Equipe.objects.filter(profession=task.task.equipe.profession).values_list('id', flat=True)
        objs = Task.objects.filter(equipe__id__in=ids)
        entire_item_vol = 0
        entire_item_done = 0
        for obj in objs:
            entire_item_vol += obj.totalVolume
            entire_item_done += obj.doneVolume

        done_task_zone.append([task.id, entire_item_done / entire_item_vol * 100, entire_item_vol])


    other = {
        "weather": report.get_weather_display(),
        "weekday": report.get_weekday_display(),
        "date": report.date.strftime('%Y/%m/%d'),
        "entire_items": done_task_zone,
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


def compact_report_on_day(request, idd):
    # report = DailyReport.objects.get(id=idd)
    report = get_object_or_404(DailyReport, pk=idd)

    positions = PositionCount.objects.filter(dailyReport=report)
    professions = ProfessionCount.objects.filter(dailyReport=report)
    machines = MachineCount.objects.filter(dailyReport=report)
    materials = MaterialCount.objects.filter(dailyReport=report)
    equipes = EquipeCount.objects.filter(dailyReport=report)
    tasks = TaskReport.objects.filter(dailyReport=report)
    # tasks = TaskReport.objects.all()

    # done_task_zone = []

    tsks = {}
    for task in tasks:
        if task.task.equipe.profession in tsks.keys():
            tsks[task.task.equipe.profession]['todayVolume'] += task.todayVolume
            tsks[task.task.equipe.profession]['preDoneVolume'] += task.preDoneVolume
            tsks[task.task.equipe.profession]['entire_item_vol'] += task.task.totalVolume
            tsks[task.task.equipe.profession]['entire_item_done'] += task.task.doneVolume

            tsks[task.task.equipe.profession]['entire_item_done_percent'] = tsks[task.task.equipe.profession]['entire_item_done']/tsks[task.task.equipe.profession]['entire_item_vol']*100

        else:
            tsks[task.task.equipe.profession] = {
                'name': task.task.equipe.profession,
                'todayVolume': task.todayVolume,
                'preDoneVolume': task.preDoneVolume,
                'entire_item_vol': task.task.totalVolume,
                'entire_item_done': task.task.doneVolume,
                'entire_item_done_percent': 0.0,
                'unit': task.task.unit,
            }

    # for task in tasks:
    #     ids = Equipe.objects.filter(profession=task.task.equipe.profession).values_list('id', flat=True)
    #     objs = Task.objects.filter(equipe__id__in=ids)
    #     entire_item_vol = 0
    #     entire_item_done = 0
    #     for obj in objs:
    #         entire_item_vol += obj.totalVolume
    #         entire_item_done += obj.doneVolume
    #
    #     done_task_zone.append([task.id, entire_item_done/entire_item_vol*100, entire_item_vol])


    other = {
        "weather": report.get_weather_display(),
        "weekday": report.get_weekday_display(),
        "date": report.date.strftime('%Y/%m/%d'),
        # "entire_items": done_task_zone,
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


def get_options(request, typee):
    if request.method == "POST":
        data = json.loads(request.POST['options'])["options"]
        data = [item.strip().strip() for item in data]
        if "equipe" in typee:
            data = [f"{item.strip().split('-')[0].strip()}-{item.split('-')[-1].strip()}" for item in data]
        else:
            pass
        if typee == "profession":
            data = Profession.objects.exclude(name__in=data).all()
        elif "provider" in typee:
            if "machineprovider" == typee:
                data = MachineProvider.objects.all()
            elif "materialprovider" == typee:
                data = MaterialProvider.objects.all()
        elif typee == "unit":
            data = Unit.objects.exclude(name__in=data).all()
        elif typee == "position":
            data = Position.objects.exclude(name__in=data).all()
        elif typee == "machine":
            data = Machine.objects.exclude(name__in=data).all()
        elif typee == "material":
            data = Material.objects.exclude(name__in=data).all()
        elif typee == "contractor":
            data = Contractor.objects.exclude(name__in=data).all()
        elif typee == "task":
            data = Equipe.objects.exclude(name__in=data).all()
        elif typee == "zone":
            data = Zone.objects.exclude(name__in=data).all()
        elif typee == "equipe":
            data = Equipe.objects.exclude(name__in=data).all()
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


def get_tasks(request,):
    if request.method == "POST":
        data = json.loads(request.POST['options'])["options"]
        # data = [item.strip().split("-") for item in data]
        data = list(
            map(
                lambda x: "".join([x[0].strip(), "-", x[1].strip(), "-", x[2].strip(), "-", x[3].strip()]),
                [item.strip().split("-") for item in data]
            )
        )
        data = Task.objects.exclude(unique_str__in=data).all()
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


def get_task(request,):
    if request.method == "POST":
        name, prof, cont, zone = [item.strip() for item in request.POST['options'].split("-")]

        item = Task.objects.filter(
            name=name,
            zone=Zone.objects.get(name=zone),
            equipe=Equipe.objects.get(name=f"{prof}-{cont}"),
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


def get_units(request):
    if request.method == "GET":
        units = Unit.objects.all()
        if units.exists():
            data = json.dumps(list(units.values()))
        else:
            data = "[]"
        context = {
            "units": data
        }
        return JsonResponse(context)


def get_operations(request):
    if request.method == "GET":
        operations = Operation.objects.all()
        if operations.exists():
            data = json.dumps(list(operations.values()))
        else:
            data = "[]"
        context = {
            "operations": data
        }
        return JsonResponse(context)


def get_suboperations(request):
    if request.method == "GET":
        opr_name = request.GET.get("operation")
        suboperations = SubOperation.objects.filter(
            parent=Operation.objects.get(name=opr_name)
        )
        if suboperations.exists():
            data = json.dumps(list(suboperations.values()))
        else:
            data = "[]"
        context = {
            "suboperations": data
        }
        return JsonResponse(context)


def get_zoneoperations(request):
    if request.method == "GET":
        opr_name = request.GET.get("operation")
        operation = Operation.objects.get(name=opr_name)
        zoneoperations = operation.zones.all()
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


def get_all_equipes(request):
    if request.method == "GET":
        equipes = Equipe.objects.all()
        if equipes.exists():
            data = json.dumps(list(equipes.values()))
        else:
            data = "[]"
        context = {
            "equipes": data
        }
        return JsonResponse(context)


def get_freeAmount(request):
    if request.method == "GET":
        model = request.GET.get('model')
        if model == "zoneoperation":
            operation = request.GET.get('operation')
            zone = request.GET.get('zone')

            zoneoperation = ZoneOperation.objects.get(
                operation=Operation.objects.get(name=operation,),
                zone=Zone.objects.get(name=zone,),
            )
            freeAmount = zoneoperation.freeAmount

            return HttpResponse(freeAmount)


def get_zones(request):
    if request.method == "GET":
        zones = Zone.objects.all()
        if zones.exists():
            data = json.dumps(list(zones.values()))
        else:
            data = "[]"
        context = {
            "zones": data
        }
        return JsonResponse(context)


def get_materialproviders(request):
    if request.method == "GET":
        materialproviders = MaterialProvider.objects.all()
        if materialproviders.exists():
            data = json.dumps(list(materialproviders.values()))
        else:
            data = "[]"
        context = {
            "materialproviders": data
        }
        return JsonResponse(context)


def get_machineproviders(request):
    if request.method == "GET":
        machineproviders = MachineProvider.objects.all()
        if machineproviders.exists():
            data = json.dumps(list(machineproviders.values()))
        else:
            data = "[]"
        context = {
            "machineproviders": data
        }
        return JsonResponse(context)


def check_deletability(request):
    if request.method == "POST":
        idd = request.POST['id']
        rep = DailyReport.objects.get(id=idd)

        return HttpResponse(rep.deletable)


def check_editability(request):
    if request.method == "POST":
        idd = request.POST['id']
        rep = DailyReport.objects.get(id=idd)

        return HttpResponse(rep.editable)


def check_dailyreport_existence(request):
    if request.method == "POST":

        date = request.POST.get("date")
        date, time = date.split(" ")
        date = date.replace("/", "-")

        report = get_object_or_404(DailyReport, short_date=date)
        if report:
            return HttpResponse(True)

        # ("%Y-%m-%d %H:%M:%S")
