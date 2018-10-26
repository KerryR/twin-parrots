# coding: utf-8

import shapefile
import csv
import math
import copy
import sys
import csv
import string
import time
import re
import AdjacentLocalities
import QldElectorate
import urllib2

def today():
    return time.strftime("%d %B %Y").lstrip("0")

def findQueenslandPlaces (name):
    name1=re.sub(r' ', r'-', name)
    print "Subbing", name1
    url="http://queenslandplaces.com.au/"+string.lower(name1)
    try:
        ctx = urllib2.urlopen(url)
        if ctx == None:
            print "urlopen failed,returned None"
            return ""
        c = ctx.getcode()
        if c != 200:
            print "Code", ctx.getcode ()
            return ""
        return url
    except (urllib2.URLError):
        print "URL Error"
        return ""

# how the LGAs are referred to in the Queensland Place Names

def lgaQPN (s):
    if s == "Barcaldine Regional":
        return "Barcaldine Region"
    if s == "Blackall Tambo Regional":
        return "Blackall-Tambo Region"   
    if s == "Bundaberg Regional":
        return "Bundaberg Region"
    if s == "Cairns Regional":
        return "Cairns Region"
    if s == "Cassowary Coast Regional":
        return "Cassowary Coast Region"
    if s == "Central Highlands Regional":
        return "Central Highlands Region"
    if s == "Charters Towers Regional":
        return "Charters Towers Region"
    if s == "Fraser Coast Regional":
        return "Fraser Coast Region"
    if s == "Gladstone Regional":
        return "Gladstone Region"
    if s == "Goondiwindi Regional":
        return "Goondiwindi Region"
    if s == "Gympie Regional":
        return "Gympie Region"
    if s == "Isaac Regional":
        return "Isaac Region"
    if s == "Lockyer Valley Regional":
        return "Lockyer Valley Region"
    if s == "Longreach Regional":
        return "Longreach Region"
    if s == "Mackay Regional":
        return "Mackay Region"
    if s == "Maranoa Regional":
        return "Maranoa Region"
    if s == "Moreton Bay Regional":
        return "Moreton Bay Region"
    if s == "Napranum Aboriginal Shire":
        return "Aboriginal Shire of Napranum"
    if s == "North Burnett Regional":
        return "North Burnett Region"
    if s == "Northern Peninsula Area Regional":
        return "Northern Peninsula Area Region"
    if s == "Rockhampton Regional":
        return "Rockhampton Region"
    if s == "Scenic Rim Regional":
        return "Scenic Rim Region"
    if s == "Somerset Regional":
        return "Somerset Region"
    if s == "South Burnett Regional":
        return "South Burnett Region"
    if s == "Southern Downs Regional":
        return "Southern Downs Region"
    if s == "Sunshine Coast Regional":
        return "Sunshine Coast Region"
    if s == "Tablelands Regional":
        return "Tablelands Region"
    if s == "Toowoomba Regional":
        return "Toowoomba Region"
    if s == "Torres Strait Island Regional":
        return "Torres Strait Island Region"
    if s == "Western Downs Regional":
        return "Western Downs Region"
    if s == "Whitsunday Regional":
        return "Whitsunday Region"
    return s

# how the LGAs are referred to in the Qld Govt shapefile

