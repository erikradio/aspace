import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match
from requests.auth import HTTPDigestAuth
#this script creates accessions from a csv
#its also very poorly written, but it works

aspace_url = ""
auth=()


auth = requests.post(aspace_url+"users/"+auth[0]+"/login?password="+auth[1])
auth.raise_for_status()
auth_json=auth.json()
session = auth_json["session"]
headers = {"X-ArchivesSpace-Session":session}
# print(session)

# print(auth)

# print(headers)

with open("plz.csv","rU") as csvFile:
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

		print(AccNo)

		if len(Provenance) > 0 and len(AccType) > 0 and len(Size) > 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","extent_type":"linear_feet","portion":"whole","number":Size}],
			"resource_type":"collection","acquisition_type":AccType,"general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_records)).json()
			print(acc_records)

		if len(Provenance) > 0 and len(AccType)==0 and len(Size) >  0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","extent_type":"linear_feet","portion":"whole","number":Size}],
			"resource_type":"collection","acquisition_type":"gift","general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=json.dumps(acc_records)).json()
			print(acc_post)




		if len(Provenance) == 0 and len(AccType) > 0 and len(Size) > 0:
			acc_data={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","portion":"whole","extent_type":"cubic_feet","number":Size,}],
			"content_description":Abstract,"resource_type":"collection","acquisition_type":AccType,"general_note":Notes}
			acc_json=json.dumps(acc_data)
			acc_post=requests.post(aspace_url+"/repositories/2/accessions",headers=headers,data=acc_json).json()

			print(acc_post)
		if len(Provenance) == 0 and len(AccType) == 0 and len(Size) > 0:
			acc_data={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"extents":[{"jsonmodel_type":"extent","portion":"whole","extent_type":"cubic_feet","number":Size,}],
			"content_description":Abstract,"resource_type":"collection","general_note":Notes}

			acc_post=requests.post(aspace_url+"/repositories/2/accessions",data=json.dumps(acc_data),headers=headers,).json()
			print(acc_post)

		if len(Provenance) > 0 and len(AccType) > 0 and len(Size) == 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"resource_type":"collection","acquisition_type":AccType,"general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}

			acc_post=requests.post(aspace_url+"/repositories/2/accessions",data=json.dumps(acc_data),headers=headers,).json()
			print(acc_post)

		if len(Provenance) == 0 and len(AccType) > 0 and len(Size) == 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"resource_type":"collection","acquisition_type":AccType,"general_note":Notes,"content_description":Abstract}

			acc_post=requests.post(aspace_url+"/repositories/2/accessions",data=json.dumps(acc_data),headers=headers,).json()
			print(acc_post)

		if len(Provenance) > 0 and len(AccType) == 0 and len(Size) == 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"resource_type":"collection","general_note":Notes,"content_description":Abstract,
			"provenance":Provenance}

			acc_post=requests.post(aspace_url+"/repositories/2/accessions",data=json.dumps(acc_data),headers=headers,).json()
			print(acc_post)

		if len(Provenance) == 0 and len(AccType) == 0 and len(Size) > 0:
			acc_records={"title":title,"id_0":AccNo,"jsonmodel_type":"accession","accession_date":AccDate,
			"resource_type":"collection","general_note":Notes,"content_description":Abstract}

			acc_post=requests.post(aspace_url+"/repositories/2/accessions",data=json.dumps(acc_data),headers=headers,).json()
			print(acc_post)
