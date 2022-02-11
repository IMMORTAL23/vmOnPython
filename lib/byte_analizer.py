import os, time
import memory.works as wk
Variables = {}

def analize(string="print:Hello world!"):
    string_cmd = string.split(":")[0].lower()
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
    else:
        exit("4xx")
