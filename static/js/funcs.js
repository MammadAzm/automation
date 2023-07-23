const STRINGS_FROM_NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

function print(entry) {
    console.log(entry);
}

function search_base_machine() {
    let dropdownItems = $('#dropdown-menu-base-machines').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-machine').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-machine").dispatchEvent(event);
      $('#base-machine-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-machine').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_profession() {
    let dropdownItems = $('#dropdown-menu-base-professions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-profession').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-profession").dispatchEvent(event);
      $('#base-profession-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-profession').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_contractor() {
    let dropdownItems = $('#dropdown-menu-base-contractors').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-contractor').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-contractor").dispatchEvent(event);
      $('#base-contractor-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-contractor').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_equipes() {
    // for create report page
    let dropdownItems = $('#dropdown-menu-base-equipes-professions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-equipe-profession').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-equipe-profession").dispatchEvent(event);
      $('#base-equipe-profession-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-equipe-profession').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_position() {
    let dropdownItems = $('#dropdown-menu-base-positions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-position').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-position").dispatchEvent(event);
      $('#base-position-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-position').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_material() {
    let dropdownItems = $('#dropdown-menu-base-materials').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-position').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-material").dispatchEvent(event);
      $('#base-material-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-material').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_equipe_task() {
    let dropdownItems = $('#dropdown-menu-base-tasks').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-task').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-task").dispatchEvent(event);
      $('#base-equipetask-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-task').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_tasks() {
    let dropdownItems = $('#dropdown-menu-base-tasks').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-task').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-task").dispatchEvent(event);
      $('#base-task-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-task').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_zone_task() {
    let dropdownItems = $('#dropdown-menu-base-zones').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-zone').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-zone").dispatchEvent(event);
      $('#base-zone-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-zone').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_unit_task() {
    let dropdownItems = $('#dropdown-menu-base-units').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-unit').val("");
      let event = new Event('keyup');
      document.getElementById("search-base-unit").dispatchEvent(event);
      $('#base-unit-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-unit').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_base_equipe(type) {
    // for base data page

    let dropdownItems = $('#dropdown-menu-base-equipes-'+type+'s').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-base-equipe-'+type).val("");
      let event = new Event('keyup');
      document.getElementById("search-base-equipe-" + type).dispatchEvent(event);
      $('#base-equipe-'+type+'-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-base-equipe-' + type).on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function del_profession(prof, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-profession',
            data: {
            'profession': prof,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(prof)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(prof)
        obj.remove()
    }

}

function del_position(pos, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-position',
            data: {
            'position': pos,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(pos)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(pos)
        obj.remove()
    }

}

function del_machine(mach, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-machine',
            data: {
            'machine': mach,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(mach)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(mach)
        obj.remove()
    }

}

function del_material(mat, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-material',
            data: {
            'material': mat,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(mat)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(mat)
        obj.remove()
    }

}

function del_contractor(contractor, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-contractor',
            data: {
            'contractor': contractor,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(contractor)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(equipe)
        obj.remove()
    }

}

function del_zone(zone, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-zone',
            data: {
            'zone': zone,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(zone)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(zone)
        obj.remove()
    }

}

function del_unit(unit, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-unit',
            data: {
            'unit': unit,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(unit)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(unit)
        obj.remove()
    }

}

function del_operation(operation, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-operation',
            data: {
            'operation': operation,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                alert("با موفقیت حذف شد")
                let obj = document.getElementById(operation)

                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(operation)
        obj.remove()
    }

}

function del_materialprovider(materialprovider, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-materialprovider',
            data: {
            'materialprovider': materialprovider,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(materialprovider)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(materialprovider)
        obj.remove()
    }

}

function del_machineprovider(machineprovider, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-machineprovider',
            data: {
            'machineprovider': machineprovider,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(machineprovider)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(machineprovider)
        obj.remove()
    }

}

function del_equipe(prof, cont, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-equipe',
            data: {
            'profession': prof,
            'contractor': cont,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(prof+"-"+cont)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(prof)
        obj.remove()
    }

}

function del_task(taskOperation, equipeName, zoneName, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-task',
            data: {
            'taskOperation': taskOperation,
            // 'taskSubOperation': taskSubOperation,
            'equipeName': equipeName,
            'zoneName': zoneName,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(taskOperation+"-"+equipeName+"-"+zoneName)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(taskOperation+"-"+equipeName+"-"+zoneName)
        obj.remove()
    }

}

function del_task_in_report(taskOperation, taskSubOperation, equipeName, zoneName, db=false) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-task-in-report',
            data: {
            'taskOperation': taskOperation,
            'taskSubOperation': taskSubOperation,
            'equipeName': equipeName,
            'zoneName': zoneName,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(taskOperation+"-"+taskSubOperation+"-"+equipeName+"-"+zoneName)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(taskOperation+"-"+taskSubOperation+"-"+equipeName+"-"+zoneName)
        obj.remove()
    }

}

function search_machine() {
    let dropdownItems = $('#dropdown-menu-machines').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-machine').val("");
      let event = new Event('keyup');
      document.getElementById("search-machine").dispatchEvent(event);
      $('#machine-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-machine').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_profession() {
    let dropdownItems = $('#dropdown-menu-professions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-profession').val("");
      let event = new Event('keyup');
      document.getElementById("search-profession").dispatchEvent(event);
      $('#profession-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-profession').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_contractor() {
    let dropdownItems = $('#dropdown-menu-contractors').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-contractor').val("");
      let event = new Event('keyup');
      document.getElementById("search-contractor").dispatchEvent(event);
      $('#contractor-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-contractor').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_equipes() {
    // for create report page

    let dropdownItems = $('#dropdown-menu-equipes-professions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-equipe-profession').val("");
      let event = new Event('keyup');
      document.getElementById("search-equipe-profession").dispatchEvent(event);
      $('#equipe-profession-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-equipe-profession').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_providers(type) {
    // for create report page

    let dropdownItems = $('#dropdown-menu-' + type + 's').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-'+type).val("");
      let event = new Event('keyup');
      document.getElementById("search-"+type).dispatchEvent(event);
      $('#'+type+'-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-'+type).on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_position() {
    let dropdownItems = $('#dropdown-menu-positions').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-position').val("");
      let event = new Event('keyup');
      document.getElementById("search-position").dispatchEvent(event);
      $('#position-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-position').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_material() {
    let dropdownItems = $('#dropdown-menu-materials').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-position').val("");
      let event = new Event('keyup');
      document.getElementById("search-material").dispatchEvent(event);
      $('#material-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-material').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_equipe_task() {
    let dropdownItems = $('#dropdown-menu-tasks').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-task').val("");
      let event = new Event('keyup');
      document.getElementById("search-task").dispatchEvent(event);
      $('#equipetask-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-task').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_tasks() {
    let dropdownItems = $('#dropdown-menu-tasks').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-task').val("");
      let event = new Event('keyup');
      document.getElementById("search-task").dispatchEvent(event);
      $('#task-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-task').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_zone_task() {
    let dropdownItems = $('#dropdown-menu-zones').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-zone').val("");
      let event = new Event('keyup');
      document.getElementById("search-zone").dispatchEvent(event);
      $('#zone-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-zone').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_unit_task() {
    let dropdownItems = $('#dropdown-menu-units').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-unit').val("");
      let event = new Event('keyup');
      document.getElementById("search-unit").dispatchEvent(event);
      $('#task-unit').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-unit').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_unit_operation(shortcut=null) {
    if (shortcut) {
        shortcut = "base-"
    } else {
        shortcut = ""
    }

    let dropdownItems = $('#dropdown-menu-'+shortcut+'unitforoperations').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-unitforoperation').val("");
      let event = new Event('keyup');
      document.getElementById("search-unitforoperation").dispatchEvent(event);
      $('#unitforoperation-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-unitforoperation').on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function search_equipe(type) {
    // for base data page

    let dropdownItems = $('#dropdown-menu-equipes-'+type+'s').find('a');

    // Add event listener to the dropdown items
    dropdownItems.on('click', function() {
      let selectedItemText = $(this).text();

      // Set the search input value to the selected item text
      $('#search-equipe-'+type).val("");
      let event = new Event('keyup');
      document.getElementById("search-equipe-" + type).dispatchEvent(event);
      $('#equipe-'+type+'-name').val(selectedItemText);
    });
    // Add event listener to the search input
    $('#search-equipe-' + type).on('keyup', function() {
      let searchText = $(this).val().toLowerCase();

      // Loop through each dropdown item and hide/show based on search text
      dropdownItems.each(function() {
        let text = $(this).text().toLowerCase();
        if (text.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });
}

function add_machine_to_daily_report() {
    let val = document.getElementById("machine-name").value;
    if (!val) {
        return 0
    }
    let valP = document.getElementById("machineprovider-name").value;
    if (!valP) {
        return 0
    }

    document.getElementById("machine-name").value = "";
    document.getElementById("machineprovider-name").value = "";

    let table = document.getElementById("table-machine");
    let tbody = table.getElementsByTagName("tbody")[0];

    let rows = tbody.getElementsByTagName("tr")
    for (let i = 0; i < rows.length; i++) {
        let name = rows[i].getElementsByTagName("td")[0].innerText
        let prov = rows[i].getElementsByTagName("td")[4].innerText

        if (name.trim() === val.trim() && prov.trim() === valP.trim()) {
            alert("این ماشین قبلا به جدول اضافه شده است")
            return 0
        }
    }

    let newRow = document.createElement('tr');
    newRow.id = val;

    let cell1 = document.createElement('td', );
    cell1.className = "";
    cell1.innerHTML = val;
    let span = document.createElement('span', );
    Object.assign(span.style, {
        float: 'right',
        color: 'black',
    });
    span.className = "badge rounded-pill";
    span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
    span.style.marginLeft = "5pt"
    span.style.marginLeft = "5pt"
    span.addEventListener('click', function() {
    del_machine(val, false);
    });

    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell02 = document.createElement('td', );
    cell02.className = "";
    let input0 = document.createElement('input', );
    input0.style.borderRadius = "0"
    input0.style.textAlign = "center"
    input0.required = true;
    input0.className = "small-input-integer";
    input0.type = "number";
    input0.id = "machine_"+val+"_"+valP+"_workHours";
    input0.name = "machine_"+val+"_"+valP+"_workHours";
    input0.min = '0';
    input0.value = '0';

    cell02.appendChild(input0)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    input.required = true;
    input.className = "small-input-integer";
    input.type = "number";
    input.id = "machine_"+val+"_"+valP+"_activeCount";
    input.name = "machine_"+val+"_"+valP+"_activeCount";
    input.min = '0';
    input.value = '0';

    cell2.appendChild(input)

    let cell3 = document.createElement('td', );
    cell3.className = "";
    input = document.createElement('input', );
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    input.required = true;
    input.className = "small-input-integer";
    input.type = "number";
    input.id = "machine_"+val+"_"+valP+"_inactiveCount";
    input.name = "machine_"+val+"_"+valP+"_inactiveCount";
    input.min = '0';
    input.value = '0';
    cell3.appendChild(input)

    let cell4 = document.createElement('td', );
    cell4.className = "";
    let select = document.createElement('select',)
    select.required = true;
    select.className = "form-select";
    select.id = "machine_"+val+"_"+valP+"_provider";
    select.name = "machine_"+val+"_"+valP+"_provider";
    select.style.fontSize = '11px';
    select.style.textAlign = 'left  ';
    select.style.padding = '0';
    select.style.paddingLeft = '15%';

    let option = document.createElement('option',)
    option.value = valP
    option.innerHTML = valP
    option.selected = true
    select.appendChild(option)

    cell4.appendChild(select)

    newRow.appendChild(cell1);
    newRow.appendChild(cell02);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);
    newRow.appendChild(cell4);

    table.querySelector('tbody').appendChild(newRow);

}

function add_material_to_daily_report() {
    let val = document.getElementById("material-name").value;
    if (!val) {
        return 0
    }
    let valP = document.getElementById("materialprovider-name").value;
    if (!valP) {
        return 0
    }

    document.getElementById("material-name").value = "";
    document.getElementById("materialprovider-name").value = "";


    let table = document.getElementById("table-material");
    let tbody = table.getElementsByTagName("tbody")[0];

    let rows = tbody.getElementsByTagName("tr")
    for (let i = 0; i < rows.length; i++) {
        let name = rows[i].getElementsByTagName("td")[0].innerText
        let prov = rows[i].getElementsByTagName("td")[3].innerText

        if (name.trim() === val.trim() && prov.trim() === valP.trim()) {
            alert("این مصالح قبلا به جدول اضافه شده است")
            return 0
        }
    }


    let newRow = document.createElement('tr');
    newRow.id = val;

    let cell1 = document.createElement('td', );
    cell1.className = "";
    cell1.innerHTML = val;
    let span = document.createElement('span', );
    Object.assign(span.style, {
        float: 'right',
        color: 'black',
    });
    span.className = "badge rounded-pill";
    span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
    span.style.marginLeft = "5pt"
    span.addEventListener('click', function() {
    del_material(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    input.required = true;
    input.className = "small-input-integer w-75";
    input.type = "number";
    input.id = "material_"+val+"_"+valP+"_count";
    input.name = "material_"+val+"_"+valP+"_count";
    input.min = '0';
    input.value = '0';

    let cell3 = document.createElement('td', );
    cell3.className = "";
    let select = document.createElement('select',)
    select.required = true;
    select.className = "form-select";
    select.id = "material_"+val+"_"+valP+"_unit";
    select.name = "material_"+val+"_"+valP+"_unit";
    select.style.fontSize = '11px';
    select.style.textAlign = 'left  ';
    select.style.padding = '0';
    select.style.paddingLeft = '15%';

    input.onchange = function () {
        toggle_requirement.call(this, select.id, input.id)
    }
    cell2.appendChild(input)

    let option = document.createElement('option',)
    option.value = ""
    option.innerHTML = "انتخاب"
    option.disabled = true
    option.hidden = true
    option.selected = true
    select.appendChild(option)

    fetch_units(function (units) {
        units.forEach(unit => {
            let option = document.createElement('option',)
            option.value = unit.name
            option.innerHTML = unit.name
            select.appendChild(option)
        })
    })
    cell3.appendChild(select)

    let cell4 = document.createElement('td', );
    cell4.className = "";
    let select2 = document.createElement('select',)
    select2.required = true;
    select2.className = "form-select";
    select2.id = "material_"+val+"_"+valP+"_provider";
    select2.name = "material_"+val+"_"+valP+"_provider";
    select2.style.fontSize = '11px';
    select2.style.textAlign = 'left  ';
    select2.style.padding = '0';
    select2.style.paddingLeft = '15%';

    option = document.createElement('option',)
    option.value = valP
    option.innerHTML = valP
    option.selected = true
    select2.appendChild(option)

    // fetch_materialproviders(function (materialproviders) {
    //     materialproviders.forEach(materialprovider => {
    //         let option = document.createElement('option',)
    //         option.value = materialprovider.name
    //         option.innerHTML = materialprovider.name
    //         select2.appendChild(option)
    //     })
    // })

    cell4.appendChild(select2)

    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);
    newRow.appendChild(cell4);

    table.querySelector('tbody').appendChild(newRow);

}

function add_profession_to_daily_report() {
    let val = document.getElementById("profession-name").value
    document.getElementById("profession-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-profession")

    let newRow = document.createElement('tr');
    newRow.id = val;

    let cell1 = document.createElement('td', );
    cell1.className = "";
    let span = document.createElement('span', );
    Object.assign(span.style, {
        float: 'right',
        color: 'black',
    });
    span.className = "badge rounded-pill";
    span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
    span.style.marginLeft = "5pt"
    span.addEventListener('click', function() {
    del_profession(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)
    newRow.appendChild(cell1);

    let cell2 = document.createElement('td', );
    cell2.className = "";

    let counts = ["_ExpertCount", "_SemiExpertCount",
                     "_NonExpertCount", "_count",]
    for (let i=0; i<3; i++){
        let cell_i = document.createElement('td', );
        cell_i.className = "";

        let input = document.createElement('input', );
        input.style.borderRadius = "0"
        input.style.textAlign = "center"
        input.required = true;
        input.className = "small-input-integer";
        input.type = "number";
        input.id = "profession_"+val+counts[i];
        input.name = "profession_"+val+counts[i];
        input.min = '0';
        input.value = '0';

        cell_i.appendChild(input);

        newRow.appendChild(cell_i);
    }

    table.querySelector('tbody').appendChild(newRow);

}

function add_equipe_to_daily_report() {
    let val = document.getElementById("equipe-profession-name").value
    let prof = val.split("-")[0]
    let cont = val.split("-")[1]

    document.getElementById("equipe-profession-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-equipes-profession")

    let newRow = document.createElement('tr');
    newRow.id = val;

    let cell1 = document.createElement('td', );
    cell1.className = "";
    let span = document.createElement('span', );
    Object.assign(span.style, {
        float: 'right',
        color: 'black',
    });
    span.className = "badge rounded-pill";
    span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
    span.style.marginLeft = "5pt"
    span.addEventListener('click', function() {
    del_profession(val, false);
    });
    cell1.innerHTML = prof;
    cell1.appendChild(span)
    newRow.appendChild(cell1);

    let cell2 = document.createElement('td', );
    cell2.className = "";
    cell2.innerHTML = cont
    newRow.appendChild(cell2)

    let counts = ["_ExpertCount", "_SemiExpertCount",
                     "_NonExpertCount", "_count",]
    for (let i=0; i<3; i++){
        let cell_i = document.createElement('td', );
        cell_i.className = "";

        let input = document.createElement('input', );
        input.style.borderRadius = "0"
        input.style.textAlign = "center"
        input.required = true;
        input.className = "small-input-integer";
        input.type = "number";
        input.id = prof+counts[i];
        input.name = "equipe_profession_"+val+counts[i];
        input.min = '0';
        input.value = '0';

        cell_i.appendChild(input);

        newRow.appendChild(cell_i);
    }

    table.querySelector('tbody').appendChild(newRow);

}

function add_position_to_daily_report() {
    let val = document.getElementById("position-name").value;
    document.getElementById("position-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-position");

    let newRow = document.createElement('tr');
    newRow.id = val;

    let cell1 = document.createElement('td', );
    cell1.className = "";
    cell1.innerHTML = val;
    let span = document.createElement('span', );
    Object.assign(span.style, {
        float: 'right',
        color: 'black',
    });
    span.className = "badge rounded-pill";
    span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
    span.style.marginLeft = "5pt"
    span.addEventListener('click', function() {
    del_position(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    input.required = true;
    input.className = "small-input-integer";
    input.type = "number";
    input.id = "position_"+val+"_count";
    input.name = "position_"+val+"_count";
    input.min = '0';
    input.value = '0';
    cell2.appendChild(input);

    newRow.appendChild(cell1);
    newRow.appendChild(cell2);

    table.querySelector('tbody').appendChild(newRow);

}

function add_task_to_daily_report() {
    let val = document.getElementById("task-name").value;
    document.getElementById("task-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-task");
    $.ajax({
        type: 'POST',
        url: '/edit-db/get-task',
        data: {
        'options': val,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            let obj = response
            let newRow = document.createElement('tr');
            newRow.id = val;
            let cell1 = document.createElement('td', );
            cell1.className = "";
            cell1.innerHTML = obj.name;
            let span = document.createElement('span', );
            Object.assign(span.style, {
                float: 'right',
                color: 'black',
            });
            span.className = "badge rounded-pill";
            span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
            span.style.marginLeft = "5pt"
            span.addEventListener('click', function() {
            del_task(obj.name, obj.equipe, obj.zone, obj.totalVolume, obj.unit, false);
            });
            cell1.innerHTML = obj.name;
            cell1.appendChild(span)

            let cell2 = document.createElement('td', );
            cell2.className = "";
            cell2.innerHTML = obj.equipe;

            let cell3 = document.createElement('td', );
            cell3.className = "";
            cell3.innerHTML = obj.zone;

            let cell4 = document.createElement('td', );
            let input = document.createElement('input', );
            input.style.borderRadius = "0"
            input.style.textAlign = "center"
            input.required = true;
            input.className = "small-input-integer";
            input.type = "number";
            input.id = "task_"+val+"_today";
            input.name = "task_"+val+"_today";
            input.min = '0';
            input.value = '0';
            input.addEventListener('keyup', function() {
                let target = document.getElementById('live_total_done_'+'task_'+val+'_today')
                target.innerHTML = parseFloat(input.value) + parseFloat(document.getElementById('doneVolume_'+'task_'+val+'_today').innerHTML)
            });
            cell4.className = "";
            cell4.appendChild(input)

            let cell5 = document.createElement('td', );
            cell5.className = "";
            cell5.style.textAlign = "center"
            cell5.id = 'doneVolume_'+'task_'+val+'_today'
            cell5.innerHTML = obj.doneVolume.toFixed(2);

            let cell5_1 = document.createElement('td', );
            cell5_1.className = "";
            cell5_1.style.textAlign = "center"
            cell5_1.id = 'live_total_done_'+'task_'+val+'_today'


            let cell6 = document.createElement('td', );
            cell6.className = "";
            cell6.style.textAlign = "center"
            cell6.innerHTML = obj.totalVolume.toFixed(2);

            let cell7 = document.createElement('td', );
            cell7.className = "";
            cell7.style.textAlign = "center"
            cell7.innerHTML = obj.donePercentage.toFixed(2);

            let cell8 = document.createElement('td', );
            cell8.className = "";
            cell8.style.textAlign = "center"
            cell8.innerHTML = obj.unit;


            newRow.appendChild(cell1);
            newRow.appendChild(cell2);
            newRow.appendChild(cell3);
            newRow.appendChild(cell4);
            newRow.appendChild(cell5);
            newRow.appendChild(cell5_1);
            newRow.appendChild(cell6);
            newRow.appendChild(cell7);
            newRow.appendChild(cell8);


            table.querySelector('tbody').appendChild(newRow);
        }
    });



    // let cell2 = document.createElement('td', );
    // cell2.className = "";
    // let input = document.createElement('input', );
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    // input.required = true;
    // input.className = "small-input-integer";
    // input.type = "number";
    // input.id = "position_"+val+"_count";
    // input.name = "position_"+val+"_count";
    // input.min = '0';
    // input.value = '0';
    // cell2.appendChild(input);
    //
    //
    // newRow.appendChild(cell2);



}

function add_equipe_to_base_data(shortcut=null) {
    if (shortcut) {
        let valProf = document.getElementById("base-equipe-profession-name").value
        let valCont = document.getElementById("base-equipe-contractor-name").value

        if (!valProf) {
            return 0
        } else if (!valCont) {
            return 0
        }

        document.getElementById("base-equipe-profession-name").value = "";
        document.getElementById("base-equipe-contractor-name").value = "";

         $.ajax({
                type: 'POST',
                url: '/edit-db/add-equipe',
                data: {
                'profession': valProf,
                'contractor': valCont,
                },
                beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
                },
                success: function(response) {
                    if (response == "True" || response == true) {
                        alert("با موفقیت اضافه شد")
                    }
                }
            });
    } else {
        let valProf = document.getElementById("equipe-profession-name").value
        document.getElementById("equipe-profession-name").value = "";

        let valCont = document.getElementById("equipe-contractor-name").value
        document.getElementById("equipe-contractor-name").value = "";
        if (!valProf) {
            return 0
        } else if (!valCont) {
            return 0
        }

        let table = document.getElementById("table-equipe")

        let newRow = document.createElement('tr');
        newRow.id = valProf + "-" + valCont;

        let cell1 = document.createElement('td', );
        cell1.className = "";
        let span = document.createElement('span', );
        Object.assign(span.style, {
            float: 'left',
            color: 'black',
        });
        span.className = "badge rounded-pill";
        span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
        span.style.marginLeft = "5pt"
        span.addEventListener('click', function() {
        del_equipe(valProf, valCont,true);
        });
        cell1.innerHTML = valProf + "-" + valCont;
        cell1.appendChild(span)
        newRow.appendChild(cell1);

         $.ajax({
                type: 'POST',
                url: '/edit-db/add-equipe',
                data: {
                'profession': valProf,
                'contractor': valCont,
                },
                beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
                },
                success: function(response) {
                    if (response == "True") {
                        table.querySelector('tbody').appendChild(newRow);
                    }
                }
            });
    }

}

function add_task_to_base_data(shortcut=null) {
    if (shortcut) {
        let taskName = document.getElementById("base-task-name").value
        let equipeName = document.getElementById("base-equipetask-name").value
        let zoneName = document.getElementById("base-zone-name").value
        let taskVol = document.getElementById("base-task-volume").value
        let unitName = document.getElementById("base-unit-name").value
        if ( !taskName || !equipeName || !zoneName || !taskVol || !unitName ) {
            return 0
        }

        document.getElementById("base-task-name").value = "";
        document.getElementById("base-equipetask-name").value = "";
        document.getElementById("base-zone-name").value = "";
        document.getElementById("base-task-volume").value = "";

         $.ajax({
                type: 'POST',
                url: '/edit-db/add-task',
                data: {
                'taskName': taskName,
                'equipeName': equipeName,
                'zoneName': zoneName,
                'unitName': unitName,
                'taskVol': taskVol,
                },
                beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
                },
                success: function(response) {
                    if (response == "True") {
                        alert("عملیات با موفقیت انجام شد")
                    }
                }
            });
    } else {
        let taskName = document.getElementById("task-name").value
        document.getElementById("task-name").value = "";

        let equipeName = document.getElementById("equipetask-name").value
        document.getElementById("equipetask-name").value = "";

        let zoneName = document.getElementById("zone-name").value
        document.getElementById("zone-name").value = "";

        let taskVol = document.getElementById("task-volume").value
        document.getElementById("task-volume").value = "";

        let unitName = document.getElementById("task-unit").value
        document.getElementById("task-unit").value = "";

        if ( !taskName || !equipeName || !zoneName || !taskVol || !unitName ) {
            return 0
        }
        let table = document.getElementById("table-task")

        let newRow = document.createElement('tr');
        newRow.id = taskName + "-" + equipeName + "-" + zoneName;

        let descr = document.createElement('td', );
        descr.className = "";
        let span = document.createElement('span', );
        Object.assign(span.style, {
            float: 'left',
            color: 'black',
        });
        span.className = "badge rounded-pill";
        span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
        span.style.marginLeft = "5pt"
        span.addEventListener('click', function() {
        del_task(taskName, equipeName, zoneName, taskVol, unitName, true);
        });
        descr.innerHTML = taskName;
        descr.style.width = "35%";
        descr.appendChild(span)

        let equipeCell = document.createElement('td', );
        equipeCell.className = ""
        equipeCell.style.width = "26%";
        equipeCell.innerHTML = equipeName;

        let zoneCell = document.createElement('td', );
        zoneCell.className = ""
        zoneCell.style.width = "13%";
        zoneCell.innerHTML = zoneName;

        let unitCell = document.createElement('td', );
        unitCell.className = ""
        unitCell.style.width = "13%";
        unitCell.innerHTML = unitName;

        let volCell = document.createElement('td', );
        volCell.className = ""
        volCell.style.width = "13%";
        volCell.innerHTML = taskVol;

        newRow.appendChild(descr);
        newRow.appendChild(equipeCell);
        newRow.appendChild(zoneCell);
        newRow.appendChild(unitCell);
        newRow.appendChild(volCell);
         $.ajax({
                type: 'POST',
                url: '/edit-db/add-task',
                data: {
                'taskName': taskName,
                'equipeName': equipeName,
                'zoneName': zoneName,
                'unitName': unitName,
                'taskVol': taskVol,
                },
                beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
                },
                success: function(response) {
                    if (response == "True") {
                        table.querySelector('tbody').appendChild(newRow);
                    }
                }
            });
    }

}

function fetch_options(type, shortcut=null){
    if (shortcut) {
        let typetype = false;
        if (type[0] == "equipe"){
            if (type[1] == "profession") {
                type = "profession"
                typetype = "base-equipes-profession"
            } else {
                type = "contractor"
                typetype = "base-equipes-contractor"
            }
        } else {
            typetype = "base-"+type;
        }

        let menu = document.getElementById("dropdown-menu-" + typetype + "s")
        let options = menu.querySelectorAll('.dropdown-item');

        if (type === "unitforoperation") {
            type = "unit"
        }

        options.forEach(option => {
          option.remove()
        });
        let innerHTMLs = []

        options = JSON.stringify(
            {
                'options': innerHTMLs,
            }
        )
        $.ajax({
            type: 'POST',
            url: '/edit-db/get-options/' + type,
            data: {
                'options': options,
            },
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function (response) {
                let opts = response[type]
                opts = JSON.parse(opts)
                for (let i = 0; i < opts.length; i++) {
                    let li = document.createElement("li")
                    let a = document.createElement("a")
                    a.className = "dropdown-item";
                    a.innerHTML = opts[i].name;
                    li.appendChild(a);
                    menu.appendChild(li);
                }

                if (typetype.includes("equipe")) {
                    if (type=="profession") {
                       search_base_equipe(type);
                    } else if (type=="contractor") {
                        search_base_equipe(type);
                    }
                } else if ( type == "zone" || type == "unit" ) {
                    if (type == "zone"){
                        search_base_zone_task();
                    } else {
                        search_base_unit_task();
                    }
                }

                if (type == "position") {
                    search_base_position();
                } else if (type == "profession") {
                    search_base_profession();
                } else if (type == "machine") {
                    search_base_machine();
                } else if (type == "material") {
                    search_base_material();
                } else if (type == "task") {
                    search_base_equipe_task();
                } else if (type == "zone") {
                    search_base_zone_task();
                } else if (type === "unit") {
                    search_unit_operation(shortcut=true)
                }

            }
        })

    }
    else {
        let typetype = false;
        if (type[0] == "equipe"){
            if (type[1] == "profession") {
                type = "profession"
                typetype = "equipes-profession"
            } else {
                type = "contractor"
                typetype = "equipes-contractor"
            }
        } else {
            typetype = type;
        }

        let menu = document.getElementById("dropdown-menu-" + typetype + "s")
        let options = menu.querySelectorAll('.dropdown-item');
        options.forEach(option => {
          option.remove()
        });
        if (type === "unitforoperation") {
            type = "unit"
        }
        let table = document.getElementById("table-" + type)
        let tbody = table.getElementsByTagName("tbody")[0]
        let rows = tbody.getElementsByTagName("tr")
        let innerHTMLs = []
        for (let i = 0; i < rows.length; i++) {
            let item = rows[i].getElementsByTagName("td")[0]
            item = item.textContent.replace("-" , "").trim()
            innerHTMLs.push(item);
        }
        if (typetype.includes("equipe")) {
            let opts = innerHTMLs
            for (let i = 0; i < opts.length; i++) {

                let item = opts[i].replace(/-/g, "") .trim()
                let li = document.createElement("li")
                let a = document.createElement("a")
                a.className = "dropdown-item";
                a.innerHTML = item;

                li.appendChild(a);
                menu.appendChild(li);
            }

            if (type=="profession") {
               search_equipe(type);
            } else if (type=="contractor") {
                search_equipe(type);
            }

        } else if ( type == "zone" || type == "unit" ){
                let opts = innerHTMLs
            for (let i = 0; i < opts.length; i++) {

                let item = opts[i]
                let li = document.createElement("li")
                let a = document.createElement("a")
                a.className = "dropdown-item";
                a.innerHTML = item;

                li.appendChild(a);
                menu.appendChild(li);
                if (type == "zone"){
                    search_zone_task();
                } else {
                    search_unit_task();
                    search_unit_operation();
                }

            }
        } else {
            options = JSON.stringify(
                {
                'options': innerHTMLs,
                }
            )
            $.ajax({
            type: 'POST',
            url: '/edit-db/get-options/'+type,
            data: {
            'options': options,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let opts = response[type]
                opts = JSON.parse(opts)
                for (let i = 0; i < opts.length; i++) {
                    let li = document.createElement("li")
                    let a = document.createElement("a")
                    a.className = "dropdown-item";
                    a.innerHTML = opts[i].name;
                    li.appendChild(a);
                    menu.appendChild(li);
                }

                if (type=="position") {
                   search_position();
                } else if (type=="profession") {
                    search_profession();
                } else if (type=="machine") {
                    search_machine();
                } else if (type=="material") {
                    search_material();
                } else if (type=="task") {
                    search_equipe_task();
                } else if (type=="zone") {
                    search_zone_task();
                }
            }
        });
        }
    }


}

function fetch_equipes(){
    let menu = document.getElementById("dropdown-menu-equipes-professions")
    let options_profs = menu.querySelectorAll('.dropdown-item');
    options_profs.forEach(option => {
      option.remove()
    });

    // let menu_conts = document.getElementById("dropdown-menu-equipes-contractors")
    // let options_conts = menu_conts.querySelectorAll('.dropdown-item');
    // options_profs.forEach(option => {
    //   option.remove()
    // });

    let table = document.getElementById("table-equipes-profession")
    let tbody = table.getElementsByTagName("tbody")[0]
    let rows = tbody.getElementsByTagName("tr")

    let innerHTMLs = []

    for (let i = 0; i < rows.length; i++) {
        let prof = rows[i].getElementsByTagName("td")[0]
        let cont = rows[i].getElementsByTagName("td")[1]

        innerHTMLs.push(prof.textContent + "-" + cont.textContent);
    }

    options = JSON.stringify(
        {
        'options': innerHTMLs,
        }
    )
    $.ajax({
        type: 'POST',
        url: '/edit-db/get-options/equipe',
        data: {
        'options': options,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            let opts = response
            for (let key in opts) {
                if (key == "equipe"){
                    break;
                }
                let li = document.createElement("li")
                let a = document.createElement("a")
                a.className = "dropdown-item";
                a.innerHTML = key;

                li.appendChild(a);
                menu.appendChild(li);
            }


            search_equipes();

        }
    });


}

function fetch_providers(type){

    let menu = document.getElementById("dropdown-menu-"+type+"s")

    let options = menu.querySelectorAll('.dropdown-item');
    options.forEach(option => {
      option.remove()
    });


    // let table = document.getElementById("table-equipes-profession")
    // let tbody = table.getElementsByTagName("tbody")[0]
    // let rows = tbody.getElementsByTagName("tr")

    let innerHTMLs = []

    // for (let i = 0; i < rows.length; i++) {
    //     let prof = rows[i].getElementsByTagName("td")[0]
    //     let cont = rows[i].getElementsByTagName("td")[1]
    //
    //     innerHTMLs.push(prof.textContent + "-" + cont.textContent);
    // }

    options = JSON.stringify(
        {
        'options': innerHTMLs,
        }
    )
    $.ajax({
        type: 'POST',
        url: '/edit-db/get-options/'+type,
        data: {
        'options': options,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            let opts = JSON.parse(response[type])
            opts.forEach(function (opt){
                let li = document.createElement("li")
                let a = document.createElement("a")
                a.className = "dropdown-item";
                a.innerHTML = opt.name;

                li.appendChild(a);
                menu.appendChild(li);
            })

            search_providers(type);
        }
    });


}

function fetch_tasks(){
    let menu = document.getElementById("dropdown-menu-tasks")
    let options = menu.querySelectorAll('.dropdown-item');
    options.forEach(option => {
      option.remove()
    });

    let table = document.getElementById("table-task")
    let tbody = table.getElementsByTagName("tbody")[0]
    let rows = tbody.getElementsByTagName("tr")

    let innerHTMLs = []

    for (let i = 0; i < rows.length; i++) {
        let name = rows[i].getElementsByTagName("td")[0].textContent.replace("-", "",).trim()
        let equipe = rows[i].getElementsByTagName("td")[1]
        let zone = rows[i].getElementsByTagName("td")[2]

        innerHTMLs.push(name + "-" + equipe.textContent + "-" + zone.textContent);
    }

    options = JSON.stringify(
        {
        'options': innerHTMLs,
        }
    )
    $.ajax({
        type: 'POST',
        url: '/edit-db/get-tasks',
        data: {
        'options': options,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            let opts = response
            opts = JSON.parse(opts)
            for (let i=0 ; i < opts.length; i++) {
                let li = document.createElement("li")
                let a = document.createElement("a")
                a.className = "dropdown-item";
                a.innerHTML = opts[i].name + "-" + opts[i].equipe + "-" + opts[i].zone;
                li.appendChild(a);
                li.style.textAlign = "right"
                menu.appendChild(li);
            }

            search_tasks();

        }
    });


}

function del_report(reportID){
    $.ajax({
        type: 'POST',
        url: '/edit-db/del-daily-report/',
        data: {
            "id" : reportID,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            // location.reload(true);
            document.getElementById("table-"+reportID).remove();
            iter_reports();
        }
    });

}

function edit_report(reportID){
    $.ajax({
        type: 'POST',
        url: '/edit-db/edit-daily-report/',
        data: {
            "template" : true,
            "id" : reportID,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            // location.reload(true);
            iter_reports();
        }
    });

}

function fetch_units(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-units/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["units"])

            callback(opts)
        }
    });
}

function fetch_operations(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-operations/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["operations"])

            callback(opts)
        }
    });
}

function fetch_all_equipes(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-all-equipes/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["equipes"])

            callback(opts)
        }
    });
}

function fetch_suboperations(opr, callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-suboperations/',
        data: {
            "operation": opr
        },
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["suboperations"])

            callback(opts)
        }
    });
}

function fetch_zoneoperations(opr, callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-zoneoperations/',
        data: {
            "operation": opr
        },
        success: function(response) {
            let opts = response
            // opts = JSON.parse(opts["zoneoperations"])
            opts = opts["zoneoperations"]

            callback(opts)
        }
    });
}

function fetch_zones(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-zones/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["zones"])

            callback(opts)
        }
    });
}

function fetch_materialproviders(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-materialproviders/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["materialproviders"])

            callback(opts)
        }
    });
}

