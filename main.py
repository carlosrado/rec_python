import csv

def read_data(filename1):
    dic = {}
    f = open(filename1, mode="rt", encoding="utf-8")

    linea = f.readline()
    while linea != "" :
        print(linea.split(","))
        linea = f.readline()

    f.close()


if __name__ == "__main__":
    read_data("stops.csv")
