from lib.action import ConsulAction

class ConsulKvPutAction(ConsulAction):

    def run(self, key, recurse):

        result = self.consul_get_kv(key, recurse)

        return result
