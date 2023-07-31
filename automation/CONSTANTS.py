from .models import *

FILTERS = {
        "zone": Zone,
        "operation": Operation,
        "contractor": Contractor,
        "equipe": Contractor,

        "machine": Machine,
        "machineProvider": MachineProvider,

        "material": Material,
        "materialProvider": MaterialProvider,
    }

MODELS = {
    "zone": Zone,
    "operation": Operation,
    "contractor": Contractor,
}

MODELS_PERSIAN = {
    "equipe": "پیمانکار",
    "zone": "موقعیت",
    "operation": "عملیات",

    "machine": "تجهیز",
    "material": "مصالح",
    "machineProvider": "تامین کننده",
    "materialProvider": "تامین کننده",
}

MODELS_PATH_TO_EXCLUDE = {
    "contractor": {
        "models": [Equipe, ],
        "attrs": ["contractor",]
    },
    "equipe": {
        "models": [Equipe, ],
        "attrs": ["contractor",]
    },
    "operation": {
        "models": [ZoneOperation, ],
        "attrs": ["operation",]
    },
    "zone": {
        "models": [],
        "attrs": [],
    },


    "machine": {
        "models": [MachineCount],
        "attrs": ['machine'],
    },
    "machineProvider": {
        "models": [MachineCount],
        "attrs": ['provider'],
    },
    "dailyReportMachine": {
        "models": [MachineCount],
        "attrs": ["dailyReport"],
    },

    "material": {
        "models": [MaterialCount],
        "attrs": ['material'],
    },
    "materialProvider": {
        "models": [MaterialCount],
        "attrs": ['provider'],
    },
    "dailyReportMaterial": {
        "models": [MaterialCount],
        "attrs": ["dailyReport"],
    },

}

FILTER_KEY_NAMES = {
    type(Equipe()): ["contractor", "name"],
    type(Zone()): ["name"],
    type(Operation()): ["name"],

    type(Machine()): ['name'],
    type(MachineProvider()): ['name'],

    type(Material()): ['name'],
    type(MaterialProvider()): ['name'],
}


# Ahjam Filters to Output
FILTERS_WEIGHTS = {
        "operation": 1,
        "zone": 2,
        "equipe": 3,
}
FILTERS_OUTPUT_PIVOT = {
        1: Operation,           # (operation)
        3: ZoneOperation,       # (zone)                        + operation ||| # (operation, zone)
        4: ParentTask,          # (contractor)                  + operation ||| # (operation, contractor)
        6: ParentTask,          # (zone, contractor)            + operation ||| # (operation, zone, contractor)
}

OUTPUT_TARGETS = {
    Operation: {
        "CLASS": Operation,
        "ID": ['operation', 'id'],
        "VALUES": {
            "TOTALVOLUME": ["operation", "amount"],
        },
    },
    ZoneOperation: {
        "CLASS": ZoneOperation,
        "ID": ["parentTask", "operation", "id"],
        "VALUES": {
            "TOTALVOLUME": ["parentTask", "operation", "amount"],
        },
    },
    ParentTask: {
        "CLASS": ParentTask,
        "ID": ['parentTask', 'id'],
        "VALUES": {
            "TOTALVOLUME": ["parentTask", "totalVolume"],
        },
    },

    MachineCount: {
        "CLASS": MachineCount,
        "ID": ['id'],
        "VALUES": {
            "WORKHOURS": ["workHours"],
        },
    },

    MaterialCount: {
        "CLASS": MaterialCount,
        "ID": ['id'],
        "VALUES": {
            "AMOUNT": ["amount"],
        },
    },
}

EDIT_BASE_DATA = {
    "position": Position,
    "profession": Profession,
    "machine": Machine,
    "material": Material,
    "contractor": Contractor,
    "equipe": Equipe,
    "zone": Zone,
    "materialprovider": MaterialProvider,
    "machineprovider": MachineProvider,
    "operation": Operation,
    "zoneoperation": ZoneOperation,
}

ONLY_NAME_MODELS = ["position", "profession", "machine", "material", "contractor", "zone", "materialprovider", "machineprovider"]