function fetch_machineproviders(callback) {
    $.ajax({
        type: 'GET',
        url: '/edit-db/get-machineproviders/',
        success: function(response) {
            let opts = response

            opts = JSON.parse(opts["machineproviders"])

            callback(opts)
        }
    });
}

function toggle_requirement(toggleID, conditionID) {
    let select = document.getElementById(toggleID)
    let input = document.getElementById(conditionID)
    input.style.borderRadius = "0"
    input.style.textAlign = "center"
    if (input.value == 0) {
        select.required = false
    } else if (input.value > 0) {
        select.required = true
    }

}

function iter_reports() {
    let btns = document.querySelectorAll('.btn-danger')
    let btn = btns[btns.length - 1]
    $.ajax({
        type: 'POST',
        url: '/edit-db/check-deletability/',
        data: {
            "id" : btn.id,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            if (response=="True") {
                btn.disabled = false;
            } else {
                btn.disabled = true;
            }

        }
    });

    let btns2 = document.querySelectorAll('.btn-primary')
    let btn2 = btns2[btns2.length - 1]
    $.ajax({
        type: 'POST',
        url: '/edit-db/check-editability/',
        data: {
            "id" : btn2.id,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            if (response=="True") {
                btn2.disabled = false;
            } else {
                btn2.disabled = true;
            }

        }
    });
}

