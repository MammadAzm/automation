//
// function search_base_machine() {
//     let dropdownItems = $('#dropdown-menu-base-machines').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-machine').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-machine").dispatchEvent(event);
//       $('#machine-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-machine').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_profession() {
//     let dropdownItems = $('#dropdown-menu-base-professions').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-profession').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-profession").dispatchEvent(event);
//       $('#profession-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-profession').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_contractor() {
//     let dropdownItems = $('#dropdown-menu-base-contractors').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-contractor').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-contractor").dispatchEvent(event);
//       $('#contractor-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-contractor').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_equipes() {
//     // for create report page
//
//     let dropdownItems = $('#dropdown-menu-base-equipes-professions').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-equipe-profession').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-equipe-profession").dispatchEvent(event);
//       $('#equipe-profession-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-equipe-profession').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_position() {
//     let dropdownItems = $('#dropdown-menu-base-positions').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-position').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-position").dispatchEvent(event);
//       $('#position-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-position').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_material() {
//     let dropdownItems = $('#dropdown-menu-base-materials').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-position').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-material").dispatchEvent(event);
//       $('#material-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-material').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_equipe_task() {
//     let dropdownItems = $('#dropdown-menu-base-tasks').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-task').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-task").dispatchEvent(event);
//       $('#equipetask-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-task').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_tasks() {
//     let dropdownItems = $('#dropdown-menu-base-tasks').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-task').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-task").dispatchEvent(event);
//       $('#task-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-task').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_zone_task() {
//     let dropdownItems = $('#dropdown-menu-base-zones').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-zone').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-zone").dispatchEvent(event);
//       $('#zone-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-zone').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_unit_task() {
//     let dropdownItems = $('#dropdown-menu-base-units').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-unit').val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-unit").dispatchEvent(event);
//       $('#unit-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-unit').on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
//
// function search_base_equipe(type) {
//     // for base data page
//
//     let dropdownItems = $('#dropdown-menu-base-equipes-'+type+'s').find('a');
//
//     // Add event listener to the dropdown items
//     dropdownItems.on('click', function() {
//       let selectedItemText = $(this).text();
//
//       // Set the search input value to the selected item text
//       $('#search-base-equipe-'+type).val("");
//       let event = new Event('keyup');
//       document.getElementById("search-base-equipe-" + type).dispatchEvent(event);
//       $('#equipe-'+type+'-name').val(selectedItemText);
//     });
//     // Add event listener to the search input
//     $('#search-base-equipe-' + type).on('keyup', function() {
//       let searchText = $(this).val().toLowerCase();
//
//       // Loop through each dropdown item and hide/show based on search text
//       dropdownItems.each(function() {
//         let text = $(this).text().toLowerCase();
//         if (text.includes(searchText)) {
//           $(this).show();
//         } else {
//           $(this).hide();
//         }
//       });
//     });
// }
