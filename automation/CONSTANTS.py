from .models import *

FILTERS = {
        "zone": Zone,
        "operation": Operation,
        "contractor": Contractor,
        "equipe": Contractor,
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
    }
}

FILTER_KEY_NAMES = {
    type(Equipe()): ["contractor", "name"],
    type(Zone()): ["name"],
    type(Operation()): ["name"],
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
}