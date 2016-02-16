import requests, json,csv,uuid,re
from jsonpatch import JsonPatch
from re import match

aspace_url = "http://localhost:8089"
username= "admin"
password = "admin"


auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}


with open("Endacott_Society_Metadata.csv","rU") as csvFile:
	reader=csv.DictReader(csvFile)
	##get repository
	# rep = requests.get(aspace_url+""/repositories",headers=headers).json()
	# print(rep)
	# kill = requests.delete(aspace_url+"/repositories/2/resources/3",headers=headers).json()
	# print(kill)

	#get resources
	# res=requests.get(aspace_url+"/repositories/2/resources?all_ids=true")
	# print(res)
	##delete resource
	# delete=requests.delete(aspace_url+"/repositories/3/resources/1")
	# print(delete)
	# get archival objects



	# #post endacott collection
	# end_coll={"title":"endacott society oral histories","language":"eng","level":"collection","id_0":"1234","jsonmodel_type":"resource","dates":[{"date_type":"single","begin":"2004","label":"existence"}],"extents":[{"number":"1","portion":"whole","extent_type":"cassettes"}]}
	# end_coll_post=requests.post(aspace_url+"/repositories/2/resources",headers=headers,data=json.dumps(end_coll)).json()
	# print(end_coll_post)
	#
	# # post endacott items
	# arch_children=[]
	# for row in reader:
	# 	title=row["Title"]
	# 	identifier=row["FileNameAccess"]
	# 	date=row["dateCreated(original)"]
	#
	# 	#make json records for each item
	# 	end_items={"title":title,"level":"item","id_0":identifier,"language":"eng","jsonmodel_type":"archival_object","dates":[{"date_type":"single","begin":"2004","label":"existence"}],"extents":[{"number":"1","portion":"whole","extent_type":"cassettes"}]}
	# 	#put items into json array
	# 	arch_children.append(end_items)
	# 	#make new JSON with previous array as value
	# 	end_children={"children":arch_children,"jsonmodel_type":"archival_record_children"}
	#
	# end_chil_post=requests.post(aspace_url+"/repositories/2/resources/4/children",headers=headers,data=json.dumps(end_children)).json()

	# get updated endacott
	# updated_end=requests.get(aspace_url+"/repositories/2/resources/2",headers=headers).json()
	# print(updated_end)
	# # update title of resource
	# test=JsonPatch([{"op": "replace", "path":"/title", "value":"star trek oral histories"}])
	# applyPatch=test.apply(updated_end,in_place=True)
	# new_end=requests.post(aspace_url+"/repositories/2/resources/2",headers=headers,data=json.dumps(applyPatch)).json()

	# create digital objects
	# make digital endacott collection
	# dig_end={"title":"star trek digital oral histories","digital_object_id":"uri.com","level":"collection","jsonmodel_type":"digital_object","linked_instances":[{"ref":"repositories/2/resources/1"}]}
	# end_digPost=requests.post(aspace_url+"/repositories/2/digital_objects",headers=headers,data=json.dumps(dig_end)).json()

	# get star trek dig obj
	# strtrk=requests.get(aspace_url+"/repositories/2/digital_objects/1",headers=headers).json()
	# add link
	# Link=[{"instance_type":"file_version","file_uri":"www.uri.com","xlink_actuate_attribute":"onRequest","xlink_show_attribute":"new"}]
	# Linkpatch=JsonPatch([{"op":"add","path":"/file_versions","value":Link}])
	# addLink=Linkpatch.apply(strtrk,in_place=True)
	# newstrtrk=requests.post(aspace_url+"/repositories/2/digital_objects/1",headers=headers,data=json.dumps(addLink)).json()
	# print(newstrtrk)


	#link Resource to Digital Resource
	# end_instance=[{"instance_type":"digital_object","digital_object":{"ref":digital_object_uri}}]
	# update=JsonPatch([{"op": "add", "path":"/instances", "value":end_instance}])
	# applyupdate=update.apply(updated_end,in_place=true)
	# print(updated_end)

	#uris are /path/to/thing
	#identifier = filename

	# Create digital object components of endacott(star trek) collection

	# ao=requests.get(aspace_url+"/repositories/2/resources/2/tree",headers=headers).json()
	#
	# dig_children=[]
	# for x in ao["children"]:
	# 	title=x["title"]
	# 	record_uri=x["record_uri"]
	#
	# 	dig_item={"title":title,"uri":"www.fakeuri.com","digital_object_id":"fakeid","level":"image","type":"sound recording","jsonmodel_type":"digital_object_component","file_versions":[{"instance_type":"file_version","file_uri":"www.uri.com","xlink_actuate_attribute":"onRequest","xlink_show_attribute":"new"}]}
	#
	# 	dig_children.append(dig_item)
	#
	# 	star_children={"children":dig_children,"jsonmodel_type":"digital_record_children"}
	#
	# dig_post=requests.post(aspace_url+"/repositories/2/digital_objects/1/children",headers=headers,data=json.dumps(star_children)).json()
	# print(dig_post)

	# create digital objects
	# dig_objs=[]
	# ao=requests.get(aspace_url+"/repositories/2/resources/3/tree",headers=headers).json()
	# for x in ao["children"]:
	# 	title=x["title"]
	# 	record_uri=x["record_uri"]
	#
	# 	dig_item={"title":title,"uri":"www.fakeuri.com","digital_object_id":record_uri,"level":"image","type":"sound recording","jsonmodel_type":"digital_object","file_versions":[{"instance_type":"file_version","file_uri":"www.uri.com","xlink_actuate_attribute":"onRequest","xlink_show_attribute":"new"}]}
	#
	# 	dig_post=requests.post(aspace_url+"/repositories/2/digital_objects",headers=headers,data=json.dumps(dig_item)).json()
	# 	print(dig_post)

	# for x in dig_objs:
	# 	dig_post=requests.post(aspace_url+"/repositories/2/digital_objects/",headers=headers,data=json.dumps(x)).json()
	# 	print(dig_post)