def lgaQShape (s):
    if s == "Barcaldine Regional":
        return "Barcaldine Region"
    if s == "Blackall Tambo Regional":
        return "Blackall Tambo Region"   
    if s == "Bundaberg Regional":
        return "Bundaberg Region"
    if s == "Cairns Regional":
        return "Cairns Region"
    if s == "Cassowary Coast Regional":
        return "Cassowary Coast Region"
    if s == "Central Highlands Regional":
        return "Central Highlands Region"
    if s == "Charters Towers Regional":
        return "Charters Towers Region"
    if s == "Fraser Coast Regional":
        return "Fraser Coast Region"
    if s == "Gladstone Regional":
        return "Gladstone Region"
    if s == "Goondiwindi Regional":
        return "Goondiwindi Region"
    if s == "Gympie Regional":
        return "Gympie Region"
    if s == "Isaac Regional":
        return "Isaac Region"
    if s == "Lockyer Valley Regional":
        return "Lockyer Valley Region"
    if s == "Longreach Regional":
        return "Longreach Region"
    if s == "Mackay Regional":
        return "Mackay Region"
    if s == "Maranoa Regional":
        return "Maranoa Region"
    if s == "Moreton Bay Regional":
        return "Moreton Bay Region"
    if s == "Napranum Aboriginal Shire":
        return "Aboriginal Shire of Napranum"
    if s == "North Burnett Regional":
        return "North Burnett Region"
    if s == "Northern Peninsula Area Regional":
        return "Northern Peninsula Area Region"
    if s == "Rockhampton Regional":
        return "Rockhampton Region"
    if s == "Scenic Rim Regional":
        return "Scenic Rim Region"
    if s == "Somerset Regional":
        return "Somerset Region"
    if s == "South Burnett Regional":
        return "South Burnett Region"
    if s == "Southern Downs Regional":
        return "Southern Downs Region"
    if s == "Sunshine Coast Regional":
        return "Sunshine Coast Region"
    if s == "Tablelands Regional":
        return "Tablelands Region"
    if s == "Toowoomba Regional":
        return "Toowoomba Region"
    if s == "Torres Strait Island Regional":
        return "Torres Strait Island Region"
    if s == "Western Downs Regional":
        return "Western Downs Region"
    if s == "Whitsunday Regional":
        return "Whitsunday Region"
    return s

def lgaLede (s):
    if s == "Balonne Shire":
        return "Shire of Balonne"
    if s == "Banana Shire":
        return "Shire of Banana"
    if s == "Barcoo Shire":
        return "Shire of Barcoo"
    if s == "Boulia Shire":
        return "Shire of Boulia"
    if s == "Brisbane City":
        return "City of Brisbane"
    if s == "Bulloo Shire":
        return "Shire of Bulloo"
    if s == "Burdekin Shire":
        return "Shire of Burdekin"
    if s == "Burke Shire":
        return "Shire of Burke"
    if s == "Carpentaria Shire":
        return "Shire of Carpentaria"
    if s == "Cherbourg Aboriginal Shire":
        return "Aboriginal Shire of Cherbourg"    
    if s == "Cloncurry Shire":
        return "Shire of Cloncurry"
    if s == "Cook Shire":
        return "Shire of Cook"
    if s == "Croydon Shire":
        return "Shire of Croydon"
    if s == "Diamantina Shire":
        return "Shire of Diamantina"
    if s == "Douglas Shire":
        return "Shire of Douglas"
    if s == "Etheridge Shire":
        return "Shire of Etheridge"
    if s == "Gold Coast City":
        return "City of Gold Coast"
    if s == "Hinchinbrook Shire":
        return "Shire of Hinchinbrook"
    if s == "Hope Vale Aboriginal Shire":
        return "Aboriginal Shire of Hope Vale"
    if s == "Ipswich City":
        return "City of Ipswich"
    if s == "Logan City":
        return "City of Logan"
    if s == "Mareeba Shire":
        return "Shire of Mareeba"
    if s == "Mckinlay Shire":
        return "Shire of Mckinlay"
    if s == "Mount Isa City":
        return "City of Mount Isa"
    if s == "Murweh Shire":
        return "Shire of Murweh"
    if s == "Napranum Aboriginal Shire":
        return "Aboriginal Shire of Napranum"
    if s == "Noosa Shire":
        return "Shire of Noosa"
    if s == "Paroo Shire":
        return "Shire of Paroo"
    if s == "Quilpie Shire":
        return "Shire of Quilpie"
    if s == "Redland City":
        return "City of Redland"
    if s == "Richmond Shire":
        return "Shire of Richmond"
    if s == "Torres Shire":
        return "Shire of Torres"
    if s == "Townsville City":
        return "City of Townsville"
    if s == "Winton Shire":
        return "Shire of Winton"
    if s == "Woorabinda Aboriginal Shire":
        return "Aboriginal Shire of Woorabinda"
    return s

