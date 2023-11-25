import json

with open('migrated_iTunes_Library_bmosley2_music.json') as json_data:
	d = json.load(json_data)
	for k in d['Tracks']:
		print k