function shortcut_add(which, ) {
    if (which == "position") {
        let value = document.getElementById("shortcut_position").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_position").value = ""

    } else if (which == "profession") {
        let value = document.getElementById("shortcut_profession").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_profession").value = ""
    }
    else if (which == "machine") {
        let value = document.getElementById("shortcut_machine").value
        let type = document.getElementById("shortcut_machineType").value
        shortcut_add_to_base(which, value, type);
        document.getElementById("shortcut_machine").value = ""
    }
    else if (which == "material") {
        let value = document.getElementById("shortcut_material").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_material").value = ""
    }
    else if (which == "contractor") {
        let value = document.getElementById("shortcut_contractor").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_contractor").value = ""
    }
    else if (which == "zone") {
        let value = document.getElementById("shortcut_zone").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_zone").value = ""
    }
    else if (which == "unit") {
        let value = document.getElementById("shortcut_unit").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_unit").value = ""
    }
    else if (which == "materialprovider") {
        let value = document.getElementById("shortcut_materialprovider").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_materialprovider").value = ""
    }
    else if (which == "machineprovider") {
        let value = document.getElementById("shortcut_machineprovider").value
        shortcut_add_to_base(which, value);
        document.getElementById("shortcut_machineprovider").value = ""
    }
    else if (which == "") {

    }
    else if (which == "") {

    }

}

function shortcut_add_to_base(which, value, type=null) {
    if (!value) {
        return 0
    } else if (!type && which == "machine")  {
        return 0
    }

    $.ajax({
            type: 'POST',
            url: '/edit-db/shortcut-add',
            data: {
            "which": which,
            "value": value,
            'type': type,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                if (response == "True") {
                    alert("با موفقیت اضافه شد");
                } else {
                    alert("مشکلی پیش آمد. به پشتیبانی اطلاع دهید");
                }
            }
        });

}

function shortcut_add_to_base_2(which, value, type=null) {
    if (!value) {
        return 0
    } else if (!type && which == "machine")  {
        return 0
    }

    $.ajax({
            type: 'POST',
            url: '/edit-db/shortcut-add',
            data: {
            "which": which,
            "value": value,
            'type': type,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                if (response == "True") {
                    alert("با موفقیت اضافه شد");
                } else {
                    alert("مشکلی پیش آمد. به پشتیبانی اطلاع دهید");
                }
            }
    });

}