def lgaTemplate (s):
    if s == "Balonne Shire":
        return "Shire of Balonne"
    if s == "Banana Shire":
        return "Shire of Banana"
    if s == "Barcoo Shire":
        return "Shire of Barcoo"
    if s == "Boulia Shire":
        return "Shire of Boulia"
    if s == "Brisbane City":
        return "City of Brisbane suburbs"
    if s == "Bulloo Shire":
        return "Shire of Bulloo"
    if s == "Burdekin Shire":
        return "Shire of Burdekin"
    if s == "Burke Shire":
        return "Shire of Burke"
    if s == "Carpentaria Shire":
        return "Shire of Carpentaria"
    if s == "Cherbourg Aboriginal Shire":
        return "Aboriginal Shire of Cherbourg" 
    if s == "Cook Shire":
        return "Shire of Cook"
    if s == "Croydon Shire":
        return "Shire of Croydon"
    if s == "Cloncurry Shire":
        return "Shire of Cloncurry"
    if s == "Diamantina Shire":
        return "Shire of Diamantina"
    if s == "Douglas Shire":
        return "Shire of Douglas"
    if s == "Etheridge Shire":
        return "Shire of Etheridge"
    if s == "Flinders Shire":
        return "Shire of Flinders"
    if s == "Gold Coast City":
        return "Localities in Gold Coast" # odd one out
    if s == "Hinchinbrook Shire":
        return "Shire of Hinchinbrook"
    if s == "Hope Vale Aboriginal Shire":
        return "Aboriginal Shire of Hope Vale"
    if s == "Ipswich City":
        return "Ipswich City" # odd one out
    if s == "Livingstone Shire":
        return "Shire of Livingstone"
    if s == "Logan City":
        return "Logan City" # odd one out
    if s == "Mareeba Shire":
        return "Shire of Mareeba"
    if s == "Mckinlay Shire":
        return "Shire of Mckinlay"
    if s == "Mount Isa City":
        return "City of Mount Isa"
    if s == "Murweh Shire":
        return "Shire of Murweh"
    if s == "Napranum Aboriginal Shire":
        return "Aboriginal Shire of Napranum"
    if s == "Noosa Shire":
        return "Shire of Noosa"
    if s == "Paroo Shire":
        return "Shire of Paroo"
    if s == "Quilpie Shire":
        return "Shire of Quilpie"
    if s == "Richmond Shire":
        return "Shire of Richmond"
    if s == "Torres Shire":
        return "Shire of Torres"
    if s == "Townsville City":
        return "Suburbs of Townsville"
    if s == "Winton Shire":
        return "Shire of Winton"
    if s == "Woorabinda Aboriginal Shire":
        return "Aboriginal Shire of Woorabinda"
    return s

def lgaCategory (s, isS):
    if s == "Balonne Shire":
        return "Shire of Balonne"
    if s == "Banana Shire":
        return "Shire of Banana"
    if s == "Barcoo Shire":
        return "Shire of Barcoo"
    if s == "Blackall Tambo Region":
        return "Blackall-Tambo Region"
    if s == "Boulia Shire":
        return "Shire of Boulia"
    if s == "Brisbane City":
        return "Suburbs of Brisbane" #odd
    if s == "Bulloo Shire":
        return "Shire of Bulloo"
    if s == "Burdekin Shire":
        return "Shire of Burdekin"
    if s == "Burke Shire":
        return "Shire of Burke"
    if s == "Carpentaria Shire":
        return "Shire of Carpentaria"
    if s == "Cherbourg Aboriginal Shire":
        return "Aboriginal Shire of Cherbourg" 
    if s == "Cook Shire":
        return "Shire of Cook"
    if s == "Croydon Shire":
        return "Shire of Croydon"
    if s == "Cloncurry Shire":
        return "Shire of Cloncurry"
    if s == "Diamantina Shire":
        return "Shire of Diamantina"
    if s == "Douglas Shire":
        return "Shire of Douglas"
    if s == "Etheridge Shire":
        return "Shire of Etheridge"
    if s == "Flinders Shire":
        return "Shire of Flinders"
    if s == "Gold Coast City":
        return "Suburbs of the Gold Coast, Queensland" #odd
    if s == "Hinchinbrook Shire":
        return "Shire of Hinchinbrook"
    if s == "Hope Vale Aboriginal Shire":
        return "Aboriginal Shire of Hope Vale"
    if s == "Ipswich City":
        return "Ipswich, Queensland" #odd
    if s == "Livingstone Shire":
        return "Shire of Livingstone"
    if s == "Mareeba Shire":
        return "Shire of Mareeba"
    if s == "Mckinlay Shire":
        return "Shire of Mckinlay"
    if s == "Mount Isa City":
        return "City of Mount Isa"
    if s == "Murweh Shire":
        return "Shire of Murweh"
    if s == "Napranum Aboriginal Shire":
        return "Aboriginal Shire of Napranum"
    if s == "Noosa Shire":
        return "Shire of Noosa"
    if s == "Paroo Shire":
        return "Shire of Paroo"
    if s == "Quilpie Shire":
        return "Shire of Quilpie"
    if s == "Richmond Shire":
        return "Shire of Richmond"
    if s == "Torres Shire":
        return "Shire of Torres"
    if s == "Townsville City":
        if isS:
            return "Suburbs of Townsville" #odd
        else:
            return "City of Townsville"    #odd
    if s == "Winton Shire":
        return "Shire of Winton"
    if s == "Woorabinda Aboriginal Shire":
        return "Aboriginal Shire of Woorabinda"
    return s

