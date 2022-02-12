import os, sys, random
from lib import byte_analizer as ba

fr = open("bcode.lbc","r")
Splitted = fr.read().split("\n")
sh = 1
for i in Splitted:
    sh += 1
    ba.analize(string=i,str=sh)