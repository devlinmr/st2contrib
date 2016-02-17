import httplib
import requests

from st2actions.runners.pythonrunner import Action

class ConsulAction(Action):

    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.setup = config['setup']

    def consul_put_kv(key, value):
        url = self.setup['consul_api_url']
        url = url + '/kv/' + key
        response = requests.put(url=url, data=value)

        return validate_result(response)    

    def validate_result(result):
        if response.status_code in [httplib.OK, httplib.CREATED]:
            status = 'ok'
            error = None
        else:
            status = 'failure'
            error = response.text

        result = {
            'status_code': response.status_code,
            'status': status,
            'uploaded_file': remote_file,
        }

        if error:
            result['error'] = error

        return result