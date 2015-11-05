# IPDB - A stupid simple IP database.

IPDB is a stupid simple IP database to keep track of devices and servers on your network.

The tool was born since my coworking place uses a weird DHCP configuration where they keep handing out new IPs as soon as the DHCP lease expires. This became very annoying, since I have a handful of Raspberry Pis at my desk that I need to SSH into throughout the day.

## Running

$ docker run -d -p 80:80 --name ipdb vpetersson/ipdb

## Submitting to the database

The recommend way is to download [report.sh](https://raw.githubusercontent.com/vpetersson/ipdb/master/report.sh) and simply run it as follows (probably hourly):

```
./report.sh eth0
```

Alternatively, you could submit IPs to the database using `curl` and do a POST directly:

```
$ curl -H "Content-Type: application/json" \
  -X POST -d '{"ip": "192.168.10.10", "hostname": "myserver.local", "interface": "eth0"}' \
  http://YourServer/submit
```

## Reporting

```
$ curl http://YourServer
Hostname                Interface    IP             Timestamp
----------------------  -----------  -------------  ----------------
some-service.local      wlan0        10.43.111.92   2015-11-05 16:00
other-server.local      wlan0        10.43.111.96   2015-11-05 16:00
foobar.local            eth0         10.43.108.10   2015-11-05 16:00
myserver.local          eth1         10.43.107.202  2015-11-05 16:00
```
