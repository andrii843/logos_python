import sys

def iter_file(filename):
	for line in open(filename, 'r'):
		if len(line) > 40 :
			yield line

for l in iter_file(sys.argv[1]):
	print(l)