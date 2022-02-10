def edit_file(filename,string):
    wr = open(filename,"w")
    wr.write(string)
    wr.close()
def read(filename):
    wr = open(filename,"r")
    readlines = wr.read()
    wr.close()
    return readlines