function check_report_date() {
    let date = document.getElementById("date")

    $.ajax({
            type: 'POST',
            url: '/home/daily-reports/check-existence',
            data: {
            "date": date.value,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                if (response == "True") {
                    alert("برای تاریخ " + date.value.split(" ")[0] + " قبلا گزارشی ثبت شده است. به آرشیو گزارشات مراجعه فرمایید.");
                    date.value = ""
                } else {
                    // alert("مشکلی پیش آمد. به پشتیبانی اطلاع دهید");
                }
            }
    });

}

function confirmZeroValues() {
    const fields = document.querySelectorAll('input[type="number"]');

    for (let i = 0; i < fields.length; i++) {
      if (fields[i].value === "0") {
          fields[i].style.borderColor = "red"
      }
    }
    for (let i = 0; i < fields.length; i++) {
      if (fields[i].value === "0") {
          console.log("waiting...")
      }
    }
    const confirmed = confirm("مواردی که با کادر قرمز نشان داده میشوند، مقداردهی 0 شده اند. تایید میکنید؟");
    if (!confirmed) {
      return false;
    }
    return true;
}

function update_live_total_done(live) {
    let target = document.getElementById('live_total_done_'+live)
    target.innerHTML = parseFloat(document.getElementById(live).value) + parseFloat(document.getElementById('doneVolume_'+live).innerHTML)
}





function submitForm(ID, type, shortcut=null,) {
    if (type === "suboperation") {
        var target = "form-" + ID
    }
    else if (type === "operation") {
        var target = "add-operation"
    }
    else if (type === "zoneoperation") {
        var target = "form-zone-" + ID
    }
    else if (type === "task") {
        var target = "form-task"
    }
    else if (type === "task-shortcut") {
        type = "task"
        var target = "form-task-shortcut"
    }
    else if (type === "task_in_report") {
        var target = "form-task_in_report"
    }
    else if (type === "position") {
        var target = "form-position"
    }
    else if (type === "profession") {
        var target = "form-profession"
    }
    else if (type === "machine") {
        var target = "form-machine"
    }
    else if (type === "material") {
        var target = "form-material"
    }
    else if (type === "contractor") {
        var target = "form-contractor"
    }
    else if (type === "equipe") {
        var target = "form-equipe"
    }
    else if (type === "zone") {
        var target = "form-zone"
    }
    else if (type === "materialprovider") {
        var target = "form-materialprovider"
    }
    else if (type === "machineprovider") {
        var target = "form-machineprovider"
    }
    else if (type === "unit") {
        var target = "form-unit"
    }
    $('#'+target).submit(function(event) {
        // Prevent form submission
        event.preventDefault();

        // Collect form data
        var formData = new FormData(this);

        if (type === "task_in_report") {
            let opr = formData.get("operation")
            let subopr = formData.get("suboperation")
            let zoneopr = formData.get("zoneoperation")
            let equipe = formData.get("equipe")
            let unit = formData.get("unit")

            let select = document.getElementById("select2-equipe")

            // $.ajax({
            //     url: '/edit-db/get-equipes-in-report/',
            //     type: 'POST',
            //     data: {
            //         'operation': opr,
            //         'suboperation': subopr,
            //         'zone': zoneopr,
            //     },
            //     beforeSend: function(xhr, settings) {
            //     xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            //     },
            //     success: function(response) {
            //         let tasks = JSON.parse(response['tasks'])
            //
            //         $("#select2-equipe").empty().append(
            //             '<option value="" selected disabled>انتخاب اکیپ</option>'
            //         )
            //         for (let i=0; i<tasks.length; i++) {
            //             let splitted = tasks[i].unique_str.split("-")
            //
            //             let option = document.createElement("option")
            //             option.value = splitted[2] + "-" + splitted[3]
            //             option.innerText = splitted[2] + "-" + splitted[3]
            //
            //             select.appendChild(option)
            //         }
            //
            //     }
            // })

            $("#select2-equipe").empty().append(
                '<option value="" selected disabled>انتخاب اکیپ</option>'
            )
            // fetch_all_equipes(function (equipes) {
            //     equipes.forEach(equipe => {
            //         let option = document.createElement('option',)
            //         option.value = equipe.name
            //         option.innerHTML = equipe.name
            //         select.appendChild(option)
            //     })
            // })
            // $('#select2-equipe').select2({
            //     dropdownParent: $("#equipe-box")
            // });

            let select2 = document.getElementById("select2-zoneoperation")
            $("#select2-zoneoperation").empty().append(
                '<option value="" selected disabled>انتخاب موقعیت عملیات</option>'
            )
            fetch_zoneoperations(opr, function (zoneoperations) {
                zoneoperations.forEach(zoneoperation => {
                    let option = document.createElement('option',)
                    option.value = zoneoperation.zone
                    option.innerHTML = zoneoperation.zone
                    select2.appendChild(option)
                })
            })
            $('#select2-zoneoperation').select2({
                dropdownParent: $("#zoneoperation-box")
            });

            if (
                document.getElementById(opr + "-" + subopr + "-" + equipe + "-" + zoneopr)
            ) {
                alert('عملیات انتخابی در جدول وجود دارد')

                return 0
            }

            $.ajax({
                url: '/edit-db/get-subtask-in-report/',
                type: 'POST',
                data: {
                    'operation': opr,
                    'suboperation': subopr,
                    'zone': zoneopr,
                    'equipe': equipe,
                },
                beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
                },
                success: function(response) {
                    response = response[0]

                    let table = document.getElementById("table-task")
                    let tbody = table.querySelector("tbody")

                    let newRow = document.createElement("tr")
                    newRow.id =  opr + "-" + subopr + "-" + equipe + "-" + zoneopr

                    for (let i=0; i<10; i++) {
                        let td = document.createElement('td')
                        switch (i) {
                            case 0:
                                td.innerText = response.operation.name

                                let span = document.createElement('span',);
                                Object.assign(span.style, {
                                    float: 'right',
                                    color: 'black',
                                });
                                span.className = "badge rounded-pill";
                                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                                span.style.marginLeft = "5pt"
                                span.addEventListener('click', function () {
                                    del_task_in_report(
                                        opr,
                                        subopr,
                                        equipe,
                                        zoneopr,
                                        false,
                                    );
                                });
                                td.appendChild(span)
                                newRow.appendChild(td)

                                break;
                            case 1:
                                td.innerText = response.suboperation.name
                                newRow.appendChild(td)

                                break;
                            case 2:
                                td.innerText = response.equipe
                                newRow.appendChild(td)

                                break;
                            case 3:
                                td.innerText = response.zone
                                newRow.appendChild(td)

                                break;
                            case 4:
                                td.className = "text-centred"
                                let input = document.createElement('input')
                                input.required = true
                                input.className = "small-input-integer"
                                input.style = "border-radius: 0; text-align: center;"
                                input.id = "task_"+newRow.id+"_today"
                                input.name = "task_"+newRow.id+"_today"
                                input.min = '0'
                                input.max = response.freeVolume
                                input.value = '0'
                                input.type = 'number'
                                input.addEventListener('keyup', function () {
                                    update_live_total_done(
                                        "task_"+newRow.id+"_today"
                                    )
                                })
                                td.appendChild(input)
                                newRow.appendChild(td)

                                break;
                            case 5:
                                td.className = "text-centred"
                                td.innerText = response.doneVolume
                                td.id = "doneVolume_task_" + opr + "-" + subopr + "-" + equipe + "-" + zoneopr + "_today"
                                newRow.appendChild(td)

                                break;
                            case 6:
                                td.className = "text-centred"
                                td.id = "live_total_done_task_" + opr + "-" + subopr + "-" + equipe + "-" + zoneopr + "_today"

                                newRow.appendChild(td)

                                break;
                            case 7:
                                td.className = "text-centred"
                                td.innerText = response.totalVolume
                                newRow.appendChild(td)

                                break;
                            case 8:
                                td.className = "text-centred"
                                td.innerText = response.donePercentage
                                newRow.appendChild(td)

                                break;
                            case 9:
                                td.className = "text-centred"
                                td.innerText = response.unit
                                newRow.appendChild(td)

                                break;

                        }
                    }
                    tbody.appendChild(newRow)
                }
            })

            return 0
        }

        // Send AJAX request
        $.ajax({
        url: '/edit-db/add-' + type,
        type: 'POST',
        data: formData,
        dataType: 'json',
        contentType: false,
        processData: false,
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {

            if (shortcut) {
                alert("با موفقیت افزوده شد")
                let form = document.getElementById(target);
                for (const pair of formData.entries()) {
                  // Get the input element by name
                  const inputName = pair[0];
                  const input = form.elements[inputName];

                  // Reset the value of the input field
                  input.value = '';
                }

                handle_select(type+"-shortcut")

                return 0
            }

            if ( type === "suboperation" ) {
                let table = document.getElementById("table-" + ID)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = "suboperation-" + document.getElementById('suboperation-name-' + ID).value + "-" + ID;


                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerHTML = document.getElementById('suboperation-name-' + ID).value;

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'right',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.style.marginLeft = "5pt"
                let val = document.getElementById('suboperation-name-' + ID).value
                span.addEventListener('click', function () {
                    del_suboperation(
                        val,
                        ID,
                        true
                    );
                });
                cell1.appendChild(span)


                let cell2 = document.createElement('td',);
                cell2.className = "";
                cell2.innerHTML = document.getElementById('select2-' + document.getElementById('suboperation-operation-' + ID).value).value

                let cell3 = document.createElement('td',);
                cell3.className = "";
                cell3.innerHTML = document.getElementById('suboperation-amount-' + ID).value;

                let cell4 = document.createElement('td',);
                cell4.className = "weights-" + ID;
                cell4.innerHTML = document.getElementById('suboperation-weight-' + ID).value;

                newRow.appendChild(cell1)
                newRow.appendChild(cell4)
                newRow.appendChild(cell3)
                newRow.appendChild(cell2)

                tbody.appendChild(newRow)

                let weights = document.getElementsByClassName("weights-" + ID)
                let sum = 0.0
                for (let i = 0; i < weights.length; i++) {
                    sum += parseFloat(weights[i].innerText.trim())
                }
                let cell = document.getElementById(
                    "suboperation-weight-" + ID
                )
                cell.max = 100 - sum
            }
            else if ( type === "operation" ) {
                let table = document.getElementById("table-operation")
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = document.getElementById("operation-name").value;


                let cell1 = document.createElement('td',);
                cell1.className = "";
                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                let val = document.getElementById("operation-name").value
                span.addEventListener('click', function () {
                    del_operation(
                        val,
                        true
                    );
                });

                let span2 = document.createElement('span',);
                Object.assign(span2.style, {
                    float: 'right',
                    color: 'black',
                });
                span2.className = "badge rounded-pill";
                span2.innerHTML = '<img src="/static/icons/list-task.svg" style="-webkit-transform: scaleX(-1); transform: scaleX(-1);"/>';
                span2.setAttribute('data-bs-toggle', 'modal');
                span2.setAttribute('data-bs-target', '#staticBackdropSubOperations-'+response);

                let span3 = document.createElement('span',);
                Object.assign(span2.style, {
                    float: 'right',
                    color: 'black',
                });
                span3.className = "badge rounded-pill";
                span3.innerHTML = '<img src="/static/icons/grid-1x2.svg"/>';
                span3.setAttribute('data-bs-toggle', 'modal');
                span3.setAttribute('data-bs-target', '#staticBackdropZoneOperations-'+response);

                cell1.innerText = document.getElementById("operation-name").value;

                cell1.appendChild(span)
                let temp = document.createElement('div')
                temp.style.display = "inline-block"
                Object.assign(temp.style, {
                    float: 'right',
                    color: 'black',
                });
                temp.appendChild(span2)
                temp.appendChild(span3)
                cell1.appendChild(temp)
                // cell1.appendChild()


                let cell2 = document.createElement('td',);
                cell2.className = "";
                cell2.style.width = "20%"
                cell2.innerHTML = document.getElementById("unitforoperation-name").value

                let cell3 = document.createElement('td',);
                cell3.className = "";
                cell3.style.width = "20%"
                cell3.innerHTML = document.getElementById("unitforoperation-amount").value

                newRow.appendChild(cell1)
                newRow.appendChild(cell2)
                newRow.appendChild(cell3)

                tbody.appendChild(newRow)

                createModal(
                    'suboperation',
                    response,
                    document.getElementById("operation-name").value,
                    document.getElementById("unitforoperation-amount").value,
                    document.getElementById("unitforoperation-name").value,
                )

                createModal(
                    'zoneoperation',
                    response,
                    document.getElementById("operation-name").value,
                    document.getElementById("unitforoperation-amount").value,
                    document.getElementById("unitforoperation-name").value,
                )

                let selects = document.getElementsByTagName("select")
                for (let i=0; i<selects.length; i++) {
                    if (selects[i].id === "select2-operation") {
                        let id = selects[i].id
                        $("#"+id).empty().append(
                            '<option value="" selected disabled>انتخاب عملیات اصلی</option>'
                        )
                        fetch_operations(function (operations) {
                            operations.forEach(operation => {
                                let option = document.createElement('option',)
                                option.value = operation.name
                                option.innerHTML = operation.name
                                selects[i].appendChild(option)
                            });
                        });
                        // $('#'+id).select2({
                        //     dropdownParent: $("#equipe-box")
                        // });
                    }
                }

            }
            else if (type === "zoneoperation") {
                let table = document.getElementById("table-zone-" + ID)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = "zoneoperation-" + document.getElementById('select2-zone-' + ID).value + "-" + ID;


                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerHTML = document.getElementById('select2-zone-' + ID).value;
                cell1.setAttribute('colspan', '2')

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'right',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.style.marginLeft = "5pt"
                let val = document.getElementById('select2-zone-' + ID).value
                span.addEventListener('click', function () {
                    del_zoneoperation(
                        val,
                        ID,
                        true
                    );
                });
                cell1.appendChild(span)


                // let cell2 = document.createElement('td',);
                // cell2.className = "";
                // cell2.innerHTML = document.getElementById('select2-' + document.getElementById('suboperation-operation-' + ID).value).value

                let cell3 = document.createElement('td',);
                cell3.className = "amounts-" + ID;
                cell3.innerHTML = document.getElementById('zoneoperation-amount-' + ID).value;

                let cell4 = document.createElement('td',);
                cell4.className = ""
                cell4.innerHTML = document.getElementById("total-unit-" + ID).innerText.trim();

                newRow.appendChild(cell1)
                newRow.appendChild(cell3)
                newRow.appendChild(cell4)

                tbody.appendChild(newRow)

                let amounts = document.getElementsByClassName("amounts-" + ID)
                let sum = 0.0
                for (let i = 0; i < amounts.length; i++) {
                    sum += parseFloat(amounts[i].innerText.trim())
                }
                let cell = document.getElementById(
                    "zoneoperation-amount-" + ID
                )
                cell.max = parseFloat(document.getElementById("total-amount-"+ID).innerText) - sum

            }
            else if (type === "task") {
                if ( response === false) {
                    alert(
                        "این مورد قبلا ایجاد شده است"
                    )
                    return 0
                }

                if (target.includes("shortcut")) {

                    alert("با موفقیت اضافه شد")

                    let opr = document.getElementById("select2-operation-shortcut").value
                    // let subopr = document.getElementById("select2-suboperation-shortcut").value
                    let equipe = document.getElementById("select2-equipe-shortcut").value
                    let zone = document.getElementById("select2-zoneoperation-shortcut").value
                    let amount = document.getElementById("task-volume-shortcut").value
                    let unit = document.getElementById("task-unit-shortcut").value

                    let select = document.getElementById("select2-equipe-shortcut")
                    $("#select2-equipe-shortcut").empty().append(
                        '<option value="" selected disabled>انتخاب اکیپ</option>'
                    )
                    fetch_all_equipes(function (equipes) {
                        equipes.forEach(equipe => {
                            let option = document.createElement('option',)
                            option.value = equipe.name
                            option.innerHTML = equipe.name
                            select.appendChild(option)
                        })
                    })
                    $('#select2-equipe-shortcut').select2({
                        dropdownParent: $("#equipe-box-shortcut")
                    });

                    let select2 = document.getElementById("select2-zoneoperation-shortcut")
                    $("#select2-zoneoperation-shortcut").empty().append(
                        '<option value="" selected disabled>انتخاب موقعیت عملیات</option>'
                    )
                    fetch_zoneoperations(opr, function (zoneoperations) {
                        zoneoperations.forEach(zoneoperation => {
                            let option = document.createElement('option',)
                            option.value = zoneoperation.zone
                            option.innerHTML = zoneoperation.zone
                            select2.appendChild(option)
                        })
                    })
                    $('#select2-zoneoperation-shortcut').select2({
                        dropdownParent: $("#zoneoperation-box-shortcut")
                    });

                    let temp = document.getElementById("task-volume-shortcut")
                    temp.value = ""
                    temp.setAttribute('placeholder' , "مقدار")


                    return 0
                }

                let opr = document.getElementById("select2-operation").value
                // let subopr = document.getElementById("select2-suboperation").value
                let equipe = document.getElementById("select2-equipe").value
                let zone = document.getElementById("select2-zoneoperation").value
                let amount = document.getElementById("task-volume").value
                let unit = document.getElementById("task-unit").value


                let table = document.getElementById("table-task")
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = opr + "-" + equipe + "-" + zone ;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.style.width = "45%"
                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                let val = opr + "-" + equipe + "-" + zone ;
                span.addEventListener('click', function () {
                    del_task(
                        opr, equipe, zone,true
                    );
                });

                let span2 = document.createElement('span',);
                Object.assign(span2.style, {
                    float: 'right',
                    color: 'black',
                });
                span2.className = "badge rounded-pill";
                span2.innerHTML = '<img src="/static/icons/list-task.svg" style="-webkit-transform: scaleX(-1); transform: scaleX(-1);"/>';
                span2.setAttribute('data-bs-toggle', 'modal');
                span2.setAttribute('data-bs-target', '#staticBackdropSubTasks-'+response);

                cell1.innerText = opr

                cell1.appendChild(span)
                cell1.appendChild(span2)


                let cell3 = document.createElement('td',);
                cell3.className = "";
                cell3.style.width = "18%"
                cell3.innerHTML = equipe

                let cell4 = document.createElement('td',);
                cell4.className = "";
                cell4.style.width = "17%"
                cell4.innerHTML = zone

                let cell5 = document.createElement('td',);
                cell5.className = "";
                cell5.style.width = "10%"
                cell5.innerHTML = amount

                let cell6 = document.createElement('td',);
                cell6.className = "";
                cell6.style.width = "10%"
                cell6.innerHTML = unit

                newRow.appendChild(cell1)
                // newRow.appendChild(cell2)
                newRow.appendChild(cell3)
                newRow.appendChild(cell4)
                newRow.appendChild(cell6)
                newRow.appendChild(cell5)

                tbody.appendChild(newRow)

                // handle_select('zone')

                let select = document.getElementById("select2-equipe")
                $("#select2-equipe").empty().append(
                    '<option value="" selected disabled>انتخاب اکیپ</option>'
                )
                fetch_all_equipes(function (equipes) {
                    equipes.forEach(equipe => {
                        let option = document.createElement('option',)
                        option.value = equipe.name
                        option.innerHTML = equipe.name
                        select.appendChild(option)
                    })
                })
                $('#select2-equipe').select2({
                    dropdownParent: $("#equipe-box")
                });

                let select2 = document.getElementById("select2-zoneoperation")
                $("#select2-zoneoperation").empty().append(
                    '<option value="" selected disabled>انتخاب موقعیت عملیات</option>'
                )
                fetch_zoneoperations(opr, function (zoneoperations) {
                    zoneoperations.forEach(zoneoperation => {
                        let option = document.createElement('option',)
                        option.value = zoneoperation.zone
                        option.innerHTML = zoneoperation.zone
                        select2.appendChild(option)
                    })
                })
                $('#select2-zoneoperation').select2({
                    dropdownParent: $("#zoneoperation-box")
                });

                let temp = document.getElementById("task-volume")
                temp.value = ""
                temp.setAttribute('placeholder' , "مقدار")

                createModal(
                    "subtask",
                    response,
                    opr,
                    amount,
                    unit,
                    zone,
                    equipe,
                )



            }
            else if (type === "position") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""
                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_position(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)


            }
            else if (type === "profession") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""
                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_profession(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "machine") {
                let input = document.getElementById("input-" + type)
                let machine = document.getElementById('machineType')
                let value = input.value
                let machineType = machine.value
                input.value = ""
                machine.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_machine(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "material") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_material(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "contractor") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_contractor(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "equipe") {
                let prof = document.getElementById("equipe-profession-name")
                let cont = document.getElementById("equipe-contractor-name")
                let prof_value = prof.value
                let cont_value = cont.value
                prof.value = ""
                cont.value = ""
                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = prof_value + "-" + cont_value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = prof_value + "-" + cont_value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_equipe(
                        prof_value,
                        cont_value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)

                let selects = document.getElementsByTagName("select")
                for (let i=0; i<selects.length; i++) {
                    if (selects[i].id === "select2-equipe") {
                        let id = selects[i].id
                        $("#"+id).empty().append(
                            '<option value="" selected disabled>انتخاب اکیپ</option>'
                        )
                        fetch_all_equipes(function (equipes) {
                            equipes.forEach(equipe => {
                                let option = document.createElement('option',)
                                option.value = equipe.name
                                option.innerHTML = equipe.name
                                selects[i].appendChild(option)
                            });
                        });
                        // $('#'+id).select2({
                        //     dropdownParent: $("#equipe-box")
                        // });

                    }
                }
            }
            else if (type === "zone") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_zone(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)

                let selects = document.getElementsByTagName("select")
                for (let i=0; i<selects.length; i++) {
                    if (selects[i].id.includes("select2-zone-")) {
                        let id = selects[i].id
                        $("#"+id).empty().append(
                            '<option value="" selected disabled>انتخاب</option>'
                        )
                        fetch_zones(function (zones) {
                            zones.forEach(zone => {
                                let option = document.createElement('option',)
                                option.value = zone.name
                                option.innerHTML = zone.name
                                selects[i].appendChild(option)
                            });
                        });
                        // $('#'+id).select2({
                        //     dropdownParent: $("#equipe-box")
                        // });

                    }
                }
            }
            else if (type === "materialprovider") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_materialprovider(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "machineprovider") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_machineprovider(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }
            else if (type === "unit") {
                let input = document.getElementById("input-" + type)
                let value = input.value
                input.value = ""

                let table = document.getElementById("table-" + type)
                let tbody = table.querySelector("tbody")

                let newRow = document.createElement('tr');
                newRow.id = value;

                let cell1 = document.createElement('td',);
                cell1.className = "";
                cell1.innerText = value

                let span = document.createElement('span',);
                Object.assign(span.style, {
                    float: 'left',
                    color: 'black',
                });
                span.className = "badge rounded-pill";
                span.innerHTML = '<img src="/static/icons/patch-minus.svg"/>';
                span.addEventListener('click', function () {
                    del_unit(
                        value,
                        true
                    );
                });
                cell1.appendChild(span)

                newRow.appendChild(cell1)

                tbody.appendChild(newRow)
            }


            alert("با موفقیت افزوده شد")

        },
        error: function(xhr, status, error) {
            alert("مشکلی در ارتباط با سرور ایجاد شده است:" + "\n" + error)
          // console.error(error);
        }
        });
    });
}

