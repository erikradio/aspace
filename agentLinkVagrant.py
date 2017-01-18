import requests, json,csv,uuid,re,sys
from jsonpatch import JsonPatch
from re import match


aspace_url = "http://localhost:8089"
username= "admin"
password = "admin"
auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}


class Agent:
    def __init__(self, name, uri):
        self.name = name
        self.uri = uri
        self.linked_accessions = []


def get_agents_from_api():
    # Actually implement something here
    def get_people_agents():
        agent=requests.get(aspace_url+"/agents/people?all_ids=true").json()
	    agentList=[x for x in agent]
        for agent in agentList:
            agentData=requests.get(aspace_url+"/agents/people/"+str(agent),headers=headers).json()
            name=agentData['display_name']['sort_name']
            nameID=agentData['uri']
        return name,nameID

    def get_corp_agents():
        corp=requests.get(aspace_url+"/agents/corporate_entities?all_ids=true").json()
        corpList=[x for x in corp]
        for corp in corpList:
            corpData=requests.get(aspace_url+"/agents/corporate_entities/"+str(corp),headers=headers).json()
            name=corpData['display_name']['sort_name']
            nameID=corpData['uri']
        return name,nameID


    agents = []
    for name,uri in get_people_agents():
        agent = Agent(name, uri)
        agents.append(agent)

    for name,uri in get_corp_agents():
        agent = Agent(name, uri)
        agents.append(agent)

    return agents


def read_csv(path):
    rows = []
    with open(path) as f:
        reader = DictReader(f)
        for x in reader:
            rows.append(x)
    return rows

# updateAcc=requests.get(aspace_url+accURL,headers=headers).json()
#
# addAgentURL=JsonPatch([{"op": "add", "path":"/linked_agents", "value":[{"ref":agentURI,"role":"source","relator":"dnr"}]}])
#
# applyPatch=addAgentURL.apply(updateAcc,in_place=True)
# newAcc=requests.post(aspace_url+accURL,headers=headers,data=json.dumps(applyPatch)).json()


def update_accession(accession, agent):
    updateAcc = requests.get(aspace_url+accIDs,headers=headers).json()
    addAgentURL = JsonPatch([{"op": "add", "path":"/linked_agents", "value":[{"ref":agent.uri,"role":"source","relator":"dnr"}]}])
    applyPatch = addAgentURL.apply(updateAcc,in_place=True)
    newAcc = requests.post(aspace_url+"{}".format(accession),
                  data=applyPatch,headers=headers).json()


def main():
    path = sys.argv[1]
    agents = get_agents_from_api()
    csv_data = read_csv(csvpath)
    #get accession ids
    acc = requests.get(aspace_url+"/repositories/2/accessions?all_ids=true",headers=headers).json()
	accIDs=[x for x in acc]
    for x in accIDs:
        accession=x['uri']
    return accession

    for x in csv_data:
        # your logic may be more complicated here, so you may want to function
        # it out or not use a list comprehension, this is for example purposes
        # only
        agent = [x for x in agents if agents.name == x['DonorLname']+x['DonorFname']
        agent.linked_accessions.append(x['acc_id'])
    for agent in agents:
        for linked_accession in agent.linked_accessions:
            update_accession(linked_accession, agent)
