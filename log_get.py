import os
import json
import datetime
import time

prev_log_timestamp = -1



log_file = open('log_container.log', 'a')

user_info = os.popen("curl -k -X POST https://10.5.29.236:9543/api/v1/sessions --upload-file ./test.json").read()
data = json.loads(user_info)
sessionId = str(data["sessionId"])

curl_url = r'curl -k https://10.5.29.236:9543/api/v1/events/text/'
log_containing_error = r'CONTAINS%20Sample/timestamp/LAST%20604800000 --header '
session_token = r'"Authorization: Bearer ' + sessionId + "\""

command = curl_url + log_containing_error + session_token

logs_from_curl = os.popen(command).read()
error_log = json.loads(logs_from_curl)

error_log_list_length = len(error_log['events'])


latest_time_stamp =  error_log["events"][0]["timestamp"]
for i in range(0, error_log_list_length):
	log_file.write(error_log["events"][i]["text"])

'''
if prev_log_timestamp != latest_time_stamp:

	for i in range(1, error_log_list_length):
		time_stamp =  error_log["events"][i]["timestamp"]

		if abs(time_stamp - latest_time_stamp) <= 300:
			log_file.write(error_log["events"][i]["text"])

		#Send the logs from log_file to trained  model

	prev_log_timestamp = latest_time_stamp
	log_file.close()
	open('log_container.log', 'w').close() # To empty the file
	time.sleep(300)
'''



