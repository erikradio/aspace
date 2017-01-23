import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match

#this script creates accessions from a csv

aspace_url = "http://localhost:8089"
username= "admin"
password = "admin"


auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}

# print(headers)

with open("accTestBatch.csv","rU") as csvFile:
	reader=csv.DictReader(csvFile)
	for row in reader:
		title = row['Collection_Title']

		CorpDonor = row['Donor-corporate']
		DonorLname = row['Donor_last_name']
		DonorFname = ['Donor_first_name	']
		AccDate = row['Accession_date']
		AccNo = row['Accession_Number']
		Size = row['Size']
		Format = row['Format']
		Location = row['Location']
		Tier = row['Tier']
		Subject = row['Subject']
		Abstract = row['Abstract']
		Notes = row['Notes']
		RecType = row['resource_type']
		AccType = row['acquisition_type']
		# print(DonorLname)
		# test=requests.get(aspace_url+"/repositories/2/accessions/1",headers=headers).json()
		# print(test)
		#make json records for each accession
		# if len(DonorLname) > 0:
		# 	acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
		# 	"extents":[{"jsonmodel_type":"extents","extent_type":"cubic_feet","number":Size,}],
		# 	"content_description":Abstract,"resource_type":RecType,"acquisition_type":AccType,"general_note":Notes,
		# 	"provenance":"Donated by "+DonorFname+' '+DonorLname}
		# 	acc_data=json.dumps(acc_records)
		# 	acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=acc_data).json()
		# 	print(acc_post)
		if len(CorpDonor) > 0:
			acc_data=json.dumps({"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,"extents":[{"jsonmodel_type":"extents","extent_type":"cubic_feet","number":Size}],"content_description":Abstract,"resource_type":RecType,"acquisition_type":AccType,"general_note":Notes,"provenance":CorpDonor})

			acc_post=requests.post(aspace_url+"/repositories/2/accessions/",headers=headers,data=acc_data).json()
			print(acc_post)
		# else:
		# 	acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
		# 	"extents":[{"jsonmodel_type":"extents","extent_type":"cubic_feet","number":Size,}],
		# 	"content_description":Abstract,"resource_type":RecType,"acquisition_type":AccType,"general_note":Notes}
		# 	acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_records)).json()
		# 	print(acc_post)
