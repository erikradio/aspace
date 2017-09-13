<?xml version="1.0" encoding="UTF-8"?>
<!-- This stylesheet transforms EAD records from ArchivesSpace into AAO specifications.
Created by Erik Radio, UA Libraries, 2017-09-13-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0"
    xmlns:ead="urn:isbn:1-931666-22-9">
    <xsl:output method="xml" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/" exclude-result-prefixes="#all">




        <ead relatedencoding="MARC21">
            <eadheader langencoding="iso639-2b" findaidstatus="edited-full-draft"
                audience="internal">
                <eadid>
                    <xsl:value-of select="//ead:titlestmt/ead:titleproper/ead:num"/>
                </eadid>
                <filedesc>
                    <titlestmt>

                        <titleproper encodinganalog="title">
                            <xsl:value-of select="//ead:titleproper/text()"/>

                            <date normal="{//ead:archdesc/ead:did/ead:unitdate/@normal}" era="ce"
                                calendar="gregorian" certainty="approximate" type="inclusive">
                                <xsl:value-of select="//ead:archdesc/ead:did/ead:unitdate[1]"/>
                            </date>
                            <date normal="{//ead:archdesc/ead:did/ead:unitdate/@normal}" type="bulk"
                                >(bulk <xsl:value-of select="//ead:archdesc/ead:did/ead:unitdate[1]"
                                />)</date>
                        </titleproper>
                        <titleproper type="filing" altrender="nodisplay">
                            <xsl:value-of select="//ead:titleproper/text()"/>
                        </titleproper>
                        <author>
                            <xsl:value-of select="//ead:titlestmt/ead:author"/>
                        </author>
                    </titlestmt>
                    <publicationstmt>
                        <publisher>University of Arizona Libraries, Special Collections</publisher>
                        <address>
                            <addressline>PO Box 210055</addressline>
                            <addressline>Tucson, AZ 85721-0055</addressline>
                            <addressline>Phone: 520-621-6423</addressline>
                            <addressline>Fax: 520-621-9733</addressline>
                            <addressline>URL:http://speccoll.library.arizona.edu/</addressline>
                            <addressline>E-Mail: LBRY-askspcoll@email.arizona.edu</addressline>
                        </address>
                        <date normal="{year-from-date(current-date())}" era="ce"
                            calendar="gregorian">
                            <xsl:value-of select="year-from-date(current-date())"/>
                        </date>
                        <p>Arizona Board of Regents. All Rights Reserved.</p>
                    </publicationstmt>


                </filedesc>
                <profiledesc>
                    <creation>
                        <xsl:value-of select="//ead:profiledesc/ead:creation"/>
                    </creation>
                </profiledesc>
                <revisiondesc>
                    <change>
                        <date>
                            <xsl:value-of select="//ead:revisiondesc/ead:change/ead:date"/>
                        </date>
                        <item>
                            <xsl:value-of select="//ead:revisiondesc/ead:change/ead:item"/>
                        </item>
                    </change>

                </revisiondesc>
            </eadheader>
            <archdesc level="collection" type="inventory" relatedencoding="351$c">
                <did>
                    <head>Collection Summary</head>
                    <unittitle encodinganalog="245" label="Collection Name">
                        <xsl:value-of select="//ead:archdesc/ead:did/ead:unittitle"/>
                        <unitdate type="inclusive" label="Dates"
                            normal="{//ead:archdesc/ead:did/ead:unitdate/@normal}">
                            <xsl:value-of select="//ead:archdesc/ead:did/ead:unitdate[1]"/>
                        </unitdate>
                        <unitdate type="bulk" label="Dates"
                            normal="{//ead:archdesc/ead:did/ead:unitdate/@normal}">(bulk
                                <xsl:value-of select="//ead:archdesc/ead:did/ead:unitdate[2]"
                            />)</unitdate>
                    </unittitle>
                    <unitid label="Collection Number" encodinganalog="099" repositorycode="US-AzU"
                        countrycode="US">
                        <xsl:value-of select="//ead:archdesc/ead:did/ead:unitid"/>
                    </unitid>
                    <origination label="Creator">
                        <persname source="lcnaf" encodinganalog="100">
                            <xsl:value-of select="//ead:did/ead:origination/ead:persname"/>
                        </persname>
                    </origination>
                    <abstract label="Abstract">
                        <xsl:value-of select="//ead:did/ead:abstract"/>
                    </abstract>
                    <physdesc encodinganalog="300$a" label="Physical Description">
                        <extent>
                            <xsl:value-of select="//ead:did/ead:physdesc/ead:extent"/>
                        </extent>
                    </physdesc>
                    <repository label="Repository">
                        <corpname>University of Arizona Libraries, Special Collections</corpname>
                        <address>
                            <addressline>University of Arizona</addressline>
                            <addressline>PO Box 210055</addressline>
                            <addressline>Tucson, AZ 85721-0055</addressline>
                            <addressline>Phone: 520-621-6423</addressline>
                            <addressline>Fax: 520-621-9733</addressline>
                            <addressline>URL: http://speccoll.library.arizona.edu/</addressline>
                            <addressline>E-Mail: LBRY-askspcoll@email.arizona.edu</addressline>
                        </address>
                    </repository>
                    <langmaterial>Materials are in <language encodinganalog="546" langcode="eng"
                            scriptcode="Latn"><xsl:value-of select="//ead:profiledesc/ead:langusage"
                            /></language></langmaterial>
                </did>
                    <accessrestrict>
                        <head>Restrictions</head>
                        <p>
                            <xsl:value-of select="//ead:accessrestrict/ead:p"/>
                        </p>
                    </accessrestrict>
                    <userestrict>
                        <head>Copyright</head>
                        <p>It is the responsibility of the user to obtain permission to publish from
                            the owner of the copyright (the institution, the creator of the record,
                            the author or his/her transferees, heirs, legates, or literary
                            executors). The user agrees to indemnify and hold harmless the Arizona
                            Board of Regents for the University of Arizona, its officers, employees,
                            and agents from and against all claims made by any person asserting that
                            he or she is an owner of copyright. </p>
                    </userestrict>
                    <prefercite>
                        <head>Credit Line</head>
                        <p>
                            <xsl:value-of select="//ead:prefercite//ead:p"/>
                        </p>
                    </prefercite>
                    <processinfo>
                        <head>Processing History</head>
                        <p>Processed by University of Arizona Special Collections staff</p>
                    </processinfo>
                    <bioghist encodinganalog="545">
                        <head>Biographical Note</head>
                        <p>
                            <xsl:value-of select="//ead:bioghist/ead:p"/>
                        </p>
                    </bioghist>
                    <!--<arrangement encodinganalog="351$a"> 
                                <head>Arrangement</head>
                                <p> <xsl:value-of select="//ead:archdesc/ead:arrangement/ead:p"/></p>
                                <list type="ordered">
                                <xsl:copy-of select="//ead:arrangement/ead:list/*" copy-namespaces="no"/>
                                </list>
                            </arrangement>-->

                    <xsl:copy-of select="//ead:arrangement" copy-namespaces="no" exclude-result-prefixes="#all"/>
                    <scopecontent encodinganalog="520">
                        <head>Scope and Content Note</head>
                        <p>
                            <xsl:value-of select="//ead:scopecontent//ead:p"
                                exclude-result-prefixes="#all"/>
                        </p>
                    </scopecontent>

                    <xsl:copy-of select="//ead:controlaccess" copy-namespaces="no" exclude-result-prefixes="#all"/>
                    <dsc type="combined">
                        <xsl:copy-of select="//ead:dsc/*" copy-namespaces="no" exclude-result-prefixes="#all"/>
                    </dsc>
                    

                
            </archdesc>
        </ead>




        <!--
                
                <field xmlns="http://www.lunaimaging.com/xsd" type="Record ID">
                    
                    <xsl:value-of select="mods:recordInfo/mods:recordIdentifier"/>
                    
                </field>
                
                
                <fieldGroup type="titleInfo">
                    <field xmlns="http://www.lunaimaging.com/xsd" type="Title">
                        <xsl:for-each select="mods:titleInfo[1]">
                            
                            <xsl:choose>
                                <xsl:when test="count($nonsort)>0">
                                    <xsl:value-of select="concat($nonsort,$title )"/>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:value-of select="$title"/>
                                </xsl:otherwise>
                            </xsl:choose>
                        </xsl:for-each>
                    </field>
                    <xsl:if test="count($subtitle)>0">
                        <field xmlns="http://www.lunaimaging.com/xsd" type="subTitle">
                            <xsl:value-of select="$subtitle"/>
                        </field>
                    </xsl:if>
                </fieldGroup>
                
                
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="name">
                    <xsl:for-each select="mods:name">
                        
                        
                        
                        <field type="Creator">
                            
                            <xsl:value-of select="mods:namePart"/>
                            
                            
                        </field>
                    </xsl:for-each>
                </fieldGroup>
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="Abstract_Description">
                    <field type="Abstract">
                        <xsl:value-of select="mods:abstract"/>
                    </field>
                </fieldGroup>
                
                
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="Language">
                    
                    <field type="Language">
                        <xsl:choose>
                            <xsl:when test="mods:language/mods:languageTerm[@type='code']='spa'">
                                <xsl:value-of select="$spa"/>
                            </xsl:when>
                            <xsl:when test="mods:language/mods:languageTerm[@type='code']='eng'">
                                <xsl:value-of select="$eng"/>
                            </xsl:when>
                            <xsl:when test="mods:language/mods:languageTerm[@type='code']='ger'">
                                <xsl:value-of select="$ger"/>
                            </xsl:when>
                            <xsl:when test="mods:language/mods:languageTerm[@type='code']='fre'">
                                <xsl:value-of select="$fre"/>
                            </xsl:when>
                            <xsl:when test="mods:language/mods:languageTerm[@type='code']='ita'">
                                <xsl:value-of select="$ita"/>
                            </xsl:when>
                        </xsl:choose>
                        
                    </field>
                </fieldGroup>
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="Genre">
                    <field type="Genre">
                        <xsl:value-of select="mods:genre"/>
                    </field>
                </fieldGroup>
                
                
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="originInfo">
                    <field type="Date Issued">
                        <xsl:value-of select="mods:originInfo/mods:dateIssued[@encoding='marc']"/>
                    </field>
                    <field type="Place">
                        <xsl:choose>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='nq'">
                                <xsl:value-of select="$nq"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='gt'">
                                <xsl:value-of select="$gt"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='ho'">
                                <xsl:value-of select="$ho"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='es'">
                                <xsl:value-of select="$es"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='cr'">
                                <xsl:value-of select="$cr"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='py'">
                                <xsl:value-of select="$py"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='fr'">
                                <xsl:value-of select="$fr"/>
                            </xsl:when>
                            <xsl:when test="mods:originInfo/mods:place/mods:placeTerm[@type='code']='mx'">
                                <xsl:value-of select="$mx"/>
                            </xsl:when>
                        </xsl:choose>
                    </field>
                    <field type="Publisher"><xsl:value-of select="mods:originInfo/mods:publisher"/></field>
                    <field type="Issuance"><xsl:value-of select="mods:originInfo/mods:issuance"/></field>
                    
                    
                </fieldGroup>
                
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="Physical_Description">
                    <field type="Extent">
                        <xsl:value-of select="mods:physicalDescription/mods:extent"/>
                    </field>
                    <field type="Form">
                        <xsl:value-of select="mods:physicalDescription/mods:form"/>
                    </field>
                </fieldGroup>
                
                <fieldGroup xmlns="http://www.lunaimaging.com/xsd" type="Misc_Note">
                    <field type="Note">
                        <xsl:value-of select="mods:note"/>
                    </field>
                </fieldGroup>
                
                -->




    </xsl:template>






</xsl:stylesheet>
