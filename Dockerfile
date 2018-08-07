FROM alpine 
RUN echo "nameserver 192.168.30.2" > /etc/resolv.conf \
	&& apk add --update \
    python \
    py-pip \
    --no-cache bash \
   	git \
   	&& git clone https://github.com/vmware/liota.git \
   	&& cd /liota \
   	&& python setup.py install \ 
   	&& cd /usr/lib/liota \ 
   	&& LIOTA_USER="root" ./post-install-setup.sh
ADD sampleProp.conf /usr/lib/liota/packages/sampleProp.conf
ADD graphite_bike_simulated.py /usr/lib/liota/packages/examples/graphite_bike_simulated.py
ADD run1.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh
ENTRYPOINT ./usr/local/bin/run.sh && /bin/sh
# ENTRYPOINT cd /usr/lib/liota/packages/ \
#	&& nohup bash -c "python ./liotad/liotad.py &" \
#	&& ./liotad/liotapkg.sh load examples/graphite_bike_simulated `sha1sum examples/graphite_bike_simulated.py | cut -d ' ' -f 1` \
#	&& sleep 5 \
#	&& /bin/sh \
#	&& tail -f /var/log/liota/liota.log