#----
# link AO to DO
# get the digital objects stored in json

	thing=[]
	digital_ob=[]
	for x in range(3,14):
		thing.append(str(x))
	for x in thing:
		do=requests.get(aspace_url+"/repositories/2/digital_objects?id_set="+x,headers=headers).json()
		digital_ob.append(do)
	ao=requests.get(aspace_url+"/repositories/2/resources/4/tree",headers=headers).json()

	arch_children=[]
	arch_records=[]
	#compare titles for matching
	for x in ao['children']:


		atitle=x['title']
		arecord=str(x['id'])

		arch_records.append(str(arecord))

		for z in digital_ob:
			for y in z:

				dtitle=y['title']
				digrecord_uri=y['uri']

				if atitle==dtitle:
					dig_instance=[{"instance_type":"digital_object","digital_object":{"ref":digrecord_uri}}]
					update=JsonPatch([{"op": "add", "path":"/instances", "value":dig_instance},{"op":"add","path":"/lock_version","value":"1"}])
					applyupdate=update.apply(x,in_place=True)

		newInstances=requests.post(aspace_url+"/repositories/2/archival_objects/"+arecord,headers=headers,data=json.dumps(applyupdate)).json()
		print(newInstances)

					# end_children={"id":arecord,"jsonmodel_type":"archival_object"}

		#
		#










	# print(arch_children.text)
		# dtitle=x["title"]
		#
		# digrecord_uri=x["record_uri"]
		# digID=x['id']
	#
	# 	dig_instance=[{"instance_type":"digital_object","digital_object":{"ref":digrecord_uri}}]
	# 	update=JsonPatch([{"op": "add", "path":"/instances", "value":dig_instance}])
	#
	#
	#
	# 	for y in ao['children']:
	#
	# 		atitle=y['title']
	# 		archrecord_uri=y['record_uri']
	#
	# 		if dtitle==atitle:
	#
	#
	#  			applyupdate=update.apply(y,in_place=True)
	#
	#
	#
	# 			arch_children.append(applyupdate)
	# 			end_children={"children":arch_children,"jsonmodel_type":"archival_record_children"}
	# newInstances=requests.post(aspace_url+"/repositories/2/resources/3/children",headers=headers,data=json.dumps(end_children)).json()
	# print(newInstances)

