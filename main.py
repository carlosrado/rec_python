import csv
from pydoc import describe
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
    clave=""
    for k in dic.keys():
        dic_interno=dic[k]
        lon_list.append(float(dic_interno["lon"]))
        if(float(dic_interno["lon"])==lon):
            clave = k
    if str(type(lon)) != "<class 'float'>":
        raise ValueError("No es de tipo float")
    elif lon not in lon_list == True:
        raise ValueError("No existe")
    else:
        return clave
def get_min(key, dic):
    dic_list=[]
    for k in dic.keys():
        if float(k)<float(key):
            name,desc=get_name_description(k,dic)
            dic_res={name:desc}
            dic_list.append(dic_res)
    if k < min(dic.keys()):
        raise ValueError("No hay elementos")
    print(dic_list)


if __name__ == "__main__":
    dic=read_data("stops.csv","stops_data.csv")
    print(dic)
    try:
        name, desc = get_name_description("1020",dic)
        print(name, desc)

    except ValueError:
        print("Ha saltado error")
    
    """try:
        name, desc = get_name_description("2020",dic)
        print(name, desc)

    except ValueError:
        print("Ha saltado error")"""

    try:
        k=search_by_lon(-0.366829060109773, dic)
        print(k)
    except ValueError as err:
        if str(err)=="No existe":
            print("Error de clave")
        elif str(err)=="No es de tipo float":
            print("Error de tipo")
    try:
        get_min(1023, dic)
    except ValueError:
        print("Ha saltado error")
