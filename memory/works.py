import requests  # импортируем модул
def edit_file(filename,string):
    wr = open(filename,"w")
    wr.write(string)
    wr.close()
def read(filename):
    wr = open(filename,"r")
    readlines = wr.read()
    wr.close()
    return readlines
def download_file(http_url,file_path):

    f = open(file_path, "wb")  # открываем файл для записи, в режиме wb
    ufr = requests.get(http_url)  # делаем запрос
    f.write(ufr.content)  # записываем содержимое в файл; как видите - content запроса
    f.close()