function del_suboperation(sub, opr, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-suboperation',
            data: {
            "suboperation": sub,
            "operation": opr,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                if (response == "True") {
                    let id = "suboperation-" + sub + "-" + opr
                    let row = document.getElementById(id)
                    row.remove();
                    alert(" با موفقیت حذف شد");

                    let weights = document.getElementsByClassName("weights-"+opr)

                    let sum = 0.0
                    for (let i=0; i < weights.length; i++) {
                        sum += parseFloat(weights[i].innerText.trim())
                    }
                    let cell = document.getElementById(
                        "suboperation-weight-" + opr
                    )
                    cell.max = 100 - sum

                } else {
                    alert("مشکلی در حذف بوجود آمده است.");
                }
            }
        });
    } else {

    }
}

function del_zoneoperation(zone, opr, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-zoneoperation',
            data: {
            "zoneoperation": zone,
            "operation": opr,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                if (response == "True") {
                    let id = "zoneoperation-" + zone + "-" + opr
                    let row = document.getElementById(id)
                    row.remove();

                    alert(" با موفقیت حذف شد");

                    let amounts = document.getElementsByClassName("amounts-"+opr)

                    let sum = 0.0
                    for (let i=0; i < amounts.length; i++) {
                        sum += parseFloat(amounts[i].innerText.trim())
                    }
                    let cell = document.getElementById(
                        "zoneoperation-amount-" + opr
                    )
                    cell.max = parseFloat(document.getElementById("total-amount-"+opr).innerText) - sum

                } else {
                    alert("مشکلی در حذف بوجود آمده است.");
                }
            }
        });
    } else {

    }
}

