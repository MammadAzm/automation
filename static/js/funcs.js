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

/*
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
*/

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
        float: 'left',
        color: 'black',
    });
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
    span.addEventListener('click', function() {
    del_machine(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
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
    input.required = true;
    input.className = "small-input-integer";
    input.type = "number";
    input.id = "machine_"+val+"_inactiveCount";
    input.name = "machine_"+val+"_inactiveCount";
    input.min = '0';
    input.value = '0';
    cell3.appendChild(input)

    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);

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
        float: 'left',
        color: 'black',
    });
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
    span.addEventListener('click', function() {
    del_material(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
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

    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    newRow.appendChild(cell3);

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
        float: 'left',
        color: 'black',
    });
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
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
        float: 'left',
        color: 'black',
    });
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
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
        float: 'left',
        color: 'black',
    });
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
    span.addEventListener('click', function() {
    del_position(val, false);
    });
    cell1.innerHTML = val;
    cell1.appendChild(span)

    let cell2 = document.createElement('td', );
    cell2.className = "";
    let input = document.createElement('input', );
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
                float: 'left',
                color: 'black',
            });
            span.className = "badge rounded-pill bg-danger";
            span.innerHTML = "-";
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

function add_equipe_to_base_data() {
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
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
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

function add_task_to_base_data() {
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
    span.className = "badge rounded-pill bg-danger";
    span.innerHTML = "-";
    span.addEventListener('click', function() {
    del_task(taskName, equipeName, zoneName, taskVol, unitName, true);
    });
    descr.innerHTML = taskName;
    descr.appendChild(span)

    let equipeCell = document.createElement('td', );
    equipeCell.className = ""
    equipeCell.innerHTML = equipeName;

    let zoneCell = document.createElement('td', );
    zoneCell.className = ""
    zoneCell.innerHTML = zoneName;

    let unitCell = document.createElement('td', );
    unitCell.className = ""
    unitCell.innerHTML = unitName;

    let volCell = document.createElement('td', );
    volCell.className = ""
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

function fetch_options(type){
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

function toggle_requirement(toggleID, conditionID) {
    let select = document.getElementById(toggleID)
    let input = document.getElementById(conditionID)
    if (input.value == 0) {
        select.required = false
    } else if (input.value > 0) {
        select.required = true
    }

}
