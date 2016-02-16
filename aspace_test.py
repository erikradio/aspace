import requests, json

aspace_url = 'http://localhost:8089'
username= 'admin'
password = 'admin'


auth = requests.post(aspace_url+'/users/'+username+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session}


# fake_repo_json=JSONModel(:repository){'name':'Basketball'}
# fake_repo_data
# rfake = requests.post(aspace_url+'/repositories',fakeRepo, headers=headers)

r = requests.get('http://localhost:8089/repositories', headers=headers)

#archives is 2



# dig_person = {'names':[{'primary_name':'Kramer','rest_of_name':'Cosmo','name_order':'inverted','sort_name':'Kramer,Cosmo','rules':'local'}]}
# dig_person_data = json.dumps(dig_person)
# dig_person_post = requests.post(aspace_url+'/agents/people',headers=headers,data=dig_person_data).json()

t=requests.get('http://localhost:8089/agents/people/2',headers=headers)


AO=requests.get('http://localhost:8089/repositories/2/resources?id_set=2',headers=headers).json()

# DO=requests.get('http://localhost:8089/repositories/2/digital_objects?all_ids=true',headers=headers).json()
DO=requests.get('http://localhost:8089/repositories/2/digital_objects/1',headers=headers).json()
# print DO['title']



# res_obj={'title':'Diary of Cosmo Kramer','level':'collection','language':'eng','dates':[{'date_type':'single','begin':'2011','label':'publication'}],'extents':[{'number':'12','portion':'whole','extent_type':'volumes'}],'id_0':'ksrl_44.3_kramer'}
# res_obj_data = json.dumps(res_obj)
# res_obj_post = requests.post(aspace_url+'/repositories/2/resources',headers=headers,data=res_obj_data).json()


# to update you need the id of the record and the full record plus new info
# lock version?
# update_res={'lock_version':'0','title':'Diary of Cosmo Kramer','linked_agents':[{'role':'creator','ref':'/agents/people/3','relator':'act'}],'level':'collection','language':'eng','dates':[{'date_type':'single','begin':'2011','label':'publication'}],'extents':[{'number':'12','portion':'whole','extent_type':'volumes'}],'id_0':'ksrl_44.3_kramer'}
# update_res_obj_data = json.dumps(update_res)
# update_res_obj_post = requests.post(aspace_url+'/repositories/2/resources/2',headers=headers,data=update_res_obj_data).json()

# make a digital object
# do={'title':'Shark Week','digital_object_type':'moving_image','file_versions':[{'file_uri':'www.sharkweek.org'}],'dates':[{'date_type':'single','begin':'2000-10-10','calendar':'gregorian','era':'ce','label':'broadcast'}],'rights_statement':'this work is in the public domain','digital_object_id':'www.handle.com/3333333'}
# do_data=json.dumps(do)
# do_post=requests.post(aspace_url+'/repositories/2/digital_objects',headers=headers,data=do_data).json()

# SR=requests.get('http://localhost:8089/subjects?id_set=3',headers=headers).json()
# print SR

subject={'terms':[{'term':'Great Pyramid (Egypt)','vocabulary':'/vocabularies/1','term_type':'geographic'}],'vocabulary':'/vocabularies/1','title':'Great Pyramid (Egypt)','authority_id':'http://id.loc.gov/authorities/subjects/sh85057002',
'source':'lcsh'}
subject_data=json.dumps(subject)
sub_post=requests.post(aspace_url+'/subjects',headers=headers,data=subject_data).json()
print sub_post



