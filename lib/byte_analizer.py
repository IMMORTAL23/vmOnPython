import os, time, re
import memory.works as wk


Variables = {}
Functions = {}
VMDatas = {}
def analize(string="print:Hello world!",str=0):
    string_cmd = string.split(":",maxsplit=1)[0].lower()
    if string_cmd == "print":
        splitted = string.split(":",maxsplit=1)
        print(splitted[1].replace("%n","\n"))
    elif string_cmd=="input":
        splitted = string.split(":")
        input(splitted[1])
    elif string == "input":
        input()
    elif string_cmd=="editfile":
        splitted = string.split(":",maxsplit=2)
        filename=splitted[1]
        string2 = splitted[2]
        wk.edit_file(filename,string2.replace("%n","\n"))
    elif string_cmd=="readfile":
        splitted = string.split(":",maxsplit=1)
        filename=splitted[1]
        print(wk.read(filename))
    elif string_cmd=="pyexec":
        splitted = string.split(":", maxsplit=1)
        exec(splitted[1])
    elif string_cmd=="var":
        splitted = string.split(":")
        splitted_tst = splitted[1].split("=")
        if splitted_tst[1] == "input":
            Variables[splitted_tst[0]] = input().replace("%n","\n")
        else:
            Variables[splitted_tst[0]] = splitted_tst[1].replace("%n","\n")
    elif string_cmd=="printvar":
        splitted = string.split(":")

        print(Variables[splitted[1]])
    elif string_cmd=="if":
        f = "F"
        splitted = string.split(":",maxsplit=2)
        splitted_2 = splitted[1].split("=")
        if Variables[splitted_2[0]] == splitted_2[1]:
            analize(splitted[2])
        else:
            pass
    elif string_cmd == "mkdir":
        splitted = string.split(":",maxsplit=1)
        #mkdir:DirName
        if not os.path.isdir(splitted[1]):
            os.mkdir(splitted[1])
    elif string_cmd == "chdir":
        splitted = string.split(":", maxsplit=1)
        try:
            os.chdir(splitted[1])
        except:
            pass
    elif string_cmd == "remove":
        splitted = string.split(":", maxsplit=1)
        try:
            os.remove(splitted[1])
        except:
            pass
    elif string_cmd == "sleep":
        splitted = string.split(":")
        time.sleep(int(splitted[1]))
    elif string_cmd == "func":
        splitted = string.split(":",maxsplit=2)
        list_cmds = splitted[2]
        name_function = splitted[1]
        Functions[name_function] = list_cmds
    elif string_cmd == "funcstart":
        splitted = string.split(":")
        func_devs = Functions[splitted[1]]
        cmd_list = re.sub(r'[\'\[\]]', '', func_devs).split(',')
        for i in cmd_list:
            analize(i)
    elif string_cmd == "downloadfile":
        splitted = string.split(":")
        splitted[1] = "http://"+splitted[1]
        wk.download_file(splitted[1],splitted[2])
    elif string_cmd == "ascii":pass