# ------
	# link archival objects to digital object components--not actually possible!
	# ao=requests.get(aspace_url+"/repositories/2/resources/3/tree",headers=headers).json()
	# do=requests.get(aspace_url+"/repositories/2/digital_objects/1/tree",headers=headers).json()
	# arch_children=[]
	# for x in do["children"]:
	# 	dtitle=x["title"]
	# 	digrecord_uri=x["record_uri"]
	# 	digID=x['id']
	#
	# 	dig_instance=[{"instance_type":"digital_object","digital_object":{"ref":digrecord_uri}}]
	# 	update=JsonPatch([{"op": "add", "path":"/instances", "value":dig_instance}])
	#
	#
	#
	# 	for y in ao['children']:
	#
	# 		atitle=y['title']
	# 		archrecord_uri=y['record_uri']
	#
	# 		if dtitle==atitle:
	#
	#
	#  			applyupdate=update.apply(y,in_place=True)
	#
	#
	#
	# 			arch_children.append(applyupdate)
	# 			end_children={"children":arch_children,"jsonmodel_type":"archival_record_children"}
	# newInstances=requests.post(aspace_url+"/repositories/2/resources/3/children",headers=headers,data=json.dumps(end_children)).json()
	# print(newInstances)

	# newInstances=requests.get(aspace_url+"/repositories/2/resources/2/tree",headers=headers).json()
	# for x in newInstances['children']:
	# 	url=x['record_uri']
	# 	if match("^.*/repositories/2/archival_objects/[1]?[1-3]?$", url): print("don't delete: {}".format(url))
	#
	# 	# newInstances=requests.delete(aspace_url+"/repositories/2/resources/2/archival_object/id="+x,headers=headers).json()

	# d_titles_and_uris = [(x['title'], x['record_uri']) for x in do['children']]

	#
	# a_titles_and_uris = [(x['title'], x['record_uri']) for x in ao['children']]
	#
	# atitles = [x[0] for x in a_titles_and_uris]
	# dtitles = [x[0] for x in d_titles_and_uris]
	#
	# dset = set(dtitles)
	# aset = set(atitles)
	#
	# commons = dset.intersection(aset)
	#
	#
	# for titles in commons:
			#do stuff, using the first two lists as references for uris







# curl -H "X-ArchivesSpace-Session: $SESSION" "http://localhost:8089/repositories/2/resources?all_ids=true"

#archives is 2



# dig_person = {"names":[{"primary_name":"Kramer","rest_of_name":"Cosmo","name_order":"inverted","sort_name":"Kramer,Cosmo","rules":"local"}]}
# dig_person_data = json.dumps(dig_person)
# dig_person_post = requests.post(aspace_url+"/agents/people",headers=headers,data=dig_person_data).json()

# t=requests.get("http://localhost:8089/agents/people/2",headers=headers)


# AO=requests.get("http://localhost:8089/repositories/2/resources?id_set=2",headers=headers).json()

# DO=requests.get("http://localhost:8089/repositories/2/digital_objects?all_ids=true",headers=headers).json()
# DO=requests.get("http://localhost:8089/repositories/2/digital_objects/1",headers=headers).json()
# print DO["title"]



# res_obj={"title":"Diary of Cosmo Kramer","level":"collection","language":"eng","dates":[{"date_type":"single","begin":"2011","label":"publication"}],"extents":[{"number":"12","portion":"whole","extent_type":"volumes"}],"id_0":"ksrl_44.3_kramer"}
# res_obj_data = json.dumps(res_obj)
# res_obj_post = requests.post(aspace_url+"/repositories/2/resources",headers=headers,data=res_obj_data).json()


# to update you need the id of the record and the full record plus new info
# lock version?
# update_res={"lock_version":"0","title":"Diary of Cosmo Kramer","linked_agents":[{"role":"creator","ref":"/agents/people/3","relator":"act"}],"level":"collection","language":"eng","dates":[{"date_type":"single","begin":"2011","label":"publication"}],"extents":[{"number":"12","portion":"whole","extent_type":"volumes"}],"id_0":"ksrl_44.3_kramer"}
# update_res_obj_data = json.dumps(update_res)
# update_res_obj_post = requests.post(aspace_url+"/repositories/2/resources/2",headers=headers,data=update_res_obj_data).json()

# make a digital object
# do={"title":"Shark Week","digital_object_type":"moving_image","file_versions":[{"file_uri":"www.sharkweek.org"}],"dates":[{"date_type":"single","begin":"2000-10-10","calendar":"gregorian","era":"ce","label":"broadcast"}],"rights_statement":"this work is in the public domain","digital_object_id":"www.handle.com/3333333"}
# do_data=json.dumps(do)
# do_post=requests.post(aspace_url+"/repositories/2/digital_objects",headers=headers,data=do_data).json()

# SR=requests.get("http://localhost:8089/subjects?id_set=3",headers=headers).json()
# print SR

# subject={"terms":[{"term":"Great Pyramid (Egypt)","vocabulary":"/vocabularies/1","term_type":"geographic"}],"vocabulary":"/vocabularies/1","title":"Great Pyramid (Egypt)","authority_id":"http://id.loc.gov/authorities/subjects/sh85057002",
# "source":"lcsh"}
# subject_data=json.dumps(subject)
# sub_post=requests.post(aspace_url+"/subjects",headers=headers,data=subject_data).json()
# print sub_post



# bhl_repo = {
 #    "name":"sharkweek",
 #    "org_code":"sw",
 #    "repo_code":"sw",
 #    "parent_institution_name":"University of the Ocean"
 #    }

	# post_repo = requests.post("http://localhost:8089/repositories",headers=headers,data=json.dumps(bhl_repo)).json()
	# print (post_repo)