# if the entire LGA is within a state electorate, return it, otherwise ""
def lgaSE (s):
##    if s == "Charters Towers Region":
##        return "[[Electoral district of Dalrymple|Dalrymple]]"
##    if s == "Etheridge Shire":
##        return "[[Electoral district of Mount Isa|Mount Isa]]"
##    if s == "Goondiwindi Region":
##        return "[[Electoral district of Kennedy|Kennedy]]"
##    if s == "North Burnett Region":
##        return "[[Electoral district of Callide|Callide]]"
    return ""

# if the entire LGA is within a federal electorate, return it, otherwise ""
def lgaFE (s):
##    
##    if s == "Cassowary Coast Region":
##        return "[[Division of Kennedy|Kennedy]]"
##    if s == "Etheridge Shire":
##        return "[[Division of Kennedy|Kennedy]]"
##    if s == "Goondiwindi Region":
##        return "[[Division of Maranoa|Maranoa]]"
##    if s == "Gympie Region":
##        return "[[Division of Wide Bay|Wide Bay]]"
##    if s == "Isaac Region":
##        return "[[Division of Capricornia|Capricornia]]"
##    if s == "Shire of Livingstone":
##        return "[[Division of Capricornia|Capricornia]]"
##    if s == "North Burnett Region":
##        return "[[Division of Flynn|Flynn]]"
    return ""
    
def isSettlement (t):
    if t == "LOCB":
        return True
    if t == "POPL":
        return True
    if t == "SUB":
        return True
    return False

def hasHistory (row):
    if row ["COMMENTS"] != "" or row  ["ORIGIN"] != "" or row ["HISTORY"] != "":
            return True
    return False

# try to work out what can be usefully done with the Links field
def extLink (row):
    if row ["LINKS"] == "":
        return ""
    match = re.match("Town map: https://geospatial.information.qld.gov.au/arcgisoutput/cadscans/(.*)(\d\d\d\d).jpg$", row ["LINKS"])
    if match:
        return "* [https://gisservices.information.qld.gov.au/arcgis/rest/directories/historicalscans/cad_scans/" \
               + match.group(1) + match.group(2) + ".jpg Town map of " \
               + row ["PLACE_NAME"] + ", " + match.group(2) + "]\n"  
    return "* " + row ["LINKS"] + "\n"

def dec4 (s):
    match = re.match("([0-9-]+).(\d+)", s)
    if match:
        s2 = match.group(1)+"."+match.group(2)[0:4]
        #print s2
        return s2


