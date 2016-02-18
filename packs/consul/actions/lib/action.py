import httplib
import requests

from st2actions.runners.pythonrunner import Action

class ConsulAction(Action):

    def __init__(self, config):
        super(ConsulAction, self).__init__(config)
        self.setup = config['setup']

    def consul_get_kv(self, key, recurse=False):
        url = self.setup['consul_api_url']
        url = url + '/kv/' + key
        if recurse:
          recurse = 'recurse'
        else
          recurse = None
        response = requests.get(url=url, data=recurse)

        return self._validate_result(response=response)    

    def consul_put_kv(self, key, value):
        url = self.setup['consul_api_url']
        url = url + '/kv/' + key
        response = requests.put(url=url, data=value)

        return self._validate_result(response=response)    

    def consul_del_kv(self, key recurse=False):
        url = self.setup['consul_api_url']
        url = url + '/kv/' + key
        if recurse:
          recurse = 'recurse'
        else
          recurse = None
        response = requests.delete(url=url, data=recurse)

        return self._validate_result(response=response)    

    def _validate_result(self, response):
        if response.status_code in [httplib.OK, httplib.CREATED]:
            status = 'ok'
            error = None
        else:
            status = 'failure'
            error = response.text

        result = {
            'status_code': response.status_code,
            'status': status,
            'error': error
        }

        if error:
            result['error'] = error

        return result