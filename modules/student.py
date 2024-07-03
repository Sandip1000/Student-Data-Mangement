from modules.validation import *
from modules.filemanagement import *

class Student:
     def calc_percent(self,marks):
        sum=0
        count=0
        for key,value in marks.items(): 
          sum=sum+value
          count=count+1
        percentage=sum/count
        return percentage
     
     def pass_fail_detemination(self,marks):
        for key,value in marks.items():
          if value<40:
            remarks="Fail"
            break
          else:
            remarks="Pass"
        return remarks
     
     def accept(self):
          self.name=input("Enter name: ")

          while True:
            self.roll_number=input("Enter Roll Number: ")
            if (validate_student_rollnumber(self.roll_number)==True):
              break
            else:
              print("Invalid Roll Number.Re-enter Roll Number.")

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
            
          self.address=input("Enter address: ")

          print("Enter Marks of Subject: ")

          self.marks={
             "Math":int(input("Math: ")),
             "Science":int(input("Science: ")),
             "Social":int(input("Social: ")),
             "Computer":int(input("Computer: ")),
             "Nepali":int(input("Nepali: "))
          }

          self.percent=self.calc_percent(self.marks)

          self.remarks=self.pass_fail_detemination(self.marks)

          new_data={
                 "name":self.name,
                 "Roll Number":self.roll_number,
                 "Email":self.email,
                 "Phone Number":self.phone_number,
                 "Address":self.address,
                 "Marks":self.marks,
                 "Percent":self.percent,
                 "Remarks":self.remarks
               }
          append_file("datafiles/student.json",new_data)
    
     @staticmethod
     def display_all():
          student_details=read_file("datafiles/student.json")
          print(student_details)

     @staticmethod
     def search(name):
        student_details=read_file("datafiles/student.json")
        for i in student_details:
            if i['name']==name:
              print(f"Name: {i['name']}")
              print(f"Roll Number: {i['Roll Number']}")
              print(f"Email:{i['Email']}")
              print(f"Phone Number: {i['Phone Number']}")
              print(f"Address: {i['Address']}")
              print(f"Marks: {i['Marks']}")
              print(f"Percent: {i['Percent']}")
              print(f"Remarks: {i['Remarks']}")
              return True
        return False
     
     @staticmethod
     def delete_student_record(name):
        student_details=read_file("datafiles/student.json")
        for index,i in student_details(enumerate):
            if i['name']==name:
              student_details.pop(index)
              print(f"Record of {name} has been deleted.")
              return True
        return False   
     
     @staticmethod
     def highest_lowest_percent():
        student_details=read_file("datafiles/student.json")
        max=0
        min=100
        for index,student in enumerate(student_details):
          if student['Percent'] >max:
             max=student['Percent']
             index1=index
          if student['Percent']<min:
             min=student['Percent']
             index2=index
        print(f"Highest pricentage is {max} obtained by {student_details[index1]['name']}")
        print(f"Lowest pricentage is {min} obtained by {student_details[index2]['name']}")  
     
     @staticmethod
     def rank_calculation():
        student_details=read_file("datafiles/student.json")
        sorted_students=sorted(student_details.items(),key=lambda x:x['Percent'],reverse=True )

        ranked_student=[]
        current_rank=1
        for i,student in enumerate(sorted_students):
            if i>0 and student['marks']<sorted_students[i-1]['marks']:
              current_rank=current_rank+1
            ranked_student.append((student['name'], student['marks'], current_rank))
        for name, marks, rank in ranked_student:
            print(f"Name: {name}, Marks: {marks}, Rank: {rank}")
        
              


      