def emit (tRow, lRow, isT, isS, isL):
    print "in emit"
    if isT:
        print "is town", tRow ["PLACE_NAME"]
    if isS:
        print "is suburb", lRow ["PLACE_NAME"]
    if isL:
        print "is locality", lRow ["PLACE_NAME"]
    if isT:
        wikiFile = open("wiki/" + tRow ["PLACE_NAME"] + "-" +tRow ["LGA_NAME"] +".wik", "wb")
    else:
        wikiFile = open("wiki/" + lRow ["PLACE_NAME"] + "-" +lRow ["LGA_NAME"] +".wik", "wb")   

    s=""

    s = s +"{{Use DMY dates}}\n"
    s = s +"{{Use Australian English}}\n"
    s = s +"{{Infobox Australian place\n"
    if isT:
        s = s +"| type                = town\n"
        print tRow ["PLACE_NAME"]
    else:
        s = s +"| type                = suburb\n"
        print lRow ["PLACE_NAME"]
    if isT:  
        s = s +"| name                = " + lgaLede (tRow ["PLACE_NAME"]) + "\n"
    else:
        s = s +"| name                = " + lgaLede (lRow ["PLACE_NAME"]) + "\n"
    s = s +"| city                = \n"
    s = s +"| state               = qld\n"
    s = s +"| image               = \n"
    s = s +"| caption             = \n"
    if isT:
        s = s +"| coordinates         = {{coord|" +dec4(tRow ["LATITUDE_D"]) +"|" + dec4(tRow ["LONGITUDE_"]) \
            + "|type:city_region:AU-QLD|display=inline,title}}\n"
    else:
        s = s +"| coordinates         = {{coord|" +dec4(lRow ["LATITUDE_D"]) +"|" + dec4(lRow ["LONGITUDE_"]) \
            + "|type:city_region:AU-QLD|display=inline,title}}\n"
    s = s +"| pop                 = \n" 
    s = s +"| pop_year            = {{CensusAU|2016}}\n"
    s = s +"| pop_footnotes       = <ref name=Census2016/>\n"
    s = s +"| established         = \n"
    if isT:
        s = s + "| postcode            = " + QldElectorate.findPostCode(tRow["PLACE_NAME"],lgaQShape(tRow["LGA_NAME"])) +"\n"
    else:
        s = s + "| postcode            = " + QldElectorate.findPostCode(lRow["PLACE_NAME"],lgaQShape(lRow["LGA_NAME"])) +"\n"

    if (isS or isL):
        aln = string.upper(lRow["PLACE_NAME"]+", "+lgaQShape(lRow["LGA_NAME"]))
        a = AdjacentLocalities.calcArea(aln)
        print "Area", a
        if (a > 0.0):
            s = s +"| area                = "+str(round(a,1))+"\n"
        else:
            s = s +"| area                = \n"
    s = s +"| dist1               = \n"
    s = s +"| dir1                = \n"
    s = s +"| location1           = \n"
    s = s +"| dist2               = \n"
    s = s +"| dir2                = \n"
    s = s +"| location2           = \n"
    s = s +"| dist3               = \n"
    s = s +"| dir3                = \n"
    s = s +"| location3           = \n"
    s = s +"| dist4               = \n"
    s = s +"| dir4                = \n"
    s = s +"| location4           =\n"
    if isT:
        s = s + "| lga                 = " + lgaLede (tRow ["LGA_NAME"]) +"\n"
    else:
        s = s + "| lga                 = " + lgaLede (lRow ["LGA_NAME"]) +"\n"

    # State Electorate
    # if the place is a suburb/locality, work out the electorates based on boundaries

    if isS or isL:

        se=lgaSE (lRow ["LGA_NAME"])
        if se != "":
            s = s + "| stategov            = " + se + "\n"
        else:
            ln = string.upper(lRow["PLACE_NAME"]+", "+lgaQShape(lRow["LGA_NAME"]))
            seList=QldElectorate.findElectorate("qld", ln)
            if seList == []:
                print "Warning", ln, "is not in any Queensland electorates!"
            else :
                print "first electorate", seList [0][0]
                en = string.capwords(seList[0][0])
                s = s + "| stategov            = [[Electoral district of " + en + "|"+ en + "]]\n"
                for i in range(1,len(seList)):
                    print "more than 1 electorate"
                    en = string.capwords(seList[i][0])
                    
                    s = s + "| stategov" + str(i+1)+ "           = [[Electoral district of " + en + "|" + en + "]]\n"
    elif isT:
        s = s + "| stategov            = " + lgaSE (tRow ["LGA_NAME"]) + "\n" 
             
    if isS or isL:
        se=lgaSE (lRow ["LGA_NAME"])
        if se != "":
            s = s + "| fedgov              = " + se + "\n"
        else:
            ln = string.upper(lRow["PLACE_NAME"]+", "+lgaQShape(lRow["LGA_NAME"]))
            seList=QldElectorate.findElectorate("ozqld", ln)
            if seList == []:
                print "Warning", ln, "is not in any Federal electorates!"
            else :
                en = string.capwords(seList[0][0])
                s = s + "| fedgov              = [[Division of " + en + "|"+ en + "]]\n"
                for i in range(1,len(seList)):
                    print "more than 1 electorate"
                    en = string.capwords(seList[i][0])
                    
                    s = s + "| fedgov" + str(i+1)+ "            = [[Division of " + en + "|" + en + "]]\n"

    else:
        s = s + "| fedgov              = " + lgaFE (tRow ["LGA_NAME"]) + "\n"
    if isT:
        s = s + "| maxtemp     = \n"
        s = s + "| mintemp     = \n"
        s = s + "| rainfall    = \n"

    if isS or isL:
        aln = string.upper(lRow["PLACE_NAME"]+", "+lgaQShape(lRow["LGA_NAME"]))
        print aln
        al = AdjacentLocalities.adjacentLocalities(aln)
        s = s + al
        s = s + "}}\n"


    if isT and not isS and not isL: # just a town
        s = s + "'''" + tRow ["PLACE_NAME"] + "'''"
        if tRow ["ALT_NAME"] != "":
            s = s + "(also known as " + tRow ["ALT_NAME"] + ")"
        s = s + " is a town in the [[" \
            + lgaLede (tRow ["LGA_NAME"]) + "]], [[Queensland]], Australia."
    elif isT and isS and not isL:
        s = s + "'''" + tRow ["PLACE_NAME"] + "'''"
        if tRow ["ALT_NAME"] != "":
            s = s + "(also known as " + tRow ["ALT_NAME"] + ")"
        s = s + " is a town and a suburb in the [[" \
            + lgaLede (tRow ["LGA_NAME"]) + "]], [[Queensland]], Australia."
    elif isT and not isS and isL:
        s = s + "'''" + tRow ["PLACE_NAME"] + "'''"
        if tRow ["ALT_NAME"] != "":
            s = s + "(also known as " + tRow ["ALT_NAME"] + ")"
        s = s + " is a town and a [[Suburbs and localities (Australia)|locality]] in the [[" \
            + lgaLede (tRow ["LGA_NAME"]) + "]], [[Queensland]], Australia."
    elif isT and isL and isS:
        print "Found a town and a suburb and a locality all with same name!"
        System.exit (1)
    elif not isT and isS and not isL:
        s = s + "'''" + lRow ["PLACE_NAME"] + "'''"
        if lRow ["ALT_NAME"] != "":
            s = s + "(also known as " + lRow ["ALT_NAME"] + ")"
        s = s + " is a suburb in the [[" \
            + lgaLede (lRow ["LGA_NAME"]) + "]], [[Queensland]], Australia."
    elif not isT and not isS and isL:
        s = s + "'''" + lRow ["PLACE_NAME"] + "'''"
        if lRow ["ALT_NAME"] != "":
            s = s + "(also known as " + lRow ["ALT_NAME"] + ")"
        s = s + " is a [[Suburbs and localities (Australia)|locality]] in the [[" \
            + lgaLede (lRow ["LGA_NAME"]) + "]], [[Queensland]], Australia."
    else:
        print "Found a suburb and locality with the same name!"

    # now emit the citations
    if isT:
        s = s + "<ref name=qpnt>{{cite QPN|" + tRow["REF_NO"] +"|" + tRow["PLACE_NAME"] + "|town in " \
            + lgaLede (tRow ["LGA_NAME"]) + "|accessdate=" + today() + "}}</ref>"
    if isS:
        s = s + "<ref name=qpnl>{{cite QPN|" + lRow["REF_NO"] +"|" + lRow["PLACE_NAME"] + "|suburb in " \
            + lgaLede (lRow ["LGA_NAME"]) + "|accessdate=" + today() + "}}</ref>"
    if isL:
        s = s + "<ref name=qpnl>{{cite QPN|" + lRow["REF_NO"] +"|" + lRow["PLACE_NAME"] + "|locality in " \
            + lgaLede (lRow ["LGA_NAME"]) + "|accessdate=" + today() + "}}</ref>"

    if (isL or isS):
        s=s+" In the {{CensusAU|2016}}, "+lRow["PLACE_NAME"]+" had a population of NUMBER people.<ref name=Census2016>{{Census 2016 AUS|id=ID|name="+lRow["PLACE_NAME"]+" (SSC)|accessdate=20 October 2018|quick=on}}</ref>"
    elif isT:
        s=s+" In the {{CensusAU|2016}}, "+tRow["PLACE_NAME"]+" had a population of NUMBER people.<ref name=Census2016>{{Census 2016 AUS|id=ID|name="+tRow["PLACE_NAME"]+" (UCL)accessdate=20 October 2018|quick=on}}</ref>"
    else:
        print "Panic: Not a town, not a locality, not a suburb"
        sys.exit(1)

    s = s + "\n\n"
        
    # now the History section if needed
    if (isT and hasHistory (tRow)) or ((isS or isL) and hasHistory(lRow)):
            s = s + "== History ==\n"
            if isT:
                if tRow ["COMMENTS"] != "":
                     s = s + tRow ["COMMENTS"] + "<ref name=qpnt/>\n"
            if isS or isL:
                if lRow ["COMMENTS"] != "":
                     s = s + lRow ["COMMENTS"] + "<ref name=qpnl/>\n"
            if isT:
                if tRow ["ORIGIN"] != "":
                     s = s + tRow ["ORIGIN"] + "<ref name=qpnt/>\n"
            if isS or isL:
                if lRow ["ORIGIN"] != "":
                     s = s + lRow ["ORIGIN"] + "<ref name=qpnl/>\n"
            if isT:
                if tRow ["HISTORY"] != "":
                     s = s + tRow ["HISTORY"] + "<ref name=qpnt/>\n"
            if isS or isL:
                if lRow ["HISTORY"] != "":
                     s = s + lRow ["HISTORY"] + "<ref name=qpnl/>\n"
            s = s + "\n"


    # Now the references
    s = s + "== References ==\n" + "{{reflist}}\n\n"

    # Now the external links (if required)
    extLinks = False

    if isT:
        name = tRow["PLACE_NAME"]
    else:
        name = lRow["PLACE_NAME"]

    url = findQueenslandPlaces(name)

    if url != "":
        s = s + "== External links ==\n"
        s = s + "* {{cite web|url=" + url +"|title=" +name+ \
            "|publisher=Centre for the Government of Queensland, " + \
            "University of Queensland|website=Queensland Places}}\n"
        extLinks = True

    if (isT and tRow ["LINKS"] != "") or ((isS or isL) and lRow ["LINKS"] != ""):
        if not extLinks:
            s = s + "== External links ==\n"
            extLinks = True
        if isT and tRow ["LINKS"] != "":
            s = s + extLink (tRow)       #pass the whole row as not sure what we will need to know
        if (isS or isL) and lRow ["LINKS"] != "":
            s = s + extLink (lRow)
        s = s + "\n"

    # Now the navbox and categories

    if isT:
        s = s + "{{" + lgaTemplate(tRow ["LGA_NAME"]) + "}}\n\n" + "[[Category:Towns in Queensland]]\n" \
            + "[[Category:" + lgaCategory (tRow["LGA_NAME"], isS) +"]]\n"
    else:
        s = s + "{{" + lgaTemplate (lRow ["LGA_NAME"]) + "}}\n\n" \
            + "[[Category:" + lgaCategory (lRow ["LGA_NAME"], isS) + "]]\n"

    # stub template
        s = s + "{{Queensland-geo-stub}}\n"
    wikiFile.write (s)
    wikiFile.close ()
    #print s

