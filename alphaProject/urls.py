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


    path("home/", home),

    # Main Paths
    path("home/add-base-data/", add_base_data_template),

    path("home/add-base-data/operation-break", operation_break_template),

    path("home/create-report/", create_report_template),
    path("home/daily-reports/", reports_daily),
    path("home/daily-reports/<int:idd>", report_on_day),
    path("home/daily-reports/compact/<idd>", compact_report_on_day),
    path("home/daily-reports/check-existence", check_dailyreport_existence),

    # Edit DB paths
    path("edit-db/add-position", add_position_to_db),
    path("edit-db/add-profession", add_profession_to_db),
    path("edit-db/add-machine", add_machine_to_db),
    path("edit-db/add-material", add_material_to_db),
    path("edit-db/add-contractor", add_contractor_to_db),
    path("edit-db/add-zone", add_zone_to_db),
    path("edit-db/add-equipe", add_equipe_to_db),
    path("edit-db/add-task", add_task_to_db),
    path("edit-db/add-unit", add_unit_to_db),
    path("edit-db/add-materialprovider", add_materialprovider_to_db),
    path("edit-db/add-machineprovider", add_machineprovider_to_db),

    path("edit-db/shortcut-add", shortcut_add),

    path("edit-db/save-daily-report", save_daily_report_to_db),
    path("edit-db/save-edit-daily-report", edit_daily_report_in_db),
    path("edit-db/del-daily-report/", del_daily_report_from_db),
    path("edit-db/edit-daily-report/", edit_daily_report_in_db),

    path("edit-db/del-position", del_position_from_db),
    path("edit-db/del-profession", del_profession_from_db),
    path("edit-db/del-machine", del_machine_from_db),
    path("edit-db/del-material", del_material_from_db),
    path("edit-db/del-contractor", del_contractor_from_db),
    path("edit-db/del-zone", del_zone_from_db),
    path("edit-db/del-unit", del_unit_from_db),
    path("edit-db/del-equipe", del_equipe_from_db),
    path("edit-db/del-task", del_task_from_db),
    path("edit-db/del-materialprovider", del_materialprovider_from_db),
    path("edit-db/del-machineprovider", del_machineprovider_from_db),


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
    path("edit-db/get-operations/", get_operations),
    path("edit-db/get-suboperations/", get_suboperations),
    path("edit-db/get-subtasks-of/<int:ID>/", get_subtasks_of),
    path("edit-db/get-zoneoperations/", get_zoneoperations),
    path("edit-db/get-all-equipes/", get_all_equipes),
    path("edit-db/get-equipes-in-report/", get_equipes_in_report),
    path("edit-db/get-freeAmount/", get_freeAmount),
    path("edit-db/get-zones/", get_zones),
    path("edit-db/get-materialproviders/", get_materialproviders),
    path("edit-db/get-machineproviders/", get_machineproviders),
    path("edit-db/check-deletability/", check_deletability),
    path("edit-db/check-editability/", check_editability),

    # path("edit-db/add-machine-to-daily-report", add_machine_to_daily_report),
]