function createModal(type, ID, opr_name, opr_amount, opr_unit, zone=null, equipe=null) {
    if (type === 'suboperation') {
        let container = document.getElementById("main-container")

        let div_modal = document.createElement("div")
        div_modal.className = "modal fade"
        div_modal.id = "staticBackdropSubOperations-"+ID
        div_modal.setAttribute("data-bs-backdrop", "static")
        div_modal.setAttribute("data-bs-keyboard", "false")
        div_modal.setAttribute("tabindex", "-1")

        let div_modal_dialog = document.createElement("div")
        div_modal_dialog.className = "modal-dialog"

        let div_modal_content = document.createElement("div")
        div_modal_content.className = "modal-content"

        let div_modal_header = document.createElement("div")
        div_modal_header.className = "modal-header"

        let close_modal = document.createElement("button")
        close_modal.className = "btn-close"
        close_modal.setAttribute("data-bs-dismiss", "modal")
        close_modal.setAttribute("aria-label", "Close")

        let modal_title = document.createElement("h5")
        modal_title.className = "modal-title"
        modal_title.id = "staticBackdropSubOperationsLabel-"+ID
        modal_title.style.marginRight = "auto"
        modal_title.innerText = "زیرعملیات های " + opr_name

        let div_modal_body = document.createElement("div")
        div_modal_body.className = "modal-body"

        let div_input_group_01 = document.createElement("div")
        div_input_group_01.className = "input-group mb-3"

        let table = document.createElement("table")
        table.className = "table table-bordered border-dark"
        table.id = "table-" + ID
        table.style.fontSize = "11px"

        let thead01 = document.createElement("thead")
        thead01.className = ""
        let thead01_row = document.createElement("tr")
        let thead01_row_td01 = document.createElement("th")
        let thead01_row_td02 = document.createElement("th")
        let thead01_row_td03 = document.createElement("th")
        thead01_row_td01.style.textAlign = "center"
        thead01_row_td02.style.textAlign = "center"
        thead01_row_td03.style.textAlign = "center"

        thead01_row_td01.setAttribute("colspan", "2")
        thead01_row_td02.setAttribute("colspan", "1")
        thead01_row_td03.setAttribute("colspan", "1")

        thead01_row_td01.innerText = opr_name
        thead01_row_td02.innerText = opr_amount
        thead01_row_td03.innerText = opr_unit



        let thead02 = document.createElement("thead")
        thead02.className = ""
        let thead02_row = document.createElement("tr")
        let thead02_row_td01 = document.createElement("th")
        let thead02_row_td02 = document.createElement("th")
        let thead02_row_td03 = document.createElement("th")
        let thead02_row_td04 = document.createElement("th")
        thead02_row_td02.style.width = "20%"
        thead02_row_td03.style.width = "20%"
        thead02_row_td04.style.width = "20%"

        thead02_row_td01.innerText = "شرح زیرعملیات"
        thead02_row_td02.innerText = "وزن %"
        thead02_row_td03.innerText = "مقدار"
        thead02_row_td04.innerText = "واحد"



        let tbody = document.createElement("tbody")
        // let temp = document.createElement("tr")
        // tbody.appendChild(temp)

        let form = document.createElement("form")
        form.id = "form-"+ID

        let div_input_group_02 = document.createElement("div")
        div_input_group_02.className = "input-group mb-3"

        let table_form = document.createElement("table")
        table_form.style.fontSize = "11px"

        let thead_form =  document.createElement("thead")

        let input_id = document.createElement("input")
        input_id.hidden = true
        input_id.value = ID
        input_id.name = "operation-id"
        input_id.id = "suboperation-operation-" + ID
        input_id.required = true

        let th01 = document.createElement("th")
        th01.style = "width: 187px; background-color: white; border: solid black 1px;"

        let input_subopr_name = document.createElement("input")
        input_subopr_name.style = "outline: none; background-color: white; border: none; width: 100%; padding: 3px;"
        input_subopr_name.id = "suboperation-name-" + ID
        input_subopr_name.placeholder = "نام زیرعملیات"
        input_subopr_name.name = "name"
        input_subopr_name.required = true


        let th02 = document.createElement("th")
        th02.style = "width: 93px; background-color: white; border: solid black 1px;"

        let input_subopr_weight = document.createElement("input")
        input_subopr_weight.style = "outline: none; background-color: white; border: none; width: 100%; padding: 3px;"
        input_subopr_weight.id = "suboperation-weight-" + ID
        input_subopr_weight.placeholder = "وزن %"
        input_subopr_weight.type = "number"
        input_subopr_weight.name = "weight"
        input_subopr_weight.min = "0"
        input_subopr_weight.max = "100.0"
        input_subopr_weight.required = true

        let th03 = document.createElement("th")
        th03.style = "width: 93px; background-color: white; border: solid black 1px;"

        let input_subopr_amount = document.createElement("input")
        input_subopr_amount.style = "outline: none; background-color: white; border: none; width: 100%; padding: 3px;"
        input_subopr_amount.id = "suboperation-amount-" + ID
        input_subopr_amount.placeholder = "مقدار"
        input_subopr_amount.type = "number"
        input_subopr_amount.required = true
        input_subopr_amount.name = 'amount'


        let div_unit_box = document.createElement("div")
        div_unit_box.style = "width: 90px;"
        div_unit_box.id = "unit-box-" + ID

        let select_units = document.createElement('select')
        select_units.required = true
        select_units.className = "select2"
        select_units.id = "select2-"+ ID
        select_units.name = "unit"
        select_units.style = "width: 90px; border: solid black"
        // select_units.on('click', function() {
        //     findselect2(ID);
        // });

        let choose_option = document.createElement('option')
        choose_option.disabled = true
        choose_option.selected = true
        choose_option.value = ""
        choose_option.innerText = "انتخاب"

        select_units.appendChild(choose_option)
        fetch_units(function (units) {
            units.forEach(unit => {
                let option = document.createElement('option',)
                option.value = unit.name
                option.innerText = unit.name
                select_units.appendChild(option)
            })
        })
        div_unit_box.appendChild(select_units)

        let btn_submit = document.createElement("button")
        btn_submit.className = "btn btn-outline-success bp3-round w-100"
        btn_submit.type = "submit"
        btn_submit.innerText = "افزودن"

        let div_modal_footer = document.createElement("div")
        div_modal_footer.className = "modal-footer"

        let btn_cmplt = document.createElement("button")
        btn_cmplt.type = "button"
        btn_cmplt.className = "btn btn-outline-warning w-100"
        btn_cmplt.setAttribute('data-bs-dismiss', 'modal')
        btn_cmplt.innerText = "تکمیل"

        // ==================================================
        // --------------------------------------------------
        thead01_row.appendChild(thead01_row_td01)
        thead01_row.appendChild(thead01_row_td02)
        thead01_row.appendChild(thead01_row_td03)

        thead01.appendChild(thead01_row)
        // --------------------------------------------------

        // --------------------------------------------------
        thead02_row.appendChild(thead02_row_td01)
        thead02_row.appendChild(thead02_row_td02)
        thead02_row.appendChild(thead02_row_td03)
        thead02_row.appendChild(thead02_row_td04)

        thead02.appendChild(thead02_row)
        // --------------------------------------------------

        // --------------------------------------------------
        th01.appendChild(input_subopr_name)
        th02.appendChild(input_subopr_weight)
        th03.appendChild(input_subopr_amount)

        thead_form.appendChild(input_id)
        thead_form.appendChild(th01)
        thead_form.appendChild(th02)
        thead_form.appendChild(th03)

        table_form.appendChild(thead_form)

        div_input_group_02.appendChild(table_form)
        div_input_group_02.appendChild(div_unit_box)

        form.appendChild(div_input_group_02)
        form.appendChild(btn_submit)
        // --------------------------------------------------

        // --------------------------------------------------
        table.appendChild(thead01)
        table.appendChild(thead02)
        table.appendChild(tbody)

        div_input_group_01.appendChild(table)
        div_input_group_01.appendChild(form)
        // --------------------------------------------------
        // ==========================================================

        // ==========================================================
        div_modal_footer.appendChild(btn_cmplt)
        // ==========================================================

        // ==========================================================
        div_modal_body.appendChild(div_input_group_01)
        div_modal_body.appendChild(div_modal_footer)
        // ==========================================================

        // ==========================================================
        div_modal_header.appendChild(close_modal)
        div_modal_header.appendChild(modal_title)

        div_modal_content.appendChild(div_modal_header)
        div_modal_content.appendChild(div_modal_body)
        // ==========================================================

        // ==========================================================
        div_modal_dialog.appendChild(div_modal_content)
        div_modal.appendChild(div_modal_dialog)
        container.appendChild(div_modal)
        // ==========================================================

        $('#select2-'+ID).select2({
            dropdownParent: $("#unit-box-"+ID)
        });

        submitForm(ID, 'suboperation')
    }
    else if (type === 'zoneoperation') {
        let container = document.getElementById("main-container")

        let div_modal = document.createElement("div")
        div_modal.className = "modal fade"
        div_modal.id = "staticBackdropZoneOperations-"+ID
        div_modal.setAttribute("data-bs-backdrop", "static")
        div_modal.setAttribute("data-bs-keyboard", "false")
        div_modal.setAttribute("tabindex", "-1")

        let div_modal_dialog = document.createElement("div")
        div_modal_dialog.className = "modal-dialog"

        let div_modal_content = document.createElement("div")
        div_modal_content.className = "modal-content"

        let div_modal_header = document.createElement("div")
        div_modal_header.className = "modal-header"

        let close_modal = document.createElement("button")
        close_modal.className = "btn-close"
        close_modal.setAttribute("data-bs-dismiss", "modal")
        close_modal.setAttribute("aria-label", "Close")

        let modal_title = document.createElement("h5")
        modal_title.className = "modal-title"
        modal_title.id = "staticBackdropSubOperationsLabel-"+ID
        modal_title.style.marginRight = "auto"
        modal_title.innerText = "تقسیم " + opr_name + " در موقعیت ها"

        let div_modal_body = document.createElement("div")
        div_modal_body.className = "modal-body"

        let div_input_group_01 = document.createElement("div")
        div_input_group_01.className = "input-group mb-3"

        let table = document.createElement("table")
        table.className = "table table-bordered border-dark"
        table.id = "table-zone-" + ID
        table.style.fontSize = "11px"

        let thead01 = document.createElement("thead")
        thead01.className = ""
        let thead01_row = document.createElement("tr")
        let thead01_row_td01 = document.createElement("th")
        let thead01_row_td02 = document.createElement("th")
        let thead01_row_td03 = document.createElement("th")
        thead01_row_td01.style.textAlign = "center"
        thead01_row_td02.style.textAlign = "center"
        thead01_row_td03.style.textAlign = "center"

        thead01_row_td01.setAttribute("colspan", "2")
        thead01_row_td02.setAttribute("colspan", "1")
        thead01_row_td03.setAttribute("colspan", "1")

        thead01_row_td01.innerText = opr_name
        thead01_row_td02.innerText = opr_amount
        thead01_row_td03.innerText = opr_unit

        thead01_row_td02.id = "total-amount-" + ID
        thead01_row_td03.id = "total-unit-" + ID



        let thead02 = document.createElement("thead")
        thead02.className = ""
        let thead02_row = document.createElement("tr")
        let thead02_row_td01 = document.createElement("th")
        let thead02_row_td02 = document.createElement("th")
        let thead02_row_td03 = document.createElement("th")
        // let thead02_row_td04 = document.createElement("th")
        thead02_row_td02.style.width = "20%"
        thead02_row_td03.style.width = "20%"
        // thead02_row_td04.style.width = "20%"

        thead02_row_td01.colSpan = 2
        thead02_row_td01.innerText = "موقعیت"
        thead02_row_td02.innerText = "مقدار"
        thead02_row_td03.innerText = "واحد"


        let tbody = document.createElement("tbody")
        // let temp = document.createElement("tr")
        // tbody.appendChild(temp)

        let form = document.createElement("form")
        form.id = "form-zone-"+ID

        let div_input_group_02 = document.createElement("div")
        div_input_group_02.className = "input-group mb-3"

        let table_form = document.createElement("table")
        table_form.style.fontSize = "11px"

        let thead_form =  document.createElement("thead")



        let div_zone_box = document.createElement("div")
        div_zone_box.style = "width: 280px;"
        div_zone_box.id = "zone-box-" + ID

        let select_zones = document.createElement('select')
        select_zones.required = true
        select_zones.className = "select2"
        select_zones.id = "select2-zone-"+ ID
        select_zones.name = "zone"
        select_zones.style = "width: 280px; border: solid black"
        // select_zones.on('click', function() {
        //     findselect2(ID);
        // });

        let choose_option = document.createElement('option')
        choose_option.disabled = true
        choose_option.selected = true
        choose_option.value = ""
        choose_option.innerText = "انتخاب"

        select_zones.appendChild(choose_option)
        fetch_zones(function (zones) {
            zones.forEach(zone => {
                let option = document.createElement('option',)
                option.value = zone.name
                option.innerText = zone.name
                select_zones.appendChild(option)
            })
        })
        div_zone_box.appendChild(select_zones)

        let input_id = document.createElement("input")
        input_id.hidden = true
        input_id.value = ID
        input_id.name = "operation-id"
        input_id.id = "zoneoperation-operation-" + ID
        input_id.required = true

        let th02 = document.createElement("th")
        th02.style = "width: 93px; background-color: white; border: solid black 1px;"

        let th03 = document.createElement("th")
        th03.style = "width: 93px; background-color: white; border: solid black 1px;"
        th03.innerText = opr_unit

        let input_zoneopr_amount = document.createElement("input")
        input_zoneopr_amount.style = "outline: none; background-color: white; border: none; width: 100%; padding: 3px;"
        input_zoneopr_amount.id = "zoneoperation-amount-" + ID
        input_zoneopr_amount.placeholder = "مقدار"
        input_zoneopr_amount.type = "number"
        input_zoneopr_amount.required = true
        input_zoneopr_amount.name = 'amount'



        let btn_submit = document.createElement("button")
        btn_submit.className = "btn btn-outline-success bp3-round w-100"
        btn_submit.type = "submit"
        btn_submit.innerText = "افزودن"

        let div_modal_footer = document.createElement("div")
        div_modal_footer.className = "modal-footer"

        let btn_cmplt = document.createElement("button")
        btn_cmplt.type = "button"
        btn_cmplt.className = "btn btn-outline-warning w-100"
        btn_cmplt.setAttribute('data-bs-dismiss', 'modal')
        btn_cmplt.innerText = "تکمیل"

        // ==================================================
        // --------------------------------------------------
        thead01_row.appendChild(thead01_row_td01)
        thead01_row.appendChild(thead01_row_td02)
        thead01_row.appendChild(thead01_row_td03)

        thead01.appendChild(thead01_row)
        // --------------------------------------------------

        // --------------------------------------------------
        thead02_row.appendChild(thead02_row_td01)
        thead02_row.appendChild(thead02_row_td02)
        thead02_row.appendChild(thead02_row_td03)
        // thead02_row.appendChild(thead02_row_td04)

        thead02.appendChild(thead02_row)
        // --------------------------------------------------

        // --------------------------------------------------
        // th01.appendChild(input_zoneopr_name)
        th02.appendChild(input_zoneopr_amount)

        thead_form.appendChild(input_id)
        // thead_form.appendChild(th01)
        thead_form.appendChild(th02)
        thead_form.appendChild(th03)

        table_form.appendChild(thead_form)

        div_input_group_02.appendChild(div_zone_box)
        div_input_group_02.appendChild(table_form)


        form.appendChild(div_input_group_02)
        form.appendChild(btn_submit)
        // --------------------------------------------------

        // --------------------------------------------------
        table.appendChild(thead01)
        table.appendChild(thead02)
        table.appendChild(tbody)

        div_input_group_01.appendChild(table)
        div_input_group_01.appendChild(form)
        // --------------------------------------------------
        // ==========================================================

        // ==========================================================
        div_modal_footer.appendChild(btn_cmplt)
        // ==========================================================

        // ==========================================================
        div_modal_body.appendChild(div_input_group_01)
        div_modal_body.appendChild(div_modal_footer)
        // ==========================================================

        // ==========================================================
        div_modal_header.appendChild(close_modal)
        div_modal_header.appendChild(modal_title)

        div_modal_content.appendChild(div_modal_header)
        div_modal_content.appendChild(div_modal_body)
        // ==========================================================

        // ==========================================================
        div_modal_dialog.appendChild(div_modal_content)
        div_modal.appendChild(div_modal_dialog)
        container.appendChild(div_modal)
        // ==========================================================

        $('#select2-zone-'+ID).select2({
            dropdownParent: $("#zone-box-"+ID)
        });

        submitForm(ID, 'zoneoperation')
    }
    else if (type === 'subtask') {
        let container = document.getElementById("main-container")

        let div_modal = document.createElement("div")
        div_modal.className = "modal fade"
        div_modal.id = "staticBackdropSubTasks-"+ID
        div_modal.setAttribute("data-bs-backdrop", "static")
        div_modal.setAttribute("data-bs-keyboard", "false")
        div_modal.setAttribute("tabindex", "-1")

        let div_modal_dialog = document.createElement("div")
        div_modal_dialog.className = "modal-dialog modal-lg"

        let div_modal_content = document.createElement("div")
        div_modal_content.className = "modal-content"

        let div_modal_header = document.createElement("div")
        div_modal_header.className = "modal-header"

        let close_modal = document.createElement("button")
        close_modal.className = "btn-close"
        close_modal.setAttribute("data-bs-dismiss", "modal")
        close_modal.setAttribute("aria-label", "Close")

        let modal_title = document.createElement("h5")
        modal_title.className = "modal-title"
        modal_title.id = "staticBackdropSubTaskLabel-"+ID
        modal_title.style.marginRight = "auto"
        modal_title.innerText = "زیر عملیات های " + opr_name + " در موقعیت " + null + " برای اکیپ " + null

        let div_modal_body = document.createElement("div")
        div_modal_body.className = "modal-body"

        let div_input_group_01 = document.createElement("div")
        div_input_group_01.className = "input-group mb-3"

        let table = document.createElement("table")
        table.className = "table table-bordered border-dark"
        table.id = "table-" + ID
        table.style.fontSize = "11px"

        let thead01 = document.createElement("thead")
        thead01.className = ""
        let thead01_row = document.createElement("tr")
        let thead01_row_td01 = document.createElement("th")
        let thead01_row_td02 = document.createElement("th")
        let thead01_row_td03 = document.createElement("th")
        let thead01_row_td04 = document.createElement("th")
        let thead01_row_td05 = document.createElement("th")
        thead01_row_td01.style.textAlign = "center"
        thead01_row_td02.style.textAlign = "center"
        thead01_row_td03.style.textAlign = "center"
        thead01_row_td04.style.textAlign = "center"
        thead01_row_td05.style.textAlign = "center"

        thead01_row_td01.innerText = "عملیات اصلی"
        thead01_row_td02.innerText = "اکیپ"
        thead01_row_td03.innerText = "موقعیت"
        thead01_row_td04.innerText = "مقدار"
        thead01_row_td05.innerText = "واحد"

        let thead01_01 = document.createElement("thead")
        thead01_01.className = "table-light"
        let thead01_01_row = document.createElement("tr")
        let thead01_01_row_td01 = document.createElement("th")
        let thead01_01_row_td02 = document.createElement("th")
        let thead01_01_row_td03 = document.createElement("th")
        let thead01_01_row_td04 = document.createElement("th")
        let thead01_01_row_td05 = document.createElement("th")
        thead01_01_row_td01.style.textAlign = "center"
        thead01_01_row_td02.style.textAlign = "center"
        thead01_01_row_td03.style.textAlign = "center"
        thead01_01_row_td04.style.textAlign = "center"
        thead01_01_row_td05.style.textAlign = "center"

        thead01_01_row_td01.innerText = opr_name
        thead01_01_row_td02.innerText = equipe
        thead01_01_row_td03.innerText = zone
        thead01_01_row_td04.innerText = opr_amount
        thead01_01_row_td05.innerText = opr_unit

        let thead02 = document.createElement("thead")
        thead02.className = ""
        let thead02_row = document.createElement("tr")
        let thead02_row_td01 = document.createElement("th")
        let thead02_row_td02 = document.createElement("th")
        let thead02_row_td03 = document.createElement("th")
        let thead02_row_td04 = document.createElement("th")
        thead02_row_td02.style.width = "20%"
        thead02_row_td03.style.width = "20%"
        thead02_row_td04.style.width = "20%"

        thead02_row_td01.setAttribute('colspan', '2')

        thead02_row_td01.innerText = "زیرعملیات ها"
        thead02_row_td02.innerText = "وزن %"
        thead02_row_td03.innerText = "مقدار"
        thead02_row_td04.innerText = "واحد"


        let tbody = document.createElement("tbody")

        let div_modal_footer = document.createElement("div")
        div_modal_footer.className = "modal-footer"

        let btn_cmplt = document.createElement("button")
        btn_cmplt.type = "button"
        btn_cmplt.className = "btn btn-outline-warning w-100"
        btn_cmplt.setAttribute('data-bs-dismiss', 'modal')
        btn_cmplt.innerText = "تکمیل"

        // ==================================================
        // --------------------------------------------------
        thead01_row.appendChild(thead01_row_td01)
        thead01_row.appendChild(thead01_row_td02)
        thead01_row.appendChild(thead01_row_td03)
        thead01_row.appendChild(thead01_row_td04)
        thead01_row.appendChild(thead01_row_td05)

        thead01.appendChild(thead01_row)
        // --------------------------------------------------
        // --------------------------------------------------
        thead01_01_row.appendChild(thead01_01_row_td01)
        thead01_01_row.appendChild(thead01_01_row_td02)
        thead01_01_row.appendChild(thead01_01_row_td03)
        thead01_01_row.appendChild(thead01_01_row_td04)
        thead01_01_row.appendChild(thead01_01_row_td05)

        thead01_01.appendChild(thead01_01_row)
        // --------------------------------------------------
        // --------------------------------------------------
        thead02_row.appendChild(thead02_row_td01)
        thead02_row.appendChild(thead02_row_td02)
        thead02_row.appendChild(thead02_row_td03)
        thead02_row.appendChild(thead02_row_td04)

        thead02.appendChild(thead02_row)
        // --------------------------------------------------

        // --------------------------------------------------
        // th01.appendChild(input_subopr_name)
        // th02.appendChild(input_subopr_weight)
        // th03.appendChild(input_subopr_amount)
        //
        // thead_form.appendChild(input_id)
        // thead_form.appendChild(th01)
        // thead_form.appendChild(th02)
        // thead_form.appendChild(th03)
        //
        // table_form.appendChild(thead_form)
        //
        // div_input_group_02.appendChild(table_form)
        // div_input_group_02.appendChild(div_unit_box)
        //
        // form.appendChild(div_input_group_02)
        // form.appendChild(btn_submit)
        // --------------------------------------------------

        // ==================================================
        $.ajax({
            type: 'POST',
            url: '/edit-db/get-subtasks-of/' + ID + '/',
            data: {
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                // let subtasks = JSON.parse(response['subtasks'])
                let subtasks = response

                for (let i=0; i<subtasks.length; i++) {

                    let row = document.createElement("tr")
                    let row_td01 = document.createElement("td")
                    let row_td02 = document.createElement("td")
                    let row_td03 = document.createElement("td")
                    let row_td04 = document.createElement("td")

                    row_td01.setAttribute('colspan', '2')

                    row_td01.innerText = subtasks[i].foreigns.name
                    row_td02.innerText = subtasks[i].foreigns.weight
                    row_td03.innerText = subtasks[i].totalVolume
                    row_td04.innerText = subtasks[i].foreigns.unit

                    row.appendChild(row_td01)
                    row.appendChild(row_td02)
                    row.appendChild(row_td03)
                    row.appendChild(row_td04)

                    tbody.appendChild(row)

                }

            }
        });
        // --------------------------------------------------
        table.appendChild(thead01)
        table.appendChild(thead01_01)
        table.appendChild(thead02)
        table.appendChild(tbody)

        div_input_group_01.appendChild(table)
        // div_input_group_01.appendChild(form)
        // --------------------------------------------------
        // ==========================================================

        // ==========================================================
        div_modal_footer.appendChild(btn_cmplt)
        // ==========================================================

        // ==========================================================
        div_modal_body.appendChild(div_input_group_01)
        div_modal_body.appendChild(div_modal_footer)
        // ==========================================================

        // ==========================================================
        div_modal_header.appendChild(close_modal)
        div_modal_header.appendChild(modal_title)

        div_modal_content.appendChild(div_modal_header)
        div_modal_content.appendChild(div_modal_body)
        // ==========================================================

        // ==========================================================
        div_modal_dialog.appendChild(div_modal_content)
        div_modal.appendChild(div_modal_dialog)
        container.appendChild(div_modal)
        // ==========================================================

        // $('#select2-'+ID).select2({
        //     dropdownParent: $("#unit-box-"+ID)
        // });

        // submitForm(ID, 'suboperation')
    }
}

