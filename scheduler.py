#!/usr/bin/env python

import sys
import json
import validator

'''
Data validation switches
'''
formatCheck = 0 # If 1, check for correct format of JSON datastructure
existCheck = 0 # If 1, check for invalid prerequisites in JSON
cycleCheck = 0 # If 1, check for cyclical relationships in JSON

'''
Parse JSON input file and build class data structure
'''
def parse_and_validate_json(content):

	try:
		classes = json.loads(content)
	except:
		exit("Error: File cannot be parsed as JSON.")

	classDict = {}
	for clazz in classJSON:
		clazz['isScheduled'] = 0
		classDict[clazz['name']] = clazz
	
	schedule_classes(classDict)

'''
Build a dict (map) data structure from class information
'''
def _build_class_dict(classJSON):

	classDict = {}
	for clazz in classJSON:
		clazz['isScheduled'] = 0
		classDict[clazz['name']] = clazz
	
	return classDict

'''
Schedule classes via a recursive DFS over all connected components
'''
def schedule_classes(classDict):

	def _schedule(clazz):

		if clazz['isScheduled']:
			return
		if len(clazz['prerequisites']):
			for prereq in clazz['prerequisites']:
				_schedule(classDict[prereq])

		clazz['isScheduled'] = 1
		print clazz['name']

	for clazz in classDict.values():
		_schedule(clazz)


if __name__ == '__main__':

	if len(sys.argv) < 2:
		exit("Error: No argument provided.")
	if len(sys.argv) > 2:
		exit("Error: More than one argument provided.")
	
	filename = sys.argv[1]

	try:
		f = open(filename, 'r')
		content = f.read()
	except IOError as e:
		exit("Error: File " + filename + " cannot be opened.")

	classDict = parse_and_validate_json(content)
	schedule_classes(classDict)
