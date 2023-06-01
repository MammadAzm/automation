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
    path("home/create-report/", create_report_template),
    path("home/daily-reports/", reports_daily),
    path("home/daily-reports/<idd>", report_on_day),

    # Edit DB paths
    path("edit-db/add-position", add_position_to_db),
    path("edit-db/add-profession", add_profession_to_db),
    path("edit-db/add-machine", add_machine_to_db),
    path("edit-db/add-material", add_material_to_db),
    path("edit-db/save-daily-report", save_daily_report_to_db),
    path("edit-db/del-daily-report/", del_daily_report_from_db),

    path("edit-db/del-position", del_position_from_db),
    path("edit-db/del-profession", del_profession_from_db),
    path("edit-db/del-machine", del_machine_from_db),
    path("edit-db/del-material", del_material_from_db),

    path("edit-db/get-options/<typee>", get_options),
    path("edit-db/get-units/", get_units),

    # path("edit-db/add-machine-to-daily-report", add_machine_to_daily_report),
]
