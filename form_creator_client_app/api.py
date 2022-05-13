from form_creator_client_app.json_rpc import JSONRPCClient

API_ENDPOINT = 'http://127.0.0.1:8000/form-creator/api/form/'


class API:
    def __init__(self):
        self.client = JSONRPCClient(API_ENDPOINT)

    def get_form(self, uid):
        params = {'form_uid': uid}
        response = self.client.call('get_form', params)

        return self._get_form_context(response, uid)

    def post_form(self, uid, data):
        params = {'form_uid': uid, 'form_data': data}
        response = self.client.call('post_form', params)
        data = response.result

        if data['ok']:
            return data
        return self._get_form_context(response)

    def get_form_data(self, uid):
        params = {'form_uid': str(uid)}
        response = self.client.call('get_form_data', params)
        return {'form_data': response.result.get('form_data', [])}

    def _get_form_context(self, response, uid=None):
        form = response.result.get('form', None)
        if form:
            return {
                'form_data': {
                    'form_uid': uid,
                    'form': response.result['form']
                }
            }
        return {}
