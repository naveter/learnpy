import os
import re

# This script will read each dir in path and look for ivy.xml files.
# After it will read them, analise and filter it by adding to array

dir_path = r'../resource'
modulesMap = {}

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)): continue
    if not os.path.join(dir_path, path, 'ivy.xml') : continue

    lines = []
    with open(os.path.join(dir_path, path, 'ivy.xml'), 'r') as ivy:
        lines = ivy.readlines()

    for str in lines:
        dep = re.match(".*<dependency.*", str)
        if not dep : continue

        # <dependency org="junit" name="junit" rev="4.11" />
        org = re.match('.+org="([a-z0-9-]+)".+', str)
        name = re.match('.+name="([a-z0-9-]+)".+', str)
        rev = re.match('.+rev="([0-9.]+)".+', str)
        if not org and not name : continue

        if not org.groups()[0] in modulesMap: modulesMap[org.groups()[0]] = {}
        nameMap = modulesMap[org.groups()[0]]

        if len(nameMap.keys()) == 0 :
            modulesMap[org.groups()[0]][name.groups()[0]] = []
            if rev : modulesMap[org.groups()[0]][name.groups()[0]].append(rev.groups()[0])
        else :
            if name.groups()[0] in nameMap :
                if rev and (not rev.groups()[0] in nameMap[name.groups()[0]]) :
                    modulesMap[org.groups()[0]][name.groups()[0]].append(rev.groups()[0])
                else : continue
            else :
                modulesMap[org.groups()[0]][name.groups()[0]] = []
                if rev : modulesMap[org.groups()[0]][name.groups()[0]].append(rev.groups()[0])
        # if
    # for
# for

for orgkey, orgval in modulesMap.items() :
    for namekey, nameval in orgval.items() :
        print("org=" + orgkey + " name=" + namekey + " " + ", ".join(nameval) )
    # for
# for




