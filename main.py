import time
import yaml
from statsd import StatsClient
from dbs.Cassandra import Cassandra
from dbs.MySQL import MySQL
from dbs.MsSQL import MsSQL

def loadcnf():
	with open(r'config.yaml') as file:
		cnf = yaml.load(file, Loader=yaml.FullLoader)
	return cnf

def check_endpoint(dbtype,endpoint):
	_dbtype = {
		'mysql': MySQL,
		'mssql': MsSQL,
		'cassandra': Cassandra
	}

	try:
		conn = _dbtype.get(dbtype)(endpoint)
	except Exception as err:
		statsd.gauge(endpoint['hostname']+'_status',0)
		print("... DOWN ({})".format(err))
	else:
		statsd.gauge(endpoint['hostname']+'_status',1)
		_timer = statsd.timer(endpoint['hostname']+'_duration')
		_timer.start()
		res = conn._excute(endpoint['q'])
		print("... UP ({})".format(res))
		_timer.stop()


if __name__ == '__main__':
	cnf = loadcnf()
	statsd = StatsClient(host=cnf['statsd'][0]['ip'], port=str(cnf['statsd'][0]['port']))

	while True:
		for d in cnf['databases']:
			for endpoint in d['endpoints']:
				print("checking host: {}".format(endpoint['hostname']), end =" ")
				if 'q' not in endpoint or endpoint['q'] == '':
					endpoint['q'] = d['q']
				if 'timeout' not in endpoint or endpoint['timeout'] == '':
					endpoint['timeout'] = d['timeout']

				check_endpoint(d['type'],endpoint)
		print("=====")
		time.sleep(cnf['statsd'][0]['interval'])