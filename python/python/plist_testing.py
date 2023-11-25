import json

some_json = '/Users/bmosley/Desktop/its_ppttest_regular.json'

with open(some_json) as json_blob:    
    resdata = json.load(json_blob)

    print(resdata)