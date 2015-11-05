#!/bin/bash

if [ -z "$1" ]; then
  echo "Aborting. No interface provided."
  exit 1
fi

INTERFACE="$1"
IP="$(ip -4 -o addr show dev $INTERFACE | awk '{split($4,a,"/");print a[1]}')"
HOSTNAME="$(hostname -f)"
SERVER="http://YourServer"

curl \
  -H "Content-Type: application/json" \
  -X POST \
  -d "{\"ip\":\"$IP\",\"hostname\":\"$HOSTNAME\",\"interface\":\"$INTERFACE\"}" \
  $SERVER/submit
