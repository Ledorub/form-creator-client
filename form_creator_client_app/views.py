from django.shortcuts import render, redirect, HttpResponse
from django import views
from form_creator_client_app.json_rpc import JSONRPCClient
from form_creator_client_app.api import API

api = API()


class FormView(views.View):
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
            return HttpResponse(context['data_uid'])
        return render(request, self.template_name, context)


class DataView(views.View):
    template_name = 'form_creator_client_app/data.html'

    def get(self, request, *args, **kwargs):
        context = api.get_form_data(self.kwargs['form_uid'])
        return render(request, self.template_name, context)
