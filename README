# IPDB - A stupid simple IP database.

An in-memory IP database. Just add run a simple `curl` line and you're good to go.


## Submitting

By hand using `curl` directly:
```
$ curl -H "Content-Type: application/json" \
  -X POST -d '{"ip": "127.0.0.1", "hostname": "xyz", "interface":"wifi0"}' \
  http://YourServer/submit
```

Or by using `report.sh`:

```
./report.sh eth0
```

## Reporting

```
$ curl http://YourServer
Hostname    Interface    IP         Timestamp
----------  -----------  ---------  ----------------
xyz         wifi0        127.0.0.1  2015-11-05 11:42

```
