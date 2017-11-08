#!/bin/bash

echo "nameserver 192.168.30.2" > /etc/resolv.conf
cd /usr/lib/liota/packages/
x="dell5k-"
x+=`cat /etc/hostname`
y=\"$x\"
sed -i "s/^\(EdgeSystemName\s*=\s*\).*\$/\1$y/" /usr/lib/liota/packages/sampleProp.conf
y=`sha1sum examples/graphite_bike_simulated.py | cut -d ' ' -f 1`
python ./liotad/liotad.py &
nohup ./liotad/liotapkg.sh load examples/graphite_bike_simulated $y
sleep 5
tail -f /var/log/liota/liota.log
