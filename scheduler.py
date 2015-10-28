import sys
import json

'''
Parse JSON input file and build class data structure
'''
def parse_json_build_dict(content):

	try:
		classes = json.loads(content)
	except:
		exit("Error: File cannot be parsed as JSON.")

	classDict = {}
	for clazz in classes:
		clazz['isScheduled'] = 0
		classDict[clazz['name']] = clazz
	
	schedule_classes(classDict)

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
		exit("Error: File {filename} cannot be opened.")

	parse_json_build_dict(content)
