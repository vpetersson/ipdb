#!/bin/bash
INTERFACE="$1"
IP="$(ip -4 -o addr show dev $INTERFACE | awk '{split($4,a,"/");print a[1]}')"
HOSTNAME="$(hostname -f)"
ENDPOINT="http://MyServer/submit"

curl \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{'ip': $IP, 'hostname': $HOSTNAME, 'interface': $INTERFACE}" \
  $ENDPOINT
