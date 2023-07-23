from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from jdatetime import datetime
import jdatetime
from .converters import *
from django_jalali.db import models as jmodels


# Create your models here.


class Position(models.Model):
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


class Profession(models.Model):
    name = models.CharField(max_length=250, unique=True,)

    def __str__(self):
        return self.name


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
        # return str(self.get_type_display()) + " - " + self.name
        return self.name


class MachineProvider(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class MachineCount(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    workHours = models.PositiveIntegerField(default=0.0)

    activeCount = models.PositiveIntegerField(default=0)
    inactiveCount = models.PositiveIntegerField(default=0)
    totalCount = models.PositiveIntegerField(default=0)

    provider = models.ForeignKey(MachineProvider, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('dailyReport', 'machine', 'provider')

    def __str__(self):
        # TODO : add dailyReport.date to the returning string of the object
        return self.machine.name


class Unit(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class MaterialProvider(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class MaterialCount(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    amount = models.FloatField(default=0.0,)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    provider = models.ForeignKey(MaterialProvider, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('dailyReport', 'material', 'provider')

    def __str__(self):
        return self.material.name


class Contractor(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class ContractorCount(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    countExpert = models.PositiveIntegerField()
    countSemiExpert = models.PositiveIntegerField()
    countNonExpert = models.PositiveIntegerField()

    countTotal = models.PositiveIntegerField(default=0)

    def cal_countTotal(self):
        self.countTotal = self.countExpert + self.countSemiExpert + self.countNonExpert
        self.save()

    class Meta:
        unique_together = ('dailyReport', 'contractor')

    def __str__(self):
        return self.profession.name


class Equipe(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=True)

    def set_name(self):
        self.name = self.profession.name + "-" + self.contractor.name
        self.save()

    class Meta:
        unique_together = ('profession', 'contractor')

    def __str__(self):
        return self.profession.name + "-" + self.contractor.name


class EquipeCount(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)

    countExpert = models.PositiveIntegerField()
    countSemiExpert = models.PositiveIntegerField()
    countNonExpert = models.PositiveIntegerField()

    countTotal = models.PositiveIntegerField(default=0)

    def cal_countTotal(self):
        self.countTotal = self.countExpert + self.countSemiExpert + self.countNonExpert
        self.save()

    class Meta:
        unique_together = ('dailyReport', 'equipe')

    def __str__(self):
        return str(self.equipe)


class Zone(models.Model):
    # TODO : make unique=true
    name = models.CharField(max_length=250,)

    def __str__(self):
        return self.name


class Operation(models.Model):
    name = models.CharField(max_length=250, unique=True,)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="operation_unit")

    amount = models.FloatField(default=0.0, )
    assignedAmount = models.FloatField(default=0.0,)
    freeAmount = models.FloatField(default=0.0,)
    doneAmount = models.FloatField(default=0.0,)
    donePercentage = models.FloatField(default=0.0,)

    assignedWeight = models.FloatField(default=0.0, )
    freeWeight = models.FloatField(default=100.0, )
    fullyBroken = models.BooleanField(default=False)

    fullyAssigned = models.BooleanField(default=False)
    fullyDone = models.BooleanField(default=False)

    suboperations = models.ManyToManyField('SubOperation', related_name='operations')
    zones = models.ManyToManyField('ZoneOperation', related_name='zones')

    def update_doneAmount(self, auto=True, amount=None, action=None):
        if auto:
            self.doneAmount = 0.0
            for item in self.zones.all():
                self.doneAmount += item.doneAmount

        else:
            if action == "+":
                self.doneAmount += amount
            elif action == "-":
                self.doneAmount -= amount

        self.save()

        self.update_percentage()

    def update_percentage(self):
        self.donePercentage = self.doneAmount / self.amount * 100

        self.save()

    def update_assignedAmount(self):
        assigned = 0.0
        for zone in self.zones.all():
            assigned += zone.amount

        self.assignedAmount = assigned
        self.freeAmount = float(self.amount) - assigned

        if float(self.amount) - assigned > 0:
            self.fullyAssigned = False
        else:
            self.fullyAssigned = True

        self.save()

    def update_assignedWeight(self):
        broken = 0.0
        for subopr in self.suboperations.all():
            broken += subopr.weight

        self.assignedWeight = broken
        self.freeWeight = 100 - broken

        if 100 - broken > 0:
            self.fullyBroken = False
        else:
            self.fullyBroken = True

        self.save()

    def set_fully_assignment(self):
        if not self.assignedAmount < float(self.amount):
            self.fullyAssigned = True
        else:
            self.fullyAssigned = False
        self.save()

    def __str__(self):
        return self.name


class SubOperation(models.Model):
    name = models.CharField(max_length=250,)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    parent = models.ForeignKey(Operation, on_delete=models.CASCADE, )

    weight = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0.0)

    amount = models.FloatField(default=0.0,)
    doneAmount = models.FloatField(default=0.0,)

    def update_doneAmount(self, amount=None, action=None):
        print("sub-operation updated")
        if action == "+":
            self.doneAmount += amount
        elif action == "-":
            self.doneAmount -= amount

        self.save()

    class Meta:
        unique_together = ('name', 'parent')

    def __str__(self):
        return self.parent.name + " | " + self.name


class ZoneOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    amount = models.FloatField(default=0.0, )
    assignedAmount = models.FloatField(default=0.0, )
    freeAmount = models.FloatField(default=0.0, )
    doneAmount = models.FloatField(default=0.0, )
    donePercentage = models.FloatField(default=0.0, )

    tasks = models.ManyToManyField('Task', related_name='tasks')
    parentTasks = models.ManyToManyField('ParentTask', related_name='tasks')

    def update_freeAmount(self):
        self.freeAmount = float(self.amount) - float(self.assignedAmount)
        self.save()

    def update_assignedAmount(self, auto=True, amount=None, action=None):
        if auto:
            self.assignedAmount = 0.0
            for task in self.parentTasks.all():
                self.assignedAmount += task.totalVolume

            self.freeAmount = float(self.amount) - float(self.assignedAmount)

        else:
            if action == "+":
                self.assignedAmount += amount
            elif action == "-":
                self.assignedAmount -= amount
            self.freeAmount = float(self.amount) - float(self.assignedAmount)

        self.save()

    def update_doneAmount(self, auto=True, amount=None, action=None):
        if auto:
            self.doneAmount = 0.0
            for task in self.parentTasks.all():
                self.doneAmount += task.doneVolume

        else:
            if action == "+":
                self.doneAmount += amount
            elif action == "-":
                self.doneAmount -= amount

        self.save()

        self.update_donePercentage()

    def update_donePercentage(self):
        self.donePercentage = self.doneAmount / self.amount * 100

        self.save()

        self.operation.update_doneAmount()

    class Meta:
        unique_together = ('operation', 'zone')

    def __str__(self):
        return self.operation.name + " | " + self.zone.name


class ParentTask(models.Model):
    operation = models.ForeignKey(ZoneOperation, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    unique_str = models.CharField(max_length=250, unique=True)

    totalVolume = models.FloatField(default=0.1, )
    doneVolume = models.FloatField(default=0.0, )
    donePercentage = models.FloatField(default=0.0, )
    started = models.BooleanField(default=False, )
    completed = models.BooleanField(default=False, )
    # start_date = models.DateField(null=True, blank=True)
    # completion_date = models.DateField(null=True, blank=True)
    start_date = jmodels.jDateField( null=True, blank=True)
    completion_date = jmodels.jDateField( null=True, blank=True)

    subtasks = models.ManyToManyField('Task', related_name='subtasks')

    def check_completion(self):
        if self.donePercentage < 100:
            self.completed = False
            self.completion_date = None
            self.save()

    def reset(self):
        self.started = False
        self.completed = False
        self.completion_date = None
        self.start_date = None
        self.doneVolume = 0
        self.donePercentage = 0

        self.save()

    def complete(self, date):
        date = jdatetime.datetime.strptime(date, format="%Y-%m-%d %H:%M:%S")
        self.completed = True
        self.completion_date = jdatetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
        ).strftime("%Y-%m-%d")

        self.save()

    def start(self, date):
        datee = jdatetime.datetime.strptime(date, format="%Y-%m-%d %H:%M:%S")
        self.started = True
        self.start_date = jdatetime.datetime(
            year=datee.year,
            month=datee.month,
            day=datee.day,
        ).strftime("%Y-%m-%d")

        self.save()

    def update_doneVolume(self, date=None):
        self.doneVolume = 0
        for subtask in self.subtasks.all():
            self.doneVolume += subtask.doneVolume * subtask.suboperation.weight / 100

        self.save()
        self.update_percentage(date=date)
        pass

    def update_percentage(self, date=None):
        self.donePercentage = (self.doneVolume / self.totalVolume)*100
        self.save()

        if not self.donePercentage < 100:
            self.complete(date=date)

        elif self.donePercentage <= 0.0:
            self.reset()

        self.operation.update_doneAmount()

    def set_unique(self):
        self.unique_str = self.operation.operation.name + "-" + self.equipe.profession.name + "-" + self.equipe.contractor.name + "-" + self.zone.name
        self.save()

    class Meta:
        unique_together = ('operation', 'equipe', 'zone')

    def __str__(self):
        return self.unique_str


class Task(models.Model):
    parent = models.ForeignKey(ParentTask, on_delete=models.CASCADE)
    operation = models.ForeignKey(ZoneOperation, on_delete=models.CASCADE)
    suboperation = models.ForeignKey(SubOperation, on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    unique_str = models.CharField(max_length=250, unique=True)
    totalVolume = models.FloatField(default=0.1,)
    doneVolume = models.FloatField(default=0.0,)
    donePercentage = models.FloatField(default=0.0,)
    started = models.BooleanField(default=False,)
    completed = models.BooleanField(default=False,)
    # start_date = models.DateField(null=True, blank=True)
    # completion_date = models.DateField(null=True, blank=True)

    start_date = jmodels.jDateTimeField( null=True, blank=True)
    completion_date = jmodels.jDateField( null=True, blank=True)

    def check_completion(self):
        if self.donePercentage < 100:
            self.completed = False
            self.completion_date = None
            self.save()

    def reset(self):
        self.started = False
        self.completed = False
        self.completion_date = None
        self.start_date = None
        self.doneVolume = 0
        self.donePercentage = 0

        self.save()

    def complete(self, date):
        date = jdatetime.datetime.strptime(date, format="%Y-%m-%d %H:%M:%S")
        self.completed = True
        self.completion_date = jdatetime.datetime(
            year=date.year,
            month=date.month,
            day=date.day,
        ).strftime("%Y-%m-%d")

        self.save()

    def start(self, date):
        datee = jdatetime.datetime.strptime(date, format="%Y-%m-%d %H:%M:%S")
        self.started = True
        self.start_date = jdatetime.datetime(
            year=datee.year,
            month=datee.month,
            day=datee.day,
        ).strftime("%Y-%m-%d")

        self.save()

        if not self.parent.started:
            self.parent.start(date=date)


    def update_percentage(self, date=None):
        self.donePercentage = (self.doneVolume / self.totalVolume)*100
        self.save()

        self.parent.update_doneVolume(date=date)

        if not self.donePercentage < 100:
            self.complete(date=date)

        elif self.donePercentage <= 0.0:
            self.reset()

    def set_unique(self):
        self.unique_str = self.operation.operation.name + "-" + self.suboperation.name + "-" + self.equipe.profession.name + "-" + self.equipe.contractor.name + "-" + self.zone.name
        self.save()

    class Meta:
        unique_together = ('operation', 'suboperation', 'equipe', 'zone')

    def __str__(self):
        return self.unique_str


class TaskReport(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    parentTask = models.ForeignKey(ParentTask, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dailyReport = models.ForeignKey("DailyReport", on_delete=models.CASCADE)
    todayVolume = models.FloatField(default=0.0,)
    preDoneVolume = models.FloatField(default=0.0, )
    preDonePercentage = models.FloatField(default=0.0, )

    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = jmodels.jDateTimeField( auto_now_add=True)

    # reportDate = models.DateTimeField()
    reportDate = jmodels.jDateTimeField()


    # Filtering required fields -------------------------------------------------------------------
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, null=True, blank=True)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True, blank=True)

    def update_filtering_fields(self):
        self.operation = self.task.operation.operation
        self.zone = self.task.zone
        self.equipe = self.task.equipe

        self.save()

    def get_total_parent_values(self):
        if self.parent is None:
            return 0

        return self.parent.get_total_parent_values() + self.parent.todayVolume

    def update_percentage(self, reverse, date=None):
        if not reverse:
            self.task.preDoneVolume = self.task.doneVolume
            self.preDoneVolume = self.task.doneVolume
            self.preDonePercentage = self.preDoneVolume / self.task.totalVolume * 100
            self.task.doneVolume += self.todayVolume

            self.save()

            self.task.update_percentage(date=date)

            self.task.suboperation.update_doneAmount(amount=self.todayVolume, action="+")

        else:
            self.task.doneVolume -= self.todayVolume

            self.save()

            self.task.update_percentage(date=date)

            self.task.suboperation.update_doneAmount(amount=self.todayVolume, action="-")

            self.task.check_completion()

    def __str__(self):
        return self.task.unique_str

    class Meta:
        unique_together = ('dailyReport', 'task')


class DailyReport(models.Model):
    # --------------------Header----------------------
    project_name = models.CharField(max_length=250, default="Automation Project")
    employer = models.CharField(max_length=250, default="Default Employer")
    employee = models.CharField(max_length=250, default="Default Employee")
    contract_number = models.CharField(max_length=15,
                                       validators=[RegexValidator(r'^\d{1,10}$', 'Enter a valid number.')],
                                       default="123456789")

    # date = models.DateTimeField(default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date = jmodels.jDateTimeField( default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # short_date = models.DateField(default=jdatetime.datetime.now().strftime("%Y-%m-%d"))
    short_date = jmodels.jDateField( default=jdatetime.datetime.now().strftime("%Y-%m-%d"))

    weekday = models.IntegerField(choices=WEEKDAY_CHOICES, default=datetime.now().weekday())

    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = jmodels.jDateTimeField( auto_now_add=True)

    # date_created = models.DateTimeField(default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date_created = jmodels.jDateTimeField( default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # date_edited = models.DateTimeField(default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    date_edited = jmodels.jDateTimeField( default=jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #
    temperature_min = models.DecimalField(max_digits=3, decimal_places=0, default=00.0,)
    temperature_max = models.DecimalField(max_digits=3, decimal_places=0, default=00.0,)
    #
    weather = models.IntegerField(choices=WEATHER_CHOICES, default=0)
    dust_value = models.IntegerField(default=0)
    consultor_name = models.CharField(max_length=250, default="Consultor Project")
    # ------------------------------------------------
    # ---------------------Body-----------------------
    positions = models.ManyToManyField(Position, through='PositionCount')
    countPositions = models.IntegerField(default=0)

    professions = models.ManyToManyField(Profession, through='ProfessionCount')
    countProfessions = models.IntegerField(default=0)

    countPeople = models.IntegerField(default=0)

    # TODO : Check and Track the machine summation
    machines = models.ManyToManyField(Machine, through='MachineCount')
    countActiveMachines = models.IntegerField(default=0)
    countInactiveMachines = models.IntegerField(default=0)
    countAllMachines = models.IntegerField(default=0)

    materials = models.ManyToManyField(Material, through='MaterialCount')

    # TODO : Check and Track the Contractors and Equipes summation
    contractors = models.ManyToManyField(Contractor, through='ContractorCount')
    countContractors = models.IntegerField(default=0)

    equipes = models.ManyToManyField(Equipe, through='EquipeCount')
    countEquipes = models.IntegerField(default=0)

    tasks = models.ManyToManyField(Task, through="TaskReport")

    deletable = models.BooleanField(default=1)
    editable = models.BooleanField(default=1)
    edited = models.BooleanField(default=0)

    def set_weekday(self):
        self.weekday = jdatetime.datetime.strptime(self.date, format="%Y-%m-%d %H:%M:%S").weekday()
        self.short_date = self.date.split(" ")[0]
        self.save()

    def check_deletability(self):
        now = jdatetime.datetime.now()
        now = jdatetime.datetime(now.year, now.month, now.day,
                                 now.hour, now.minute, now.second,)
        date = jdatetime.datetime(self.date_created.year, self.date_created.month, self.date_created.day,
                                  self.date_created.hour, self.date_created.minute, self.date_created.second,)

        bound = jdatetime.timedelta(1, 0, 0, 0, 0, 0,)*100
        # bound = jdatetime.timedelta(0, 0, 1, 0, 0, 0,)
        if now - date > bound:
            self.deletable = 0
            self.editable = 0
            self.save()
        else:
            self.deletable = 1
            self.editable = 1
            self.save()

    def cal_countPeople(self):
        for position in self.positioncount_set.all():
            self.countPositions += position.count

        for profession in self.professioncount_set.all():
            self.countProfessions += profession.countTotal

        self.countPeople = self.countPositions + self.countProfessions

        self.save()

    def cal_countMachines(self):
        for machine in self.machinecount_set.all():
            self.countActiveMachines += machine.activeCount
            self.countInactiveMachines += machine.inactiveCount
            self.countAllMachines += machine.totalCount
        self.save()

    def update_tasks(self, reverse):
        for task in self.taskreport_set.all():
            task.update_percentage(reverse)
            self.save()

    def __str__(self):
        return self.project_name

