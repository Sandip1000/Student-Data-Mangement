from modules import *

def main():
   while True:
    print("Welcome To Student Management Sytem")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student Record")
    print("5. Student Rank Calculation")
    print("6. Display Highest and Lowest Percentage")
    print("7. Add Teacher ")
    print("8. Display All Teachers")
    print("9. Delete Teacher Record")
    print("10. Exit")

    choice=input("Enter Choice: ")

    if choice=='1':
       obj2=Student()
       obj2.accept()
    elif choice=='2':
       Student.display_all()
    elif choice=='3':
       name=input("Enter name of student: ")
       if Student.search(name)==True:
         pass
       else:
          print("Name not Found")
    elif choice=='4':
      name=input("Enter name to delete: ")
      if Student.delete_student_record(name)==True:
          pass
      else:
         print("Name not Found")
    elif choice=='5':
       Student.rank_calculation()
    elif choice=='6':
       Student.highest_lowest_percent()
    elif choice=='7':
       obj3=Teacher()
       obj3.accept()
    elif choice=='8':
       Teacher.display_all()
    elif choice=='9':
       name=input("Enter name to delete: ")
       if Teacher.delete_teacher_record(name)==True:  
          pass
       else: 
          print("Name not found")
    elif choice=='10':
       print("Thank You")
       break
    else:
       print("Choice not available")
       
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
          break
      else:
          count=count+1
          print("Invalid Name and ID.Reenter Name and ID")
          if count==3:
             break
             
    




    
