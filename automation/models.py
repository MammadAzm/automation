from django.db import models
from django.core.validators import RegexValidator
from jdatetime import datetime
from .converters import *


# Create your models here.


class Position(models.Model):
    name = models.CharField(max_length=250, unique=True,)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(max_length=250, unique=True,)

    def __str__(self):
        return self.name


class PositionCount(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    class Meta:
        unique_together = ('dailyReport', 'position')

    def __str__(self):
        return self.position.name


class ProfessionCount(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    countExpert = models.PositiveIntegerField()
    countSemiExpert = models.PositiveIntegerField()
    countNonExpert = models.PositiveIntegerField()

    countTotal = models.PositiveIntegerField(default=0)

    def cal_countTotal(self):
        self.countTotal = self.countExpert + self.countSemiExpert + self.countNonExpert
        self.save()

    class Meta:
        unique_together = ('dailyReport', 'profession')

    def __str__(self):
        return self.profession.name


class Machine(models.Model):
    type = models.IntegerField(choices=MACHINE_TYPES, default=0)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        # return self.name
        return str(self.get_type_display()) + " - " + self.name


class MachineCount(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('dailyReport', 'machine')

    def __str__(self):
        # TODO : add dailyReport.date to the returning string of the object
        return self.machine.name


class DailyReport(models.Model):
    # --------------------Header----------------------
    project_name = models.CharField(max_length=250, default="Automation Project")
    employer = models.CharField(max_length=250, default="Default Employer")
    employee = models.CharField(max_length=250, default="Default Employee")
    contract_number = models.CharField(max_length=15,
                                       validators=[RegexValidator(r'^\d{1,10}$', 'Enter a valid number.')],
                                       default="123456789")

    date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, default=datetime.now().weekday())
    #
    # temperature_min = models.DecimalField(max_digits=5, decimal_places=2)
    # temperature_max = models.DecimalField(max_digits=5, decimal_places=2)
    #
    # weather = models.IntegerField(choices=WEATHER_CHOICES)
    # ------------------------------------------------
    # ---------------------Body-----------------------
    positions = models.ManyToManyField(Position, through='PositionCount')
    countPositions = models.IntegerField(default=0)

    professions = models.ManyToManyField(Profession, through='ProfessionCount')
    countProfessions = models.IntegerField(default=0)

    countPeople = models.IntegerField(default=0)

    machines = models.ManyToManyField(Machine, through='MachineCount')
    countMachines = models.IntegerField(default=0)

    def cal_countPeople(self):
        for position in self.positioncount_set.all():
            self.countPositions += position.count

        for profession in self.professioncount_set.all():
            self.countProfessions += profession.countTotal

        self.countPeople = self.countPositions + self.countProfessions

        self.save()

    def cal_countMachines(self):
        for machine in self.machinecount_set.all():
            self.countMachines += machine.count

        self.save()

    def __str__(self):
        return self.project_name
