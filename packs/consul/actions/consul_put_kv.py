from lib.action import ConsulAction

class ConsulKvPutAction(ConsulAction):

    def run(self, key, value):

        result = self.consul_put_kv(key, value)

        return result
