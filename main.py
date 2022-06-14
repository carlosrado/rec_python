import csv

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
    dic_interno = dic[key]
    name=dic_interno["name"]
    desc=dic_interno["description"]
    return name, desc

if __name__ == "__main__":
    dic=read_data("stops.csv","stops_data.csv")
    name, desc = get_name_description("1020",dic)
