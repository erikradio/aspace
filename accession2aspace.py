import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match

#this script creates accessions from a csv

aspace_url = "http://archivesspacedev.library.arizona.edu:8089"
username= "radio"
password = ""


auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}

# print(headers)

with open("final_accession.csv","rU") as csvFile:
	reader=csv.DictReader(csvFile)
	for row in reader:
		title = row['Collection_Title']
		CorpDonor = row['Donor_corporate']
		DonorLname = row['Donor_lname']
		DonorFname = ['Donor_fname']
		DonorFamily = ['Donor_family']
		AccDate = row['Accession_date']
		AccNo = row['Accession_Number']
		Size = row['Size']
		Format = row['Format']
		Location = row['Location']
		Tier = row['Tier']
		Subject = row['Subject']
		Abstract = row['Abstract']
		Notes = row['Notes']
		AccType = row['Acquisition_Type']
		Provenance = row['Provenance']
		# print(DonorLname)
		# test=requests.get(aspace_url+"/repositories/2/accessions/1",headers=headers).json()
		# print(test)
		# make json records for each accession
		# if len(Provenance) > 0 and len(AccType) > 0:
		# 	acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,"extents":[{"jsonmodel_type":"extent","extent_type":"linear_feet","number":Size}],"content_description":Abstract,"resource_type":"collection","acquisition_type":AccType,"general_note":Notes,"provenance":Provenance}
		# 	acc_as_json = json.dumps(acc_records)
		# 	print("#########################")
		# 	print("This is the acc record we're POSTing: \n{}".format(acc_as_json))
		# 	acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=acc_as_json)
		# 	print("#########################")
		# 	print("This is the (raw) response the web server sent:\n{}".format(acc_post.text))
		# 	print("#########################")
		# 	print("Now we're trying to make it into JSON")
		# 	acc_post_response_as_json = acc_post.json()
		# 	print("We successfully interpretted the webserver response as JSON: \n{}".format(acc_post_response_as_json))





		if len(Provenance) > 0 and len(AccType) > 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","extent_type":"linear_feet","portion":"whole","number":Size}],
			"resource_type":"collection","acquisition_type":AccType,"general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_records)).json()
			print(acc_post.status_code)


			print(acc_post)
		if len(Provenance) > 0 and len(AccType)==0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","extent_type":"linear_feet","portion":"whole","number":Size}],
			"resource_type":"collection","acquisition_type":"gift","general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_records)).json()


			print(acc_post)




		if len(Provenance) == 0 and len(AccType) > 0:
			acc_data={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","portion":"whole","extent_type":"cubic_feet","number":Size,}],
			"content_description":Abstract,"resource_type":"collection","acquisition_type":AccType,"general_note":Notes}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_data)).json()

			print(acc_post)
		if len(Provenance) == 0 and len(AccType) == 0:
			acc_data={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","portion":"whole","extent_type":"cubic_feet","number":Size,}],
			"content_description":Abstract,"resource_type":"collection","acquisition_type":"gift","general_note":Notes}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_data)).json()
			print(acc_post)
