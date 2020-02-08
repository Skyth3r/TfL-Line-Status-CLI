#!/usr/bin/env python
#coding:utf-8
# TfL Line Status CLI
# Takes a command line argument (of a TfL line) and chceks the status of the line

import json, requests, sys

if __name__ == '__main__':
	if len(sys.argv) == 2:
		tfl_input_line = sys.argv[1]
		tfl_input_line = tfl_input_line.lower()
		tfl_tube_status_url = "https://api.tfl.gov.uk/line/mode/tube/status"
		tfl_response = requests.get(tfl_tube_status_url, timeout=10)
		if tfl_response.status_code != 200:
			print("Error - Status Code: {}".format(tfl_response.status_code))
		else:
			tfl_response_json = tfl_response.json()
			for item in tfl_response_json:
				if tfl_input_line == item["id"]:
					print("{} line status: {}".format(item["name"], item["lineStatuses"][0]["statusSeverityDescription"]))
					exit()
	else:
		print("Error: script only accepts one argument. This should be the name of the TfL line that you wish to check the status of")
		exit()