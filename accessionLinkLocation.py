import requests, json,csv,uuid,re,sys
from json import dumps
from jsonpatch import JsonPatch
from re import match

#this script links locations to accession records

aspace_url = "http://localhost:8089"
username= "admin"
password = "admin"
auth = requests.post(aspace_url+"/users/"+username+"/login?password="+password).json()
session = auth["session"]
headers = {"X-ArchivesSpace-Session":session}


class Location:
    def __init__(self, coordinates, uri):
        self.coordinates = coordinates
        self.uri = uri
        self.linked_accessions = []

    def __repr__(self):
        return dumps(
            {'coordinates': self.coordinates, 'uri':self.uri,
             'linked_accessions': self.linked_accessions},
            indent=4
        )


def get_locations_from_api():

    def get_locations():
        locations=requests.get(aspace_url+"/locations?all_ids=true").json()
        locList=[x for x in locations]
        for location in locList:
            locData=requests.get(aspace_url+"/locations/"+str(location),headers=headers).json()
            cord1=locData['coordinate_1_indicator']
            cord2=locData['coordinate_2_indicator']
            coordinates=cord1+','+cord2
            uri=locData['uri']
            yield coordinates,uri




    locations = []
    for coordinates,uri in get_locations():
        location = Location(coordinates, uri)
        locations.append(location)


    # print(agents)
    return locations


def read_csv(path):
    rows = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for x in reader:
            rows.append(x)
    return rows


def update_accession(accession, location):
    # print(aspace_url+accession)

    updateAcc = requests.get(aspace_url+accession,headers=headers).json()
    # print(updateAcc)
    addLocURL = JsonPatch([{"op": "replace", "path":"/instances", "value":[{"container":
    [{"type_1":"box","indicator_1":"1","container_locations":
    [{"ref":location.uri,"jsonmodel_type":"container_location","status":"current"}]}]}]}])
    # print(addAgentURL)
    applyPatch = addLocURL.apply(updateAcc,in_place=True)

    # print(applyPatch)
    newAcc = requests.post(aspace_url+accession,data=json.dumps(applyPatch),headers=headers).json()
    print(newAcc)

def main():
    path = sys.argv[1]
    locations = get_locations_from_api()

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

        if len(x['Location']) > 0:


            potential_loc_list = [y for y in locations if y.coordinates == x['Location']+','+x['Tier']]
            # print(potential_agent_list)
            if len(potential_loc_list) != 1:
                if len(potential_loc_list) > 1:
                    raise ValueError("We found too many locations. Offending search term: {}, {}".format(x['Location'], x['Tier']))
                if len(potential_agent_list) < 1:
                    raise ValueError("We found too few locations. Offending search term: {}, {}".format(x['Location'], x['Tier']))
            else:
                location = potential_loc_list[0]
            location.linked_accessions.append(x['Accession_Number'])


    for location in locations:
        for linked_accession in agent.linked_accessions:
            update_accession(acc_mapping[linked_accession], location)

if __name__ == '__main__':
    main()
