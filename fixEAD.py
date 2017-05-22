import sys
import xml.etree.ElementTree as ET
import copy


def removeColons():
    for el in root.iter('*'):
        fack=el.attrib
        for x in fack:
            attrText = fack.get(x)
            if ':' in attrText:
                m=attrText.strip(':')
                print(m)

def updateValues():
    header=root.find('eadheader')
    header.set('findaidstatus','complete')

def getRecord():
    with open(infile_path, mode='rU') as infile:
        tree=ET.parse(infile_path)
        root=tree.getroot()
    

def main(tree):
    infile_path = sys.argv[1]
    outfile_path = 'rev_'+sys.argv[1]

    tree=ET.parse(infile_path)
    tree.write(outfile_path)

# make this a safe-ish cli script
if __name__ == '__main__':

    main()
