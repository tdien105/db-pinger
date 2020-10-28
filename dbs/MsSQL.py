import pymssql

class MsSQL:
  def __init__(self,endpoint):
    self.conn = pymssql.connect(server=endpoint['ip']+":"+str(endpoint['port']), user=endpoint['user'], password=endpoint['password'],timeout=endpoint['timeout'],login_timeout=endpoint['timeout'])

  def _excute(self,q):
    try:
      self.cursor = self.conn.cursor()
      self.cursor.execute(q)
      self.res = self.cursor.fetchall()
    except:
      return
    self.conn.close()
    return self.res