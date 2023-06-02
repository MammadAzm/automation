from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from .models import *
from .converters import *
import jdatetime
import json
# Create your views here.


# TODO : Bug Fix ; error raises for adding already existing objects


def home(request):
    return render(request, "base.html")


def add_base_data_template(request):
    professions = Profession.objects.all()
    positions = Position.objects.all()
    machines = Machine.objects.all()
    materials = Material.objects.all()
    contractors = Contractor.objects.all()
    equipes = Equipe.objects.all()

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

    context = {
        "positions": positions,
        "professions": professions,
        "machines": machines,
        "materials": materials,
        "contractors": contractors,
        "equipes": equipes,
        "machine_types": MACHINE_TYPES,
    }

    return render(request, "modify-base-data.html", context=context)


def create_report_template(request):

    if DailyReport.objects.all().count() == 0:
        positions = Position.objects.all()
        professions = Profession.objects.all()
        machines = Machine.objects.all()
        materials = Material.objects.all()
        equipes = Equipe.objects.all()
        units = Unit.objects.all()

        context = {
            "positions": positions,
            "professions": professions,
            "machines": machines,
            "materials": materials,
            "equipes": equipes,
            "units": units,
            "machine_types": MACHINE_TYPES,
        }
    else:

        report = DailyReport.objects.last()
        positions = PositionCount.objects.filter(dailyReport=report)
        professions = ProfessionCount.objects.filter(dailyReport=report)
        machines = MachineCount.objects.filter(dailyReport=report)
        materials = MaterialCount.objects.filter(dailyReport=report)
        equipes = EquipeCount.objects.filter(dailyReport=report)
        units = Unit.objects.all()

        context = {
            "positions": positions,
            "professions": professions,
            "machines": machines,
            "materials": materials,
            "equipes": equipes,
            "units": units,
            "machine_types": MACHINE_TYPES,
        }

    return render(request, "daily-report.html", context=context)


def add_position_to_db(request):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        position = request.POST.get("position")

        new_position = Position.objects.create(name=position)

        return redirect(redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_machine_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        machine = request.POST.get("machine")
        type = request.POST.get("machineType")

        new_machine = Machine.objects.create(name=machine, type=type)

        return redirect(redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_material_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        material = request.POST.get("material")
        # type = request.POST.get("machineType")

        new_material = Material.objects.create(name=material)

        return redirect(redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_profession_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        profession = request.POST.get("profession")

        new_profession = Profession.objects.create(name=profession)

        return redirect(redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


def add_contractor_to_db(request,):
    if request.method == "POST":
        redirect_url = request.META.get('HTTP_REFERER', '/')
        contractor = request.POST.get("contractor")

        new_contractor = Contractor.objects.create(name=contractor)

        return redirect(redirect_url)

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
        print("HERE")
        obj = Equipe.objects.create(
            profession=prof,
            contractor=cont,
        )

        obj.set_name()
        obj.save()

        return HttpResponse(True)
        # return redirect(to=redirect_url)

    elif request.method == "GET":
        pass

    return HttpResponse("Problem")


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


def save_daily_report_to_db(request):
    if request.method == "POST":
        data = dict(request.POST)

        positions = {}
        professions = {}
        machines = {}
        materials = {}
        equipes = {}
        contractors = {}

        print(data)

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
                    machines[key.split("_")[1]].append(int(value[0]))
                else:
                    machines[key.split("_")[1]] = []
                    machines[key.split("_")[1]].append(int(value[0]))
            elif "material" in key:
                if "count" in key:
                    materials[key.split("_")[1]] = [float(value[0]), None]
                elif "unit" in key:
                    materials[key.split("_")[1]][1] = value[0]

        # print(positions)
        # print(professions)
        # print(machines)
        # print(materials)
        # print(equipes)
        # print(contractors)

        report = DailyReport.objects.create(
            project_name="پروژه آلفا",
            employer="کارفرما",
            employee="پیمانکار",
            contract_number="123456789",
        )

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
                # print(machine)
                machine = machine.strip()
                # machine = machine.split("-")[1].strip()
                mach = Machine.objects.get(name=machine)

                obj = MachineCount.objects.create(
                    machine=mach,
                    dailyReport=report,
                    activeCount=count[0],
                    inactiveCount=count[1],
                    totalCount=sum(count),
                )
                report.machines.add(obj.machine)

            else:
                continue

        for material, amount in materials.items():
            if amount[0] > 0:
                material = material.strip()

                mat = Material.objects.get(name=material)
                unit = Unit.objects.get(name=amount[1])
                obj = MaterialCount.objects.create(
                    material=mat,
                    dailyReport=report,
                    amount=amount[0],
                    unit=unit,
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

        report.cal_countPeople()
        report.cal_countMachines()

        return redirect(to="/home/daily-reports")
    else:
        return -1


def del_daily_report_from_db(request):
    if request.method == "POST":
        obj = DailyReport.objects.get(id=request.POST["id"])
        obj.delete()
        return redirect(to="/home/daily-reports")
    else:
        return -1


def reports_daily(request):
    reports = DailyReport.objects.all()

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
        "other": other,
    }
    return render(request, "print-report.html", context=context)


def get_options(request, typee):
    if request.method == "POST":
        data = json.loads(request.POST['options'])["options"]
        data = [item.strip().strip() for item in data]
        data = [f"{item.strip().split('-')[0].strip()}-{item.split('-')[-1].strip()}" for item in data]
        if typee == "profession":
            data = Profession.objects.exclude(name__in=data).all()
        elif typee == "position":
            data = Position.objects.exclude(name__in=data).all()
        elif typee == "machine":
            data = Machine.objects.exclude(name__in=data).all()
        elif typee == "material":
            data = Material.objects.exclude(name__in=data).all()
        elif typee == "contractor":
            data = Contractor.objects.exclude(name__in=data).all()
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


