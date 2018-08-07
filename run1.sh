#!/bin/bash

echo "nameserver 192.168.30.2" > /etc/resolv.conf
cd /usr/lib/liota/packages/
y=`sha1sum examples/graphite_bike_simulated.py | cut -d ' ' -f 1`
python ./liotad/liotad.py &
sleep 5
nohup ./liotad/liotapkg.sh load examples/graphite_bike_simulated $y
tail -f /var/log/liota/liota.log
