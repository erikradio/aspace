import sys
import xml.etree.ElementTree as ET
import copy


def removeColons(root):
    for el in root.iter('*'):
        fack=el.attrib
        for x in fack:
            attrText = fack[x]
            if attrText.endswith(":"):
                fack[x] = attrText.replace(':','')
                # print(fack[x])

    return root

def updateHeader(root):
    header=root.find('eadheader')
    header.set('findaidstatus','complete')
    
    return root






def main():
    infile_path = sys.argv[1]
    outfile_path = 'rev_'+sys.argv[1]

    tree=ET.parse(infile_path)
    root=tree.getroot()

    updateHeader(root)

    removeColons(root)

    # print(tree)
    tree.write(outfile_path)

# make this a safe-ish cli script
if __name__ == '__main__':
    # print(tree)

    main()
