"""
URL configuration for alphaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from automation.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("home/", home, name="home"),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path("home/analyzer/", analyzer, name="analyzer"),

    # Main Paths
    path("home/add-base-data/", add_base_data_template),

    path("home/create-report/", create_report_template),
    path("home/daily-reports/", reports_daily),
    path("home/daily-reports/<int:idd>", report_on_day),
    path("home/print-daily-reports/<int:idd>", print_report_on_day),
    path("home/print-daily-reports/compact/<int:idd>", print_report_compact_on_day),
    path("home/daily-reports/compact/<idd>", compact_report_on_day),
    path("home/daily-reports/check-existence", check_dailyreport_existence),

    # Edit DB paths
    path("edit-db/add-position", add_position_to_db),
    path("edit-db/add-profession", add_profession_to_db),
    path("edit-db/add-hardware", add_hardware_to_db),
    path("edit-db/add-machineFamily", add_machineFamily_to_db),
    path("edit-db/add-machine", add_machine_to_db),
    path("edit-db/add-material", add_material_to_db),
    path("edit-db/add-contractor", add_contractor_to_db),
    path("edit-db/add-zone", add_zone_to_db),
    path("edit-db/add-equipe", add_equipe_to_db),
    path("edit-db/add-task", add_task_to_db),
    path("edit-db/add-unit", add_unit_to_db),
    path("edit-db/add-materialprovider", add_materialprovider_to_db),
    path("edit-db/add-machineprovider", add_machineprovider_to_db),
    path("edit-db/add-issue", add_issue_to_db),
    path("edit-db/add-issueReport-to-project", add_issueReport_to_project),
    path("edit-db/add-projectField", add_projectField_to_db),

    path("edit-db/edit-base-data", edit_base_data),

    path("edit-db/shortcut-add", shortcut_add),

    path("edit-db/save-daily-report", save_daily_report_to_db),
    path("edit-db/save-edit-daily-report", edit_daily_report_in_db),
    path("edit-db/del-daily-report/", del_daily_report_from_db),
    path("edit-db/edit-daily-report/", edit_daily_report_in_db),

    path("edit-db/del-position", del_position_from_db),
    path("edit-db/del-profession", del_profession_from_db),
    path("edit-db/del-hardware", del_hardware_from_db),
    path("edit-db/del-machineFamily", del_machineFamily_from_db),
    path("edit-db/del-machine", del_machine_from_db),
    path("edit-db/del-material", del_material_from_db),
    path("edit-db/del-contractor", del_contractor_from_db),
    path("edit-db/del-zone", del_zone_from_db),
    path("edit-db/del-unit", del_unit_from_db),
    path("edit-db/del-equipe", del_equipe_from_db),
    path("edit-db/del-task", del_task_from_db),
    path("edit-db/del-materialprovider", del_materialprovider_from_db),
    path("edit-db/del-machineprovider", del_machineprovider_from_db),
    path("edit-db/del-issue", del_issue_from_db),
    path("edit-db/del-projectField", del_projectField_from_db),


    path("edit-db/add-suboperation", add_suboperation_to_db),
    path("edit-db/add-operation", add_operation_to_db),
    path("edit-db/add-zoneoperation", add_zoneoperation_to_db),
    path("edit-db/del-operation", del_operation_from_db),
    path("edit-db/del-suboperation", del_suboperation_from_db),
    path("edit-db/del-zoneoperation", del_zoneoperation_from_db),


    path("edit-db/get-options/<typee>", get_options),
    path("edit-db/get-tasks", get_tasks),
    path("edit-db/get-task", get_task),
    path("edit-db/get-units/", get_units),
    path("edit-db/get-professions/", get_professions),
    path("edit-db/get-contractors/", get_contractors),
    path("edit-db/get-hardwares/", get_hardwares),
    path("edit-db/get-machineFamilies/", get_machineFamilies),
    path("edit-db/get-machines/", get_machines),
    path("edit-db/get-operations/", get_operations),
    path("edit-db/get-issues/", get_issues),
    path("edit-db/get-projectFields/", get_projectFields),
    path("edit-db/get-operations/<int:ID>/", get_operations),
    path("edit-db/get-suboperations/", get_suboperations),
    path("edit-db/get-subtasks-of/<int:ID>/", get_subtasks_of),
    path("edit-db/get-subtask-in-report/", get_subtask_in_report),
    path("edit-db/get-zoneoperations/", get_zoneoperations),
    path("edit-db/get-all-equipes/", get_all_equipes),
    path("edit-db/get-equipes-in-report/", get_equipes_in_report),
    path("edit-db/get-equipes2-in-report/", get_equipes2_in_report),
    path("edit-db/get-freeAmount/", get_freeAmount),
    path("edit-db/get-zones/", get_zones),
    path("edit-db/get-materialproviders/", get_materialproviders),

    path("edit-db/get-machineproviders/", get_machineproviders),
    path("edit-db/check-deletability/", check_deletability),
    path("edit-db/check-editability/", check_editability),


    path("edit-db/get-options-in-priority/", get_options_in_priority),
    path("edit-db/get-onOwn-id/", get_onOwn_id),
    path("edit-db/get-task-filters/", get_task_filters),


    path("analyzer/analyze/", analyzer),
    path("analyzer/analyze/machine/day2day/", day2day_analyzer_machine),
    path("analyzer/analyze/material/day2day/", day2day_analyzer_material),
]
