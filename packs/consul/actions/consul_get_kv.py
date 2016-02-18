from lib.action import ConsulAction

class ConsulKvPutAction(ConsulAction):

    def run(self, key, value):

        result = self.consul_get_kv(key)

        return result
