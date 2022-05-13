from django.shortcuts import render, redirect, reverse, HttpResponse
from django import views
from form_creator_client_app.api import API

api = API()


class FormView(views.View):
    """
    Asks API to retrieve a form, renders it and handles submission.
    """
    template_name = 'form_creator_client_app/form.html'

    def dispatch(self, request, *args, **kwargs):
        self.form_uid = str(kwargs.pop('form_uid'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = api.get_form(self.form_uid)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = api.post_form(self.form_uid, request.POST)

        if context['ok']:
            url_kwargs = {'data_uid': context['data_uid']}
            return redirect(
                reverse(
                    'form-creator-client-app:form-submitted',
                    kwargs=url_kwargs
                )
            )
        return render(request, self.template_name, context)


def form_submitted_view(request, data_uid):
    """
    Renders data_uid from url.
    Used as success_url.
    """
    return HttpResponse(f'DATA_UID: {data_uid}')


class DataView(views.View):
    """
    Returns all submitted data for a given form (form_uid).
    """
    template_name = 'form_creator_client_app/data.html'

    def get(self, request, *args, **kwargs):
        context = api.get_form_data(self.kwargs['form_uid'])
        return render(request, self.template_name, context)
