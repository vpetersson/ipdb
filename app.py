#!/usr/bin/env python

from bottle import request
from bottle import Bottle, run
from tabulate import tabulate
from datetime import datetime, timedelta
import json


app = Bottle()
db = {}


def append_ip(hostname, interface, ip, timestamp):
    payload = {
        'ip': ip,
        'hostname': hostname,
        'interface': interface,
        'timestamp': timestamp,
    }
    db['{}_{}'.format(hostname, interface)] = payload
    return payload


def get_ips():
    # Only display results newer than 48 hours.
    cutoff = datetime.utcnow() - timedelta(days=2)
    result = []

    for r in db.values():
        if r['timestamp'] > cutoff:
            record = [
                r['hostname'],
                r['interface'],
                r['ip'],
                r['timestamp'].strftime('%Y-%m-%d %H:%M'),
            ]
            result.append(record)
    return tabulate(
        result,
        headers=['Hostname', 'Interface', 'IP', 'Timestamp']
    )


@app.route('/submit', method='POST')
def do_submit():
    payload = json.load(request.body)
    ip = payload['ip']
    hostname = payload['hostname']
    interface = payload['interface']
    timestamp = datetime.utcnow()

    if ip and hostname and interface:
        append_ip(hostname, interface, ip, timestamp)
        return 'success\n'
    else:
        return 'fail\n'


@app.route('/')
def root():
    return '{}\n'.format(get_ips())

run(app, host='0.0.0.0', port=80)
