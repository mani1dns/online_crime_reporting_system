from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page),
    path('users',views.user_register),   #modules
    path('admin_user_home',views.admin_user),
    path('advocate_user_home',views.advocate_user),
    path('police_station_home',views.police_station_name),
    path('public_user_home/',views.public_user),
    path('complaints',views.complaint),
    path('feedback',views.feedbacks),
    path('crimes/',views.crime),
    path('police_station/',views.police_stations),
    path('crime_types_view/',views.crime_type_view),
    path('criminals/',views.criminal),
    path('found_report/',views.found_reports),
    path('crime_types',views.crime_type),
    path('rating',views.rating1),
    path('law_details/',views.law_detail),
    path('advocates_register',views.advocate_register),
    path('public_register',views.public_registers),
    path('advocate',views.advocate),
    path('case_types_manage',views.case_type_manage),
    path('criminal_found_report',views.criminal_found_report),
    path('stations',views.station),
    path('registered_users',views.registered_user),
    path('case_types',views.case_type),
    path('case_manage/',views.cases_manage),    #manage files
    path('criminals_manage',views.criminal_manage),
    path('crimes_manage',views.crime_manage),
    path('complaints_view',views.complaints_view),
    path('law_details_manage',views.law_detail_manage), 
    path('users_view/', views.user_view),   #admin module
    path('update_crime/<id>',views.update_crime), #police module
    path('delete_crime/<id>',views.delete_crime),  #police module
    path('update_criminal/<id>',views.update_criminal), #police module
    path('delete_criminal/<id>',views.delete_criminal), #police module
    path('update_stations/<id>',views.update_stations), #admin module
    path('delete_stations/<id>',views.delete_stations), #admin module
    path('update_crime_type/<id>',views.update_crime_type), #admin module
    path('delete_crime_type/<id>',views.delete_crime_type), #admin module
    path('updates/<id>',views.updates),
    path('delete/<id>',views.delete),
    path('delete/{{i.adv_id}}/{{i.login_id_id}}',views.advocate),
    path('update_case_type_manage/<id>',views.update_case_type_manage),
    path('delete_case_type_manage/<id>',views.delete_case_type_manage),
    path('update_law_detail_manage/<id>',views.update_law_detail_manage),
    path('delete_law_detail_manage/<id>',views.delete_law_detail_manage),
    path('found_report_insert/',views.found_report_insert),
    path('user_make_complaint/',views.user_make_complaint),
    path('upload_evidence/',views.upload_evidence),
    path('user_cases_view/<id>',views.user_cases_view),
]
