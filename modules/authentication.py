from modules.filemanagement import read_file

def authenticate(name,id):
   teacher_details=read_file("datafiles/teacher.json")
   for i in teacher_details:
      if i['name']==name and i['id']==id:
         return True
   return False