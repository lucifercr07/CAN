import can
import threading
import random
import time

bus1 = can.interface.Bus('test', bustype='virtual')
bus2 = can.interface.Bus('test', bustype='virtual')
TIME_OUT = 0.1

class testThread(threading.Thread):
	def __init__(self, threadId):
		threading.Thread.__init__(self)
		self.threadId = threadId

	def run(self):
		if self.threadId is 1:
			print("Sending message!!!")
			#threadLock.acquire()
			sendData()
			#threadLock.release()

		if self.threadId is 2:
			print("Receiving message: ")
			#threadLock.acquire()
			recvData()
			#threadLock.release()

def sendData():
	time.sleep(1)
	i=random.randint(1,200)
	msg1 = can.Message(arbitration_id=random.randint(0,2**11-1), data=[1+i,2+i,3+i])
	bus1.send(msg1)	

def recvData():
	time.sleep(1)
	msg2 = bus2.recv(TIME_OUT)
	print(list(msg2.data))

threadLock = threading.Lock()

while True:
	thread1 = testThread(1)
	thread1.start()
	thread1.join()
	thread2 = testThread(2)
	thread2.start()
	thread2.join()

	