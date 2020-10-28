### DB pinger service
This is a simple tool to check DB services and emit metrics to statsd daemon

These metrics will be included:
- The status of DB endpoint: stats.gauges.mysql001_status 0|1
- The latency of the query (query content should be defined in config first): stats.timer.mysql001_duration value|ms

### How to run
- Edit the config file (config.yaml) accordingly to your need
- Build the docker image: ```docker build -t pinger .```
- Run the container: ```docker run -it pinger```
