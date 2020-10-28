### DB pinger service
This is a simple tool to check DB services and emit metrics to statsd daemon

These metrics will be included:
- The status of DB endpoint: stats.gauges.mysql001_status 0|1
- The latency of the query (query content should be defined in config first): stats.timer.mysql001_duration value|ms

### How to run
- Edit the config file (config.yaml) accordingly to your need
- Build the docker image: ```docker build -t db-pinger .```
- Run the container:
```
docker run -it db-pinger

checking host: mysql001 ... UP ([('information_schema',), ('mysql',), ('performance_schema',), ('sys',)])
checking host: mysql002 ... DOWN (2003: Can't connect to MySQL server on '10.163.32.238:3306' (111 Connection refused))
checking host: mssql001 ... UP ([('Microsoft SQL Server 2017 (RTM-CU22) (KB4577467) - 14.0.3356.20 (X64) \n\tAug 20 2020 22:33:27 \n\tCopyright (C) 2017 Microsoft Corporation\n\tExpress Edition (64-bit) on Linux (Ubuntu 16.04.7 LTS)',)])
checking host: cassandra001 ... UP (<cassandra.cluster.ResultSet object at 0x7f42b7ee4820>)
=====
checking host: mysql001 ... UP ([('information_schema',), ('mysql',), ('performance_schema',), ('sys',)])
checking host: mysql002 ... DOWN (2003: Can't connect to MySQL server on '10.163.32.238:3306' (111 Connection refused))
checking host: mssql001 ... UP ([('Microsoft SQL Server 2017 (RTM-CU22) (KB4577467) - 14.0.3356.20 (X64) \n\tAug 20 2020 22:33:27 \n\tCopyright (C) 2017 Microsoft Corporation\n\tExpress Edition (64-bit) on Linux (Ubuntu 16.04.7 LTS)',)])
checking host: cassandra001 ... UP (<cassandra.cluster.ResultSet object at 0x7f42b7e53160>)
```

### Visualize on grafana

![grafana](https://i.imgur.com/6X3VtId.png)
