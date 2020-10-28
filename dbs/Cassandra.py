from cassandra.cluster import Cluster

class Cassandra:
  def __init__(self,endpoint):
    if endpoint['user'] != '' or endpoint['password'] != '':
      self.cred = {'username':endpoint['user'], 'password': endpoint['password']}
      self.cluster = Cluster([endpoint['ip']], port=endpoint['port'], auth_provider=self.cred,control_connection_timeout=endpoint['timeout'])
    else:
      self.cluster = Cluster([endpoint['ip']], port=endpoint['port'],control_connection_timeout=endpoint['timeout'])
    self.session = self.cluster.connect()

  def _excute(self,q):
    try:
      self.res = self.session.execute(q)
    except:
      return
    self.cluster.shutdown()
    return self.res