# the PLACE_NAME field of the database sometimes contains disambiguation
# for our purposes, the LGA_NAME field is sufficient to disambiguate
# and the disambiguation (which is not done consistently) messes up
# a lot of the code, so we will strip it out here

def stripDisambiguation (pn):
    s = string.split(pn, ' (', 1)
    return s[0]

# assumes placenames file is sorted alphabetically and that there is a dummy last element
# if placeName is not supplied or is "", do the whole LGA
# if placeName is supplied, only do the placeName
def doLga (lga, placeName=""):
    #lgaString = " (" + lgaDisambiguation(lga) + ")"
    nameFile=open("QldPlaceNames2016.csv", "rb")
    nameReader= csv.DictReader(nameFile)
    lastname=""
    isTown=False
    isSuburb=False
    isLocality=False
    checklist=""
    townlist=""
    townRow={}
    locRow={}
    name=""
    doneEmit=False

    for row in nameReader:
        if (row ["LGA_NAME"] == lga) and isSettlement(row["TYPE"]):
            name = row["PLACE_NAME"]
            #name2 = name.replace(lgaString,"") #strip any disambiguation
            name2 = stripDisambiguation (name)
            print "doLga:", name,":", name2
            if (name != name2):
                checklist = checklist + " " + name2 + ","
                row ["PLACE_NAME"] = name2
                name=name2
            row["LGA_NAME"] = lgaQPN (row["LGA_NAME"])
            if (name != lastname) and (isTown or isSuburb or isLocality):

                #print "townRow", str(townRow)
                #print "locRow", str(locRow)
                #print isTown, isSuburb, isLocality
                if (placeName=="") or (placeName==lastname):
                    print "Calling emit", name, ":", lastname
                    emit (townRow, locRow, isTown, isSuburb, isLocality)
                    doneEmit=True
                else:
                    print "Not calling emit", name, ":", lastname
                isTown = False
                isSuburb = False
                isLocality = False
            else:
                print "Not calling emit", name, ":", lastname
            if row["TYPE"] == "POPL":
                townRow = row.copy()
                isTown = True
                townlist = townlist + " " + row ["PLACE_NAME"] + ","
            elif row ["TYPE"] == "LOCB":
                locRow = row.copy()
                isLocality = True
            elif row ["TYPE"] == "SUB":
                locRow = row.copy() # process these the same
                isSuburb = True
            lastname = name2

    # the loop above may not emit the last place in the LGA, so if there's anything still buffered, emit it
    if (isTown or isSuburb or isLocality):
        print "emitting last place", townRow["PLACE_NAME"], locRow ["PLACE_NAME"]
        if (placeName=="") or (placeName==lastname):
            emit (townRow, locRow, isTown, isSuburb, isLocality)
            doneEmit=True

    if not doneEmit:
        print "Warning: nothing emitted for'", lga, placeName
    
    print "LGA:", lga
    print "Check:", checklist
    print "Towns:", townlist
    print
    nameFile.close()

    # use the locality as found in QPN database

