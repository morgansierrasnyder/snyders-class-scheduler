import sys
import json

def parse_content(content):
	try:
		classes = json.load(content)
	except:
		exit("Error: JSON File cannot be parsed.")


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

	parse_content(content)