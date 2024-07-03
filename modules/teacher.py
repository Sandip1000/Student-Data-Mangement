from modules.validation import *
from modules.filemanagement import *

class Teacher:
    
  def accept(self):
        self.name=input("Enter teacher name: ")
        self.subject=input("Enter Subject: ")

        while True:
            self.id=input("Enter id: ")
            if (validate_teacher_id(self.id)==True):
              break
            else:
              print("Invalid ID.Re-enter ID")
        
        self.address=input("Enter Address: ")

        while True:
            self.email=input("Enter email: ")
            if (validate_email(self.email)==True):
              break
            else:
              print("Invalid Email.Re-enter Email")

        while True:      
           self.phone_number=input("Enter Phone Number: ")
           if (validate_ph(self.phone_number)==True):
              break
           else:
              print("Invalid Phone Number.Re-enter Phone Number")

        teacher_data={
                 "name":self.name,
                 "subject":self.subject,
                 "id":self.id,
                 "address":self.address,
                 "email":self.email,
                 "Phone Number":self.phone_number,
        }
        append_file("datafiles/teacher.json",teacher_data)
    
  @staticmethod
  def display_all():
        teacher_details=read_file("datafiles/teacher.json")
        print(teacher_details)