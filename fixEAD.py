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

def updateAttributes(root):

    repoCode=root.find('archdesc/did/unitid')
    repoCode.set('repositorycode','US-azu')
    repoCode.set('countrycody','us')
    # print(repoCode.attrib)

    for repoDate in root.iter('unitdate'):
        date=repoDate.attrib
        if date == '':
            date.attrib.pop('normal', None)
        if date == 'NaN':
            date.attrib.pop('normal', None)
        if date == 'AzU':
            date.attrib.pop('normal', None)
        # print(date)
    # print(repoDate)

    archDesc=root.find('archdesc')
    archDesc.attrib.pop('relatedencoding', None)
    archDesc.set('encodinganalog','351$c')

    #remove all id attrib

    for x in root.iter('*'):
        name=x.get('id')
        if name is not None:
            x.attrib.pop('id', None)
            








    for el in root.iter('*'):
        fack=el.attrib
        for x in fack:
            attrText = fack[x]
            if attrText == '5441':
                fack[x] = attrText.replace('5441','544')
            if attrText == '544$1':
                fack[x] = attrText.replace('544$1','544')


    return root





def main():
    infile_path = sys.argv[1]
    outfile_path = 'rev_'+sys.argv[1]

    tree=ET.parse(infile_path)
    root=tree.getroot()

    updateHeader(root)

    removeColons(root)
    updateAttributes(root)

    # print(tree)
    tree.write(outfile_path)

# make this a safe-ish cli script
if __name__ == '__main__':
    # print(tree)

    main()
