import os
import time

name = 'liota'
x = "while true; do ping 8.8.8.8; done"
for i in range(0,2):
	temp = name + str(i)
	os.system("docker run -td --name " + temp + " prashant")
	time.sleep(2)

'''
import docker
client = docker.from_env()
print client.containers.run("prashant", detach=False)
'''