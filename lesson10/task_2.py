import os

def walk(dir):
	res = {dir: 
			{
  				'dirs': [],
  				'files': []
  			}
  		}
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			res[dir]['files'].append(name)
		else:
			res[dir]['dirs'].append(name)
			walk(path)
	
	for key, value in res.items():
		print("{}: {}, {}".format(key, value['dirs'], value['files']))

walk(os.getcwd())