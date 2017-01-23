import requests, json,csv,uuid,re,sys
from json import dumps
from jsonpatch import JsonPatch
from re import match

#this script links agents/donors to accession records

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

    def __repr__(self):
        return dumps(
            {'name': self.name, 'uri':self.uri,
             'linked_accessions': self.linked_accessions},
            indent=4
        )


def get_agents_from_api():
    # Actually implement something here
    def get_people_agents():
        agents=requests.get(aspace_url+"/agents/people?all_ids=true").json()
        agentList=[x for x in agents]
        for agent in agentList:
            agentData=requests.get(aspace_url+"/agents/people/"+str(agent),headers=headers).json()
            name=agentData['display_name']['sort_name']
            uri=agentData['uri']
            yield name,uri

    def get_corp_agents():
        corp=requests.get(aspace_url+"/agents/corporate_entities?all_ids=true").json()
        corpList=[x for x in corp]
        for corp in corpList:
            corpData=requests.get(aspace_url+"/agents/corporate_entities/"+str(corp),headers=headers).json()
            name=corpData['display_name']['sort_name']
            uri=corpData['uri']
            yield name,uri


    agents = []
    for name,uri in get_people_agents():
        agent = Agent(name, uri)
        agents.append(agent)

    for name,uri in get_corp_agents():
        agent = Agent(name, uri)
        agents.append(agent)
    # print(agents)
    return agents


def read_csv(path):
    rows = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for x in reader:
            rows.append(x)
    return rows


def update_accession(accession, agent):
    # print(aspace_url+accession)

    updateAcc = requests.get(aspace_url+accession,headers=headers).json()
    # print(updateAcc)
    addAgentURL = JsonPatch([{"op": "replace", "path":"/linked_agents", "value":[{"ref":agent.uri,"role":"source","relator":"dnr"}]}])
    # print(addAgentURL)
    applyPatch = addAgentURL.apply(updateAcc,in_place=True)
    
    # print(applyPatch)
    newAcc = requests.post(aspace_url+accession,data=json.dumps(applyPatch),headers=headers).json()
    # print(newAcc)

def main():
    path = sys.argv[1]
    agents = get_agents_from_api()

    #get accession ids
    accs = requests.get(aspace_url+"/repositories/2/accessions?all_ids=true",headers=headers).json()
    # Map accession numbers to accession URIs
    # You will need to reference this mapping later in your posts, or else you
    # will add a bunch of wrong identifiers
    # print(accs)
    accIDs=[x for x in accs]
    acc_mapping = {}
    for key in accIDs:
        accData=requests.get(aspace_url+"/repositories/2/accessions/"+str(key),headers=headers).json()
        id_0=accData['id_0']
        uri=accData['uri']
        acc_mapping[id_0]=uri
        # print(acc_mapping)

    csv_data = read_csv(path)
    for x in csv_data:
        
        if len(x['Donor_last_name/Organization']) > 0:
            agent = [y for y in agents if y.name == x['Donor_last_name']+', '+x['Donor_first_name']][0]
            agent.linked_accessions.append(x['Accession_Number'])
        if len(x['Donor-corporate']) > 0:
            agent = [y for y in agents if y.name == x['Donor-corporate']][0]
            agent.linked_accessions.append(x['Accession_Number'])

    for agent in agents:
        for linked_accession in agent.linked_accessions:
            update_accession(acc_mapping[linked_accession], agent)

if __name__ == '__main__':
    main()
