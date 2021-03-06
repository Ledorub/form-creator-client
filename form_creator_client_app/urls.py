from django.urls import path
from form_creator_client_app import views, apps

app_name = apps.APP_NAME

urlpatterns = [
    path(
        'form/<uuid:form_uid>/',
        views.FormView.as_view(),
        name='form'
    ),
    path(
        'form-submitted/<uuid:data_uid>/',
        views.form_submitted_view,
        name='form-submitted'
    ),
    path(
        'data/<uuid:form_uid>/',
        views.DataView.as_view(),
        name='data'
    ),
]
