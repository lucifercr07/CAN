import re
import json
import os

d = {}
d["events"] = [{}]
'''
with open("./auth_log.log", "r") as auth_log_file:
	auth_log_string = auth_log_file.read() 

auth_log_string = auth_log_string.split("\n")
for i in range(1, len(auth_log_string)):
	if "authentication failure" in auth_log_string[i]:
		d["events"][0]["text"] = auth_log_string[i] 
		x = json.dumps(d, ensure_ascii=False)
		with open("./test.json","w") as output_file:
			output_file.write(x)
		command = "curl -k -X POST http://10.5.29.236:9000/api/v1/events/ingest/4C4C4544-0037-5910-805A-C4C04F585831 --upload-file ./test.json"
		os.system(command)

'''

with open("/var/log/liota/liota.log","r") as log_file:
	log_string = log_file.read()

response_string = log_string.split("INFO")
length_error = len(response_string)
for i in range(1,length_error):
	error_string = response_string[i]
	d["events"][0]["text"] = error_string 
	x = json.dumps(d, ensure_ascii=False)
	with open("./test.json","w") as output_file:
		output_file.write(x)
	command = "curl -k -X POST http://10.5.29.236:9000/api/v1/events/ingest/4C4C4544-0037-5910-805A-C4C04F585831 --upload-file ./test.json"
	os.system(command)
