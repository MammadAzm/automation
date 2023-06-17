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

function del_task(taskName, equipeName, zoneName, taskVol, unitName, db) {
    if (db) {
        $.ajax({
            type: 'POST',
            url: '/edit-db/del-task',
            data: {
            'taskName': taskName,
            'equipeName': equipeName,
            'zoneName': zoneName,
            'taskVol': taskVol,
            'unitName': unitName,
            },
            beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                let obj = document.getElementById(taskName+"-"+equipeName+"-"+zoneName)
                obj.remove()
                }
        });
    } else {
        let obj = document.getElementById(taskName+"-"+equipeName+"-"+zoneName)
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
      $('#unit-name').val(selectedItemText);
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
    document.getElementById("machine-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-machine");

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
    input0.id = "machine_"+val+"_workHours";
    input0.name = "machine_"+val+"_workHours";
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
    input.id = "machine_"+val+"_activeCount";
    input.name = "machine_"+val+"_activeCount";
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
    input.id = "machine_"+val+"_inactiveCount";
    input.name = "machine_"+val+"_inactiveCount";
    input.min = '0';
    input.value = '0';
    cell3.appendChild(input)

    let cell4 = document.createElement('td', );
    cell4.className = "";
    let select = document.createElement('select',)
    select.required = true;
    select.className = "form-select";
    select.id = "machine_"+val+"_provider";
    select.name = "machine_"+val+"_provider";
    select.style.fontSize = '11px';
    select.style.textAlign = 'left  ';
    select.style.padding = '0';
    select.style.paddingLeft = '15%';

    let option = document.createElement('option',)
    option.value = ""
    option.innerHTML = "انتخاب"
    option.disabled = true
    option.hidden = true
    option.selected = true
    select.appendChild(option)

    fetch_machineproviders(function (providers) {
        providers.forEach(provider => {
            let option = document.createElement('option',)
            option.value = provider.name
            option.innerHTML = provider.name
            select.appendChild(option)
        })
    })
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
    document.getElementById("material-name").value = "";
    if (!val) {
        return 0
    }
    let table = document.getElementById("table-material");

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
    input.id = "material_"+val+"_count";
    input.name = "material_"+val+"_count";
    input.min = '0';
    input.value = '0';

    let cell3 = document.createElement('td', );
    cell3.className = "";
    let select = document.createElement('select',)
    select.required = true;
    select.className = "form-select";
    select.id = "material_"+val+"_unit";
    select.name = "material_"+val+"_unit";
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
    select2.id = "material_"+val+"_provider";
    select2.name = "material_"+val+"_provider";
    select2.style.fontSize = '11px';
    select2.style.textAlign = 'left  ';
    select2.style.padding = '0';
    select2.style.paddingLeft = '15%';

    option = document.createElement('option',)
    option.value = ""
    option.innerHTML = "انتخاب"
    option.disabled = true
    option.hidden = true
    option.selected = true
    select2.appendChild(option)

    fetch_materialproviders(function (materialproviders) {
        materialproviders.forEach(materialprovider => {
            let option = document.createElement('option',)
            option.value = materialprovider.name
            option.innerHTML = materialprovider.name
            select2.appendChild(option)
        })
    })

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
            cell4.className = "";
            cell4.appendChild(input)

            let cell5 = document.createElement('td', );
            cell5.className = "";
            cell5.style.textAlign = "center"
            cell5.innerHTML = obj.doneVolume.toFixed(2);

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
                    if (response == "True") {
                        alert("عملیات با موفقیت انجام شد")
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

        let unitName = document.getElementById("unit-name").value
        document.getElementById("unit-name").value = "";

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
                }
            }
        })

    } else {
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
}

function shortcut_add(which, ) {
    if (which == "position") {
        let value = document.getElementById("shortcut_position").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_position").value = ""

    } else if (which == "profession") {
        let value = document.getElementById("shortcut_profession").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_profession").value = ""
    }
    else if (which == "machine") {
        let value = document.getElementById("shortcut_machine").value
        let type = document.getElementById("shortcut_machineType").value
        shotcut_add_to_base(which, value, type);
        document.getElementById("shortcut_machine").value = ""
    }
    else if (which == "material") {
        let value = document.getElementById("shortcut_material").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_material").value = ""
    }
    else if (which == "contractor") {
        let value = document.getElementById("shortcut_contractor").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_contractor").value = ""
    }
    else if (which == "zone") {
        let value = document.getElementById("shortcut_zone").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_zone").value = ""
    }
    else if (which == "unit") {
        let value = document.getElementById("shortcut_unit").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_unit").value = ""
    }
    else if (which == "materialprovider") {
        let value = document.getElementById("shortcut_materialprovider").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_materialprovider").value = ""
    }
    else if (which == "machineprovider") {
        let value = document.getElementById("shortcut_machineprovider").value
        shotcut_add_to_base(which, value);
        document.getElementById("shortcut_machineprovider").value = ""
    }
    else if (which == "") {

    }
    else if (which == "") {

    }

}

function shotcut_add_to_base(which, value, type=null) {
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


function shotcut_add_to_base_2(which, value, type=null) {
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
