
'''
Validate that the class data is formatted as expected and complete
'''
def check_format(classDict):

	for clazz in classDict.values():
		if not 'prerequisites' in clazz:
			return 0
		if not 'name' in clazz:
			return 0
	return 1


'''
Validate that all listed prerequisites exist
'''
def check_existence(classDict):
	
	for clazz in classDict.values():
		for prereq in clazz['prerequisites']:
			if not prereq in classDict:
				return 0
	return 1

'''
Validate that there are no first order cyclical prerequisite relationships
'''
def check_cycles(classDict):

	for clazz in classDict.values():
		for prereq in clazz['prerequisites']:
			if clazz['name'] in classDict[prereq]['prerequisites']:
				return 0
	return 1
