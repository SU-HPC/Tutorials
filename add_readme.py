import os

files = os.listdir("/home/fatih/Documents/tutorials/hpc_01/docs")
print(files)

read_arr = []

for item in files:
    if(item.find("~") != -1):
        print(item.find("~"))
        reader = open(item, "r")
        arr = reader.readlines()
        print(arr)
