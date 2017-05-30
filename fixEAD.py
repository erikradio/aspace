# -*- coding: utf-8 -*-
import sys, re, uuid
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import copy
from datetime import datetime



def removeColons(root):
    for el in root.iter('*'):
        fack=el.attrib
        for x in fack:
            attrText = fack[x]
            if attrText.endswith(":"):
                fack[x] = attrText.replace(':','')
                # print(fack[x])

    return root

def updateValues(root):
    infile_path = sys.argv[1]

    time = datetime.now().strftime('%Y-%m-%d')
    #fix eadheader
    header=root.find('eadheader')
    header.set('findaidstatus','complete')
    revision=SubElement(header, 'revisiondesc')
    change=SubElement(revision,'change')
    revDate=SubElement(change,'date')
    revDate.set('normal', time)
    revDate.text = time
    item = SubElement(change, 'item')
    item.text = 'This finding aid was updated to be more closely aligned with LC specifications using a python script created by Erik Radio.'

    #fix EADid
    EADid = header.find('eadid')
    EADid.text=infile_path.strip('.xml')





    #date

    pubDate = header.find('filedesc/publicationstmt/date')
    pubDate.text = pubDate.text.replace(u"© ","")

    #control access to remove list
    conAcc = root.find('archdesc/controlaccess')
    subj=[]
    for thing in conAcc.findall('list/item/*'):
        subj.append(thing)
        for head in conAcc.findall('head'):
            # print(head.tag)
            conAcc.remove(head)
        for y in conAcc.findall('list'):
            conAcc.remove(y)

    for x in subj:

        newsubj = SubElement(conAcc,x.tag)
        newsubj.text=x.text

    return root


def updateAttributes(root):
    header=root.find('eadheader')

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
    # print(archDesc)
    archDesc.attrib.pop('relatedencoding', None)
    archDesc.set('encodinganalog','351$c')

    #langmaterial
    langusage = header.find('profiledesc/langusage/language')
    langusage.set('langcode','eng')


    langusage2 = root.find('archdesc/did/langmaterial/language')
    # print(langusage2)
    if langusage2 is not None:
        langusage2.attrib.pop('scriptcode', None)

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

    #add random ids to containers -- START HERE
    dsc = root.find('.//dsc')

    for c01 in dsc.iter('c01'):
        randomID=uuid.uuid4()
        # print(randomID)
        c01.set('id',randomID)

        # print(c01.attrib)



    return root



def main():
    infile_path = sys.argv[1]
    outfile_path = 'rev_'+sys.argv[1]



    tree=ET.parse(infile_path)
    root=tree.getroot()
    updateValues(root)
    removeColons(root)
    updateAttributes(root)


    # print(tree)
    tree.write(outfile_path)

# make this a safe-ish cli script
if __name__ == '__main__':
    # print(tree)

    main()
