import os
import memory.works as wk

def analize(string="print:Hello world!"):
    if string.startswith("print:"):
        splitted = string.split(":",maxsplit=1)
        print(splitted[1].replace("%n","\n"))
    elif string.startswith("input:"):
        splitted = string.split(":")
        input(splitted[1])
    elif string == "input":
        input()
    elif string.startswith("editfile:"):
        splitted = string.split(":",maxsplit=2)
        filename=splitted[1]
        string2 = splitted[2]
        wk.edit_file(filename,string2.replace("%n","\n"))
    elif string.startswith("readfile:"):
        splitted = string.split(":",maxsplit=1)
        filename=splitted[1]
        print(wk.read(filename))