def main(argv):
    lgaList=[   "Balonne Shire", \
                "Banana Shire", \
                "Barcaldine Regional", \
                "Barcoo Shire", \
                "Blackall Tambo Regional", \
                "Boulia Shire", \
                "Brisbane City", \
                "Bulloo Shire", \
                "Burdekin Shire", \
                "Bundaberg Regional", \
                "Burke Shire", \
                "Cairns Regional", \
                "Carpentaria Shire", \
                "Cassowary Coast Regional", \
                "Central Highlands Regional", \
                "Charters Towers Regional",  \
                "Cherbourg Aboriginal Shire", \
                "Cloncurry Shire", \
                "Cook Shire", \
                "Croydon Shire", \
                "Cloncurry Shire", \
                "Diamantina Shire", \
                "Douglas Shire", \
                "Etheridge Shire", \
                "Flinders Shire", \
                "Fraser Coast Regional", \
                "Gladstone Regional", \
                "Gold Coast City", \
                "Goondiwindi Regional", \
                "Gympie Regional", \
                "Hinchinbrook Shire", \
                "Hope Vale Aboriginal Shire", \
                "Isaac Regional", \
                "Ipswich City", \
                "Livingstone Shire", \
                "Lockyer Valley Regional", \
                "Logan City", \
                "Longreach Regional", \
                "Mackay Regional", \
                "Maranoa Regional", \
                "Mareeba Shire", \
                "Mckinlay Shire", \
                "Moreton Bay Regional", \
                "Mount Isa City", \
                "Murweh Shire", \
                "Napranum Aboriginal Shire", \
                "Noosa Shire", \
                "North Burnett Regional", \
                "Northern Peninsula Area Regional", \
                "Paroo Shire", \
                "Quilpie Shire", \
                "Redland City", \
                "Richmond Shire", \
                "Rockhampton Regional", \
                "Scenic Rim Regional", \
                "Somerset Regional", \
                "South Burnett Regional", \
                "Southern Downs Regional", \
                "Sunshine Coast Regional", \
                "Tablelands Regional", \
                "Toowoomba Regional", \
                "Torres Shire", \
                "Torres Strait Island Regional", \
                "Townsville City", \
                "Weipa Town", \
                "Western Downs Regional", \
                "Whitsunday Regional", \
                "Winton Shire", \
                "Woorabinda Aboriginal Shire" ]

    print "Argv", argv
    if argv ==[]:
        print "Usage: python article.py lgaName [placename]"
        sys.exit (1)
    if len(argv)>=1:
        print argv[0]
        if argv[0] == "all":
            print "Doing all LGAs"
            for lga in lgaList:
                doLga (lga, "")
            sys.exit(0)
        if not (argv[0] in lgaList):
            print "Not a configured LGA", argv[0]
            sys.exit (1)
        if (len(argv)==1): # do articles for the whole LGA
            print "Doing LGA:", argv[0]
            doLga (argv[0], "")
            sys.exit (0)
        for arg in argv[1:]: #do articles for each named locality
            print "Doing LGA:", argv[0], "for place", arg
            doLga (argv[0], arg)
    sys.exit (0)


if __name__ == "__main__":
   main(sys.argv[1:])
