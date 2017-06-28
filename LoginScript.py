#!/usr/bin/python

import os
import time
from SystemConfiguration import SCDynamicStoreCopyConsoleUser
import sys
import subprocess
import string
import logging
import syslog

##REPLACE ITEMS SURROUNDED BY <> WITH YOUR INFORMATION

FQDN = "<YOUR FULLY QUALIFIED DOMAIN NAME>"
DOMAIN = "<SHORT DOMAIN>"

path = ""
domainController = "<DOMAIN CONTROLLER ADDRESS>"
#logging.basicConfig(filename='/var/log/LoginScript.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


username = (SCDynamicStoreCopyConsoleUser(None, None, None) or [None])[0]; username = [username,""][username in [u"loginwindow", None, u""]]; sys.stdout.write(username + "\n")
accountType = os.system("dscl \"/Active Directory/" + DOMAIN+ "/" + FQDN + "\" -read /Users/" + username + " | grep UniqueID | cut -c 11-")
#Attempt to read Active Directory Groups from dscl

def mountSpecial():

    if username == "<USER WITH SPECIAL NEEDS>":
        print("User is member of Marketing: " + username)
        mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")

    if username == "<SECOND SPECIAL USER>":
        print("User is member of Marketing: " + username)
        mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")

def getADGroups():
    #function to retrieve AD Group Membership
    print("Determining Active Directory Groups for: " + username)
    groupMembership = subprocess.check_output(['ldapsearch', '-LLL', '-Q', '-H', 'ldap://dc-r2.igs.vic.edu.au', '-b', 'dc=igs,dc=vic,dc=edu,dc=au', '(&(objectCategory=Person)(objectClass=User)(sAMAccountName={0}))'.format(username), 'memberOf', '2>/dev/null'])
    groupMembership = groupMembership.strip()
    groupMembership = groupMembership.strip("memberOf: CN=")
    groups = groupMembership.split("CN=")
    #ridiculous if statement to mount relevant SMB Shares (using mount function) based on group membership of user
    for line in groups:
        #cut from first comma
        #print line
        if "adminr" in line:
            #match exact strings
            print("User is member of Ridgeway Admin: " + username)

            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "adminp" in line:
            print("User is member of Plenty Admin: " + username)

            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "IT Services Staff" in line:
            print("User is member of IT Services Staff: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "0000P" in line:
            print("User in 0000P group: " + username)
        if "0000R" in line:
            print("User in 0000R group: " + username)
        if "2016P" in line:
            print("User in 2016P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2016R" in line:
            print("User in 2016R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2017P" in line:
            print("User in 2017P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2017R" in line:
            print("User in 2017R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2018P" in line:
            print("User in 2018P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2018R" in line:
            print("User in 2018R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2019P" in line:
            print("User in 2019P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2019R" in line:
            print("User in 2019R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2020P" in line:
            print("User in 2020P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2020R" in line:
            print("User in 2020R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2021P" in line:
            print("User in 2021P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2021R" in line:
            logging.debug("User in 2021R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2022P" in line:
            print("User in 2022P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2022R" in line:
            print("User in 2022R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2023P" in line:
            print("User in 2023P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2023R" in line:
            print("User in 2023R group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2024P" in line:
            print("User in 2024P group: " + username)
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
            mount("<SERVER NAME>","<SHAREPOINT NAME>","<MOUNT NAME>")
        if "2024R" in line:
            print("User in 2024R group " + username)
            mount("goofy2", "collaboration", "collaboration")
            mount("goofy", "public", "public")
        if "2025P" in line:
            print("User in 2025P group: " + username)
            mount("sylvester", "collaboration", "collaboration")
            mount("sylvester", "public", "public")
        if "2025R" in line:
            print("User in 2025R group: " + username)
            mount("goofy2", "collaboration", "collaboration")
            mount("goofy", "public", "public")
        if "2026P" in line:
            print("User in 2026P group: " + username)
            mount("sylvester", "collaboration", "collaboration")
            mount("sylvester", "public", "public")
        if "2026R" in line:
            print("User in 2026R group: " + username)
            mount("goofy2", "collaboration", "collaboration")
            mount("goofy", "public", "public")
        if "2027P" in line:
            print("User in 2027P group: " + username)
            mount("sylvester", "collaboration", "collaboration")
            mount("sylvester", "public", "public")
        if "2027R" in line:
            print("User in 2027R group: " + username)
            mount("goofy2", "collaboration", "collaboration")
            mount("goofy", "public", "public")
        if "externalR" in line:
            print("User in externalR group: " + username)
            mount("goofy", "staff", "staff")
            mount("goofy", "public", "public")
        if "externalP" in line:
            print("User in externalP group: " + username)
            mount("sylvester", "staff", "staff")
            mount("sylvester", "public", "public")
        if "academicR" in line:
            print("User in Academic R Group: " + username)

            mount("goofy2", "collaboration", "collaboration")
            mount("goofy4", "Photos", "Photos")
            mount("goofy", "staff", "staff")
            mount("goofy", "public", "public")
        if "academicP" in line:
            print("User in Academic P Group: " + username)

            mount("sylvester2", "collaboration", "collaboration")
            mount("sylvester", "Photos", "Photos")
            mount("sylvester", "staff", "staff")
            mount("sylvester", "public", "public")

def mount(server, share, mountPoint):
    directory = "/Volumes/" + mountPoint
    print "Mounting /" + server + "." + FQDN + "/" + share + " as /Volumes/" + mountPoint
    logging.debug("Mounting " + server + "." + FQDN + "/" + share + " as " + directory)
    if not os.path.exists(directory):
        os.system("osascript -e 'mount volume \"smb://" + server + "." + FQDN + "/"+ share + "\"'")
    else:
        logging.debug("Mount point already exists. Skipping")
        print "Mount point already exists. Skipping"

def mountHome():
    directory = "/Volumes/" + username
    logging.debug("Locating Network Home Folder for: " + username)
    # Notice that each of the the pieces of the command are separated with a comma when you would have a space in bash
    command = ['/usr/bin/dscl', '/Active Directory/' + DOMAIN + '/' + FQDN, '-read', '/Users/' + username, 'SMBHome']

    output = subprocess.check_output(command, stderr=subprocess.PIPE)
    path = output.strip().split(": ")

    # Now we want to only get the path since this was your real goal. The [1] say to only retrieve the second object in the list
    path = output.strip().split(": ")[1]
    path = path.replace('\\', '/')

    logging.debug("Home Folder Location: " + path)

    print path

    if not os.path.exists(directory):

        os.system("osascript -e 'mount volume \"smb:" + path + "\" as user name \"" + username + "\"'")

if accountType != "":
    print("Mounting Network folders for: " + username)
    mountHome()
    getADGroups()
    mountSpecial()
else:
    print("Active Directory Binding is broken. Please repair AD Binding for: " + username)
