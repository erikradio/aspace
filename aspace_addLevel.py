#python2
#looks for a particular value in level and changes it to file
import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match

aspace_url = "http://localhost:8089"
username= "admin"
password = "admin"


auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}




#get repository
# rep = requests.get(aspace_url+"/repositories",headers=headers).json()
# print rep

# get all resource ids
res=requests.get(aspace_url+"/repositories/2/resources?all_ids=True",headers=headers).json()
# print res
# get resource record
record=requests.get(aspace_url+"/repositories/2/resources/2",headers=headers).json()

#get elements and values in record
for key,value in record.items():
	if key=='level':
		#if the value is collection or something else
		if value=='collection':
			#change it to file
			test=JsonPatch([{"op": "replace", "path":"/level", "value":"file"}])
			applyPatch=test.apply(record,in_place=True)
		 	updated_level=requests.post(aspace_url+"/repositories/2/resources/2",headers=headers,data=json.dumps(applyPatch)).json()
