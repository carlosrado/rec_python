import csv
from tkinter.tix import Tree

def read_data(filename1, filename2):
    dic = {}
    f1 = open(filename1, mode="rt", encoding="utf-8")
    f2 = open(filename2, mode="rt", encoding="utf-8")

    linea1 = f1.readline()
    linea2 = f1.readline()

    while linea1 != "" :
        linea1=linea1.split(",")
        linea2=linea2.split(",")
        dic_interno={}
        dic_interno.update({"description":linea1[3]})
        dic_interno.update({"id":linea1[0]})
        dic_interno.update({"lat":linea2[4]})
        dic_interno.update({"lon":linea2[5]})
        dic_interno.update({"name":linea1[2]})
        dic.update({linea1[0]: dic_interno})
        linea1 = f1.readline()
        linea2 = f2.readline()

    f1.close()
    return dic

def get_name_description(key, dic):
    if key not in dic.keys() == True:
        raise ValueError("No existe")
    else:
        dic_interno = dic[key]
        name=dic_interno["name"]
        desc=dic_interno["description"]
        return name, desc

def search_by_lon(lon, dic):
    lon_list=[]
    for k in dic.keys():
        dic_interno=dic[k]
        lon_list.append(dic_interno["lon"])
    print(lon_list)

if __name__ == "__main__":
    dic=read_data("stops.csv","stops_data.csv")
    try:
        name, desc = get_name_description("1020",dic)
        print(name, desc)

    except ValueError:
        print("Ha saltado error")
    
    try:
        name, desc = get_name_description("2020",dic)
        print(name, desc)

    except ValueError:
        print("Ha saltado error")

    search_by_lon(1.0, dic)