function handle_select(type) {

    if (type) {
        if (type.includes("shortcut")) {
            var shortcut = "-shortcut"
            type = type.split("-")[0]
        } else {
            var shortcut = ""
        }
    } else {
        var shortcut = ""
    }

    let select = document.getElementById("select2-"+type+shortcut)
    if ( type === "operation" ) {
        $("#select2-"+type+shortcut).empty().append(
            '<option value="" selected disabled>انتخاب عملیات اصلی</option>'
        )
        fetch_operations(function (operations) {
            operations.forEach(operation => {
                let option = document.createElement('option',)
                option.value = operation.name
                option.innerHTML = operation.name
                select.appendChild(option)
            })
        })
        $('#select2-operation'+shortcut).select2({
            dropdownParent: $("#operation-box"+shortcut)
        });
    }
    else if ( type === "suboperation" ) {
        $("#select2-"+type+shortcut).empty().append(
            '<option value="" selected disabled>انتخاب زیرعملیات</option>'
        )
        $("#select2-zoneoperation+shortcut").empty().append(
            '<option value="" selected disabled>انتخاب موقعیت عملیات</option>'
        )
        let subtype = document.getElementById("select2-operation"+shortcut).value
        fetch_suboperations(subtype, function (operations) {
            operations.forEach(operation => {
                let option = document.createElement('option',)
                option.value = operation.name
                option.innerHTML = operation.name
                select.appendChild(option)
            })
        })

        $('#select2-suboperation'+shortcut).select2({
            dropdownParent: $("#suboperation-box"+shortcut)
        });


        let select2 = document.getElementById("select2-zoneoperation"+shortcut)
        fetch_zoneoperations(subtype, function (zoneoperations) {
            zoneoperations.forEach(zoneoperation => {
                let option = document.createElement('option',)
                option.value = zoneoperation.zone
                option.innerHTML = zoneoperation.zone
                select2.appendChild(option)
                document.getElementById("task-unit"+shortcut).value = zoneoperation.unit
            })
        })

        $('#select2-zoneoperation'+shortcut).select2({
            dropdownParent: $("#zoneoperation-box"+shortcut)
        });
    }
    else if (type === "zoneoperation" ) {
        $("#select2-"+type+shortcut).empty().append(
            '<option value="" selected disabled>انتخاب موقعیت عملیات</option>'
        )
        let subtype = document.getElementById("select2-operation"+shortcut).value
        fetch_zoneoperations(subtype, function (zoneoperations) {
            zoneoperations.forEach(zoneoperation => {
                let option = document.createElement('option',)
                option.value = zoneoperation.zone
                option.innerHTML = zoneoperation.zone
                select.appendChild(option)
                document.getElementById("task-unit"+shortcut).value = zoneoperation.unit
            })
        })

        $('#select2-zoneoperation'+shortcut).select2({
            dropdownParent: $("#zoneoperation-box"+shortcut)
        });

    }
    else if (type === "equipe") {
        $("#select2-"+type+shortcut).empty().append(
            '<option value="" selected disabled>انتخاب اکیپ</option>'
        )
        fetch_all_equipes(function (equipes) {
            equipes.forEach(equipe => {
                let option = document.createElement('option',)
                option.value = equipe.name
                option.innerHTML = equipe.name
                select.appendChild(option)
            })
        })
        $('#select2-equipe'+shortcut).select2({
            dropdownParent: $("#equipe-box"+shortcut)
        });
    }
    else if ( type === "zone" ) {
        $.ajax({
            type: 'GET',
            url: '/edit-db/get-freeAmount/',
            data: {
                "model": "zoneoperation",
                "operation": document.getElementById('select2-operation'+shortcut).value,
                "zone": document.getElementById('select2-zoneoperation'+shortcut).value,
            },
            success: function(response) {
                let freeAmount = response
                document.getElementById("task-volume"+shortcut).max = freeAmount
                document.getElementById("task-volume"+shortcut).setAttribute(
                    'placeholder', "حداکثر مقدار : " + freeAmount
                )
            }
        });
    }
    else if ( type === "zone_in_report") {

        let opr = document.getElementById('select2-operation'+shortcut).value
        let subopr = document.getElementById('select2-suboperation'+shortcut).value
        let zone = document.getElementById('select2-zoneoperation'+shortcut).value
        $.ajax({
            url: '/edit-db/get-equipes-in-report/',
            type: 'POST',
            data: {
                'operation': opr,
                'suboperation': subopr,
                'zone': zone,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                // let tasks = JSON.parse(response['tasks'])
                let tasks = response['tasks']
                let select = document.getElementById("select2-equipe"+shortcut)

                $("#select2-equipe"+shortcut).empty().append(
                    '<option value="" selected disabled>انتخاب اکیپ</option>'
                )
                for (let i=0; i<tasks.length; i++) {
                    let splitted = tasks[i].split("-")

                    let option = document.createElement("option")
                    option.value = splitted[2] + "-" + splitted[3]
                    option.innerText = splitted[2] + "-" + splitted[3]

                    select.appendChild(option)
                }

            }
        })


    }
    else {
        $('#select2-operation'+shortcut).select2({
            dropdownParent: $("#operation-box"+shortcut)
        });

        $('#select2-suboperation'+shortcut).select2({
            dropdownParent: $("#suboperation-box"+shortcut)
        });

        $('#select2-zoneoperation'+shortcut).select2({
            dropdownParent: $("#zoneoperation-box"+shortcut)
        });

        $('#select2-equipe'+shortcut).select2({
            dropdownParent: $("#equipe-box"+shortcut)
        });
    }

}

