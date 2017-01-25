import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match

aspace_url = "http://archivesspacedev.library.arizona.edu:8089"
username= "radio"
password = "B5rds-on-mind6"

#this script creates agents in aspace

auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()

session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}

# print(headers)

with open("final_accession.csv","rU") as csvFile:
	reader=csv.DictReader(csvFile)
	for row in reader:

		DonorFamily = row['Donor-family']
		CorpDonor = row['Donor-corporate']
		DonorLname = row['Donor_last_name']
		DonorFname = row['Donor_first_name']

		agents=requests.get(aspace_url+"/agents/people?id_set=52",headers=headers).json()

		if len(DonorLname)>0:
			agent_record={"jsonmodel_type":"agent_person","title":DonorFname+", "+DonorLname,
			"names":[{"is_display_name":True,"sort_name_auto_generate":False,"sort_name":DonorLname+", "+DonorFname,"rules":"local","jsonmodel_type":"name_person","rest_of_name":DonorFname,"primary_name":DonorLname,"name_order":"direct"}]}
			agent_post=requests.post(aspace_url+"/agents/people",headers=headers,data=json.dumps(agent_record)).json()
			print(agent_post)
		if len(CorpDonor)>0:
			agent_record={"jsonmodel_type":"agent_corporate_entity","title":CorpDonor,"names":[{"is_display_name":True,"sort_name_auto_generate":True,"rules":"local","jsonmodel_type":"name_corporate_entity","primary_name":CorpDonor,"name_order":"inverted"}]}
			agent_post=requests.post(aspace_url+"/agents/corporate_entities",headers=headers,data=json.dumps(agent_record)).json()
			print(agent_post)
		if len(DonorFamily)>0:
			agent_record={"jsonmodel_type":"agent_family","title":DonorFamily,
			"names":[{"is_display_name":True,"sort_name_auto_generate":False,"sort_name":DonorFamily,"rules":"local","jsonmodel_type":"name_family","family_name":DonorFamily,"name_order":"direct"}]}
			agent_post=requests.post(aspace_url+"/agents/families",headers=headers,data=json.dumps(agent_record)).json()
			print(agent_post)
