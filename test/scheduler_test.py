import unittest
import sys
from StringIO import StringIO

sys.path.append('../src')

import scheduler_script

def get_file_content(filename):
	try:
		f = open(filename, 'r')
		content = f.read()
	except IOError as e:
		exit("Test Error: File " + filename + " cannot be opened.")

	return content

class SchedulerTests(unittest.TestCase):

	def setUp(self):

		self.out = StringIO()
		self.old_out = sys.stdout
		sys.stdout = self.out

		self.err = StringIO()
		self.old_err = sys.stderr
		sys.stderr = self.err

	def tearDown(self):

		sys.stdout = self.old_out
		sys.stderr = self.old_err
		self.out.close()
		self.err.close()

	def test_empty_class_data(self):

		data = get_file_content('empty.json')
		scheduler.schedule_classes(data)

		self.assertEqual(str(self.out.getvalue()), "")

	def test_connected_class_tree(self):

		data = get_file_content('math.json')
		scheduler.schedule_classes(data)

		self.assertEqual(str(self.out.getvalue()), "Algebra 1\nGeometry\nAlgebra 2\nPre Calculus\n")

	def test_disconnected_class_tree(self):

		data = get_file_content('language.json')
		scheduler.schedule_classes(data)

		self.assertEqual(str(self.out.getvalue()), "German 1\nGerman 2\nGerman 3\nSpanish 1\nSpanish 2\nSpanish 3\n")

	def test_cross_connected_class_tree(self):

		data = get_file_content('premed.json')
		scheduler.schedule_classes(data)

		self.assertEqual(str(self.out.getvalue()),
			"Chemistry\nBiology\nOrganic Chemistry\nBiochemistry\nMicrobiology\nPathology\n")


if __name__ == "__main__":
	unittest.main()


