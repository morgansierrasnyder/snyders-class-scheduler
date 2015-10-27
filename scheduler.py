import sys
import json

def parse_json(content):
	print content


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

	parse_json(content)