function analyzer_handle_select(type=null) {

        $('#select2-analyze-type').select2({
            dropdownParent: $("#select2-analyze-type-container")
        });

        // =================================================================
        // =================================================================

        $('#select2-formula-priority-one').select2({
            dropdownParent: $("#select2-formula-priority-one-container")
        });
        $('#select2-formula-priority-two').select2({
            dropdownParent: $("#select2-formula-priority-two-container")
        });
        $('#select2-formula-priority-three').select2({
            dropdownParent: $("#select2-formula-priority-three-container")
        });
        $('#select2-formula-priority-four').select2({
            dropdownParent: $("#select2-formula-priority-four-container")
        });
        $('#select2-formula-priority-five').select2({
            dropdownParent: $("#select2-formula-priority-five-container")
        });

        // ---------------------------------------------------------------

        $('#select2-filter-priority-one').select2({
            dropdownParent: $("#select2-filter-priority-one-container")
        });
        $('#select2-filter-priority-two').select2({
            dropdownParent: $("#select2-filter-priority-two-container")
        });
        $('#select2-filter-priority-three').select2({
            dropdownParent: $("#select2-filter-priority-three-container")
        });
        $('#select2-filter-priority-four').select2({
            dropdownParent: $("#select2-filter-priority-four-container")
        });
        $('#select2-filter-priority-five').select2({
            dropdownParent: $("#select2-filter-priority-five-container")
        });

        // =================================================================
        // =================================================================

        $('#select2-formula-priority-one-machine').select2({
            dropdownParent: $("#select2-formula-priority-one-container-machine")
        });
        $('#select2-formula-priority-two-machine').select2({
            dropdownParent: $("#select2-formula-priority-two-container-machine")
        });

        // ---------------------------------------------------------------

        $('#select2-filter-priority-one-machine').select2({
            dropdownParent: $("#select2-filter-priority-one-container-machine")
        });
        $('#select2-filter-priority-two-machine').select2({
            dropdownParent: $("#select2-filter-priority-two-container-machine")
        });

        // =================================================================
        // =================================================================



}

function set_analyze_type() {
    let select = document.getElementById("select2-analyze-type")

    switch (select.value) {
        case "volume":
            hide_machine_material_filters("machine");
            clear_machine_material_filters("machine");
            // hide_machine_material_filters("material");
            // clear_machine_material_filters("material");

            document.getElementById("MachineWork-Box").hidden = true
            document.getElementById("Material-Box").hidden = true
            var container = document.getElementById("Ahjam-Box")
            container.hidden = false

            break;

        case "machine":
            hide_volume_filters();
            clear_volume_filters();
            // hide_machine_material_filters("material");
            // clear_machine_material_filters("material");

            document.getElementById("Ahjam-Box").hidden = true
            document.getElementById("Material-Box").hidden = true
            var container = document.getElementById("MachineWork-Box")
            container.hidden = false

            break;

        case "material":
            hide_volume_filters();
            clear_volume_filters();
            hide_machine_material_filters("machine");
            clear_machine_material_filters("machine");

            document.getElementById("MachineWork-Box").hidden = true
            document.getElementById("Ahjam-Box").hidden = true
            var container = document.getElementById("Material-Box")
            container.hidden = false

            break;

    }
}

function handle_formula_priority(priority=null, nonVolume=null ) {

    if (nonVolume) {
        clear_machine_material_filters(type=nonVolume);
        hide_machine_material_filters(type=nonVolume)

        var priorities = {
            "machine" : "تجهیز",
            "material" : "مصالح",
            "provider" : "تامین کننده",
        }
        var select_priorities = ["one", "two", "three", "four", "five"]

        switch (priority) {
            case 1:
                var exclude = document.getElementById("select2-formula-priority-one-"+nonVolume).value
                for (let i=1; i<select_priorities.length; i++) {
                    let temp = '<option value="" selected disabled>انتخاب اولویت</option>'
                   $("#select2-formula-priority-"+select_priorities[i]+"-"+nonVolume).empty().append(
                         temp
                    )
                }
                if (exclude === nonVolume) {
                    $("#select2-formula-priority-two-"+nonVolume).append(
                        '<option value="'+'provider'+'">'+priorities["provider"]+'</option>'
                    )
                }
                else {
                    $("#select2-formula-priority-two-"+nonVolume).append(
                        '<option value="'+nonVolume+'">'+priorities[nonVolume]+'</option>'
                    )
                }

                break;

            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;

        }

        if ( nonVolume === "machine" ) {

        }
        else if ( nonVolume === "material" ) {

        }
    }
    else {
        clear_volume_filters();
        hide_volume_filters();
        var priorities = {
            // "time" : "زمان",
            "zone" : "موقعیت",
            "operation" : "عملیات اصلی",
            // "suboperation" : "عملیات اجرایی",
            "equipe" : "پیمانکار",
        }
        var select_priorities = ["one", "two", "three", "four", "five"]

        switch (priority) {
            case 1:
                var exclude = document.getElementById("select2-formula-priority-one").value
                for (let i=1; i<select_priorities.length; i++) {
                   $("#select2-formula-priority-"+select_priorities[i]).empty().append(
                    '<option value="" selected disabled>انتخاب اولویت</option>'
                    )
                }
                for (var key in priorities) {
                    if (key === exclude) {
                        continue
                    } else {
                        $("#select2-formula-priority-two").append(
                            '<option value="'+key+'">'+priorities[key]+'</option>'
                        )
                    }
                }
                break;
            case 2:
                var exclude_01 = document.getElementById("select2-formula-priority-one").value
                var exclude_02 = document.getElementById("select2-formula-priority-two").value
                for (let i=2; i<select_priorities.length; i++) {
                   $("#select2-formula-priority-"+select_priorities[i]).empty().append(
                    '<option value="" selected disabled>انتخاب اولویت</option>'
                    )
                }
                for (var key in priorities) {
                    if (key === exclude_01 || key === exclude_02) {
                        continue
                    } else {
                        $("#select2-formula-priority-three").append(
                            '<option value="'+key+'">'+priorities[key]+'</option>'
                        )
                    }
                }

                break;
            case 3:
                var exclude_01 = document.getElementById("select2-formula-priority-one").value
                var exclude_02 = document.getElementById("select2-formula-priority-two").value
                var exclude_03 = document.getElementById("select2-formula-priority-three").value
                for (let i=3; i<select_priorities.length; i++) {
                   $("#select2-formula-priority-"+select_priorities[i]).empty().append(
                    '<option value="" selected disabled>انتخاب اولویت</option>'
                    )
                }
                for (var key in priorities) {
                    if (key === exclude_01 || key === exclude_02 || key === exclude_03) {
                        continue
                    } else {
                        $("#select2-formula-priority-four").append(
                            '<option value="'+key+'">'+priorities[key]+'</option>'
                        )
                    }
                }

                break;
            case 4:
                var exclude_01 = document.getElementById("select2-formula-priority-one").value
                var exclude_02 = document.getElementById("select2-formula-priority-two").value
                var exclude_03 = document.getElementById("select2-formula-priority-three").value
                var exclude_04 = document.getElementById("select2-formula-priority-four").value
                for (let i=4; i<select_priorities.length; i++) {
                   $("#select2-formula-priority-"+select_priorities[i]).empty().append(
                    '<option value="" selected disabled>انتخاب اولویت</option>'
                    )
                }
                for (var key in priorities) {
                    if (key === exclude_01 || key === exclude_02 || key === exclude_03 || key === exclude_04) {
                        continue
                    } else {
                        $("#select2-formula-priority-five").append(
                            '<option value="'+key+'">'+priorities[key]+'</option>'
                        )
                  }
                }

                break;
            case 5:

                break;

        }
    }


}

function submitPriorityFormulaVolumes() {
    var pivots = {
        // "time" : "زمان",
        "zone" : "موقعیت",
        "operation" : "عملیات اصلی",
        // "suboperation" : "عملیات اجرایی",
        "equipe" : "پیمانکار",
    }
    show_volume_filters()

    let priorities = [
        document.getElementById("select2-formula-priority-one").value,
        document.getElementById("select2-formula-priority-two").value,
        document.getElementById("select2-formula-priority-three").value,
        document.getElementById("select2-formula-priority-four").value,
        // document.getElementById("select2-formula-priority-five").value,
    ]

    for (let i=0; i<priorities.length; i++) {
        if (pivots[priorities[i]]) {
            document.getElementById(
                "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]
            ).disabled = false
            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"
            ).disabled = false

            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"
            ).style.textDecoration = "none"

            document.getElementById("priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label").innerText = i+1 + "- " + pivots[priorities[i]]

            if (priorities[i] === "time") {
                let selectID = "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]
                $("#"+selectID).append(
                    '<option value="0">همه موارد</option>'
                )
            }
            else {
                fetch_options_in_priority(priorities[i], "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1])
                document.getElementById(
                    "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]
                ).name = i+1+"_"+priorities[i] + "_priority"
            }


        }
        else {
            document.getElementById(
                "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]
            ).disabled = true
            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"
            ).disabled = true

            document.getElementById("priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label").innerText = i+1 + "- " + "تعیین نشده"

            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"
            ).style.textDecoration = "line-through"

        }

    }

}

function hide_volume_filters() {
    document.getElementById("Ahjam-Filter-Box").hidden = true
}

function show_volume_filters() {
    document.getElementById("Ahjam-Filter-Box").hidden = false
}

function clear_volume_filters() {
    var selects = document.getElementById("Ahjam-Filter-Box").querySelectorAll("select")
    for (let i = 0; i < selects.length; i++) {
        $("#"+selects[i].id).empty()
    }
}


function submitPriorityFormula_Machines_Material(type, ) {
    var pivots = {
        "machine" : "تجهیز",
        "material" : "مصالح",
        "provider" : "تامین کننده",
    }
    show_machine_material_filters(type=type)

    let priorities = [
        document.getElementById("select2-formula-priority-one-"+type).value,
        document.getElementById("select2-formula-priority-two-"+type).value,
    ]

    for (let i=0; i<priorities.length; i++) {
        if (pivots[priorities[i]]) {
            document.getElementById(
                "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]+"-"+type
            ).disabled = false
            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type
            ).disabled = false

            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type
            ).style.textDecoration = "none"

            document.getElementById("priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type).innerText = i+1 + "- " + pivots[priorities[i]]

            if (priorities[i] === "time") {
                let selectID = "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]+"-"+type
                $("#"+selectID).append(
                    '<option value="0">همه موارد</option>'
                )
            }
            else {
                fetch_options_in_priority(priorities[i], "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]+"-"+type, providerType=type)
                document.getElementById(
                    "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]+"-"+type
                ).name = i+1+"_"+priorities[i] + "_priority"
            }


        }
        else {
            document.getElementById(
                "select2-filter-priority-"+STRINGS_FROM_NUMBERS[i+1]+"-"+type
            ).disabled = true
            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type
            ).disabled = true

            document.getElementById("priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type).innerText = i+1 + "- " + "تعیین نشده"

            document.getElementById(
                "priority-"+STRINGS_FROM_NUMBERS[i+1]+"-label"+"-"+type
            ).style.textDecoration = "line-through"

        }

    }

}

function hide_machine_material_filters(type) {
    document.getElementById(type+"-Filter-Box").hidden = true
}

function show_machine_material_filters(type) {
    document.getElementById(type+"-Filter-Box").hidden = false
}

function clear_machine_material_filters(type) {
    var selects = document.getElementById(type+"-Filter-Box").querySelectorAll("select")
    for (let i = 0; i < selects.length; i++) {
        $("#"+selects[i].id).empty()
    }
}


function fetch_options_in_priority(priority, selectID, providerType=null) {
    $.ajax({
        type: 'POST',
        url: '/edit-db/get-options-in-priority/',
        data: {
        'priority': priority,
        'providerType': providerType,
        },
        beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            let objs = JSON.parse(response[priority])
            // $("#"+selectID).empty().append(
            //     '<option value="" selected disabled>انتخاب اولویت</option>'
            // )
             $("#"+selectID).append(
                '<option value="0">همه موارد</option>'
            )
            for (let i=0; i<objs.length; i++) {
                $("#"+selectID).append(
                    '<option value="'+objs[i].id+'">'+objs[i].name+'</option>'
                )
            }

        }
    });
}

function dateFilterSwitch(nonVolume=null) {
    if (nonVolume){
     nonVolume = "-"+nonVolume
    } else {
        nonVolume = ""
    }
    let switchKey = document.getElementById("customDateFilterSwitch"+nonVolume)
    if (switchKey.checked) {
        document.getElementById("date-from"+nonVolume).disabled = false
        document.getElementById("date-through"+nonVolume).disabled = false

        document.getElementById("date-from"+nonVolume).placeholder = "از تاریخ"
        document.getElementById("date-through"+nonVolume).placeholder = "تا تاریخ"
    }
    else {
        document.getElementById("date-from"+nonVolume).disabled = true
        document.getElementById("date-through"+nonVolume).disabled = true

        document.getElementById("date-from"+nonVolume).placeholder = "همیشه"
        document.getElementById("date-through"+nonVolume).placeholder = "همیشه"
    }
}

function submitAnalyzer(type) {
    if (type === "Ahjam") {
        var target = "form-Ahjam"
    }


    $('#'+target).submit(function(event) {
        // Prevent form submission
        event.preventDefault();

        // Collect form data
        var formData = new FormData(this);
        if (!formData.get("customDateFilterSwitch")) {
            formData.append("customDateFilterSwitch", false)
        }

        $.ajax({
            url: '/analyzer/analyze/',
            type: 'POST',
            data: formData,
            dataType: 'json',
            contentType: false,
            processData: false,
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function (response) {

            }

        })

    })
}


