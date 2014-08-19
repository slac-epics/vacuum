#!/usr/bin/env python

""" 
This script will handle converting any mks subfile to the sync versions.
awallace
13-5-14    
"""

import re, os, glob

#outer loop to open each file
for subfilename in glob.glob("mks937a-*.substitutions"):
    output = []
    print subfilename
    subfile = open(subfilename, 'r+')
    for line in subfile:
        if re.search(r'^[\s\t]*pattern\s\{[\s\t]*controller[\s\t]*,[\s\t]*port[\t\s]*\}', line):
            line = "    pattern { controller    ,  port             , slowEvt, phase }\n"
        elif re.search(r'^[\s\t]*pattern\s\{[\s\t]*device[\s\t]*,[\s\t]*port[\t\s]*,[\s\t]*channel[\t\s]*,[\s\t]*slot[\t\s]*\}', line):
            line = "    pattern { device       , port         , channel , slot, fastEvt, slowEvt }\n"
        else:
            line = re.sub(r'^[\s\t]*\{[\s\t]*([\w:]+)\s*,\s*([\w:]+)[\t\s]*\}', r'   { \1 , \2, 3, 9}', line)
            line = re.sub(r'^[\s\t]*\{[\s\t]*([\w:]+)\s*,\s*([\w:]+)\s*,\s*(\d)\s*,\s*(\w\w)[\t\s]*\}', r'   { \1 , \2 , \3,  \4,      1, 3}', line)
        output.append(line)
    subfile = open(subfilename, 'w')
    for line in output:
        print line
        subfile.write(line)
os.system('sed -i \'s/vac_/sync_/g\', mks937a*substitutions')   
