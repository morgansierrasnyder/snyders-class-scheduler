#!/usr/bin/env python

import sys
import json
import validator

'''
Data validation switches
'''
FORMAT_CHECK = 1 # If 1, check for correct format of JSON datastructure
EXIST_CHECK = 1 # If 1, check for invalid prerequisites in JSON
CYCLE_CHECK = 1 # If 1, check for cyclical relationships in JSON

'''
Parse JSON input file and build class data structure
'''
def _parse_and_validate_json(class_data):

	try:
		classes = json.loads(class_data)
	except:
		exit("Error: File cannot be parsed as JSON.")

	class_dict = _build_class_dict(classes)

	if FORMAT_CHECK:
		if not validator.check_format(class_dict):
			exit("Error: File data is formatted incorrently.")
	if EXIST_CHECK:
		if not validator.check_existence(class_dict):
			exit("Error: File data contains invalid prerequisites.")
	if CYCLE_CHECK:
		if not validator.check_cycles(class_dict):
			exit("Error: File data contains cyclical prerequisite relationships.")
	
	return class_dict

'''
Build a dict (map) data structure from class information
'''
def _build_class_dict(class_data):

	class_dict = {}
	for clazz in class_data:
		clazz['is_scheduled'] = 0
		class_dict[clazz['name']] = clazz
	
	return class_dict

'''
Schedule classes via a recursive DFS over all connected components
'''
def schedule_classes(class_data):

	class_dict = _parse_and_validate_json(class_data)

	def _schedule(clazz):

		if clazz['is_scheduled']:
			return
		if len(clazz['prerequisites']):
			for prereq in clazz['prerequisites']:
				_schedule(class_dict[prereq])

		clazz['is_scheduled'] = 1
		print clazz['name']

	for clazz in class_dict.values():
		_schedule(clazz)


if __name__ == '__main__':

	if len(sys.argv) < 2:
		exit("Error: No argument provided.")
	if len(sys.argv) > 2:
		exit("Error: More than one argument provided.")
	
	filename = sys.argv[1]

	try:
		f = open(filename, 'r')
		class_data = f.read()
	except IOError as e:
		exit("Error: File " + filename + " cannot be opened.")

	schedule_classes(class_data)
