from modules import *

def main():
    print("Welcome To Student Management Sytem")
    print("1. Add Student")
    print
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Display All Teacher")
    print("5. D")
    print("6. Student Rank Calculation")
    print("8. Exit")

    choice=input("Enter Choice: ")

    if choice=='1':
       obj2=Student()
       obj2.accept()
    elif choice=='2':
       Student.display_all()
    elif choice=='3':
       name=input("Enter name of student: ")
       if Student.search(name)==True:
          print("Student Details: ")
          Student.search(name)
       else:
          print("Name not found")
    elif choice=='4':
       Teacher.display_all()
    elif choice=='5':
       name=input("Enter name of student: ")
       if Student.delete_student_record(name)==True:
          Student.delete_student_record
       else:
          print("No such name found")
    elif choice=='6':
       pass
       
if read_file("datafiles/teacher.json")==[]:
   count=0
   while True:
      print("Sign Up")
      obj1=Teacher()
      obj1.accept()
      count=count+1
      if count==3:
          break
while True:
      print("Login In")
      name=input("Enter Name: ")
      id=input("Enter ID: ")
      count=0
      if authenticate(name,id)==True:
          main()
      else:
          count=count+1
          print("Invalid Name and ID.Reenter Name and ID")
          if count==3:
             break
             
    




    
