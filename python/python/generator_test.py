# Generators

def super_generator(file_path):
	with open(file_path, 'r') as f:
		for x in f:
			yield(x)

in_file = '/Users/bmosley/Desktop/ResetITunesMigration.sh'
for x in super_generator(in_file):
	print(x.strip())
