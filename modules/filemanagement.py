import json


def read_file(filepath):
    try:
        with open(filepath,"r")as file:
            return json.load(file)
    except Exception:
         return []


def write_file(filepath,data):
     with open(filepath,"w")as file:
          json.dump(data,file,indent=4)

def append_file(filepath,new_data):
     data=read_file(filepath)
     data.append(new_data)
     write_file(filepath,data)