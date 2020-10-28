import mysql.connector

class MySQL:
  def __init__(self,endpoint):
    self.conn = mysql.connector.connect(host=endpoint['ip'], port=endpoint['port'], user=endpoint['user'], password=endpoint['password'],connection_timeout=endpoint['timeout'])

  def _excute(self,q):
    try:
      self.cursor = self.conn.cursor()
      self.cursor.execute(q)
      self.res = self.cursor.fetchall()
    except:
      return
    self.conn.close()
    return self.res