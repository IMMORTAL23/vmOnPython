import os, sys, random
from lib import byte_analizer as ba

fr = open("bcode.lbc","r")
Splitted = fr.read().split("\n")

for i in Splitted:
    ba.analize(i)