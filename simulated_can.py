import Queue

from liota.device_comms.can_device_comms import CanDeviceComms 
from liota.entities.metrics.metric import Metric

def can_connect():
	bus1 = CanDeviceComms(bustype='virtual')
	bus2 = CanDeviceComms(bustype='virtual')
	bus1.send(data=[1,2,3])
	bus2.receive()

can_connect()
