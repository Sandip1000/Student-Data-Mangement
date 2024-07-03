from modules.filemanagement import *

def validate_string(str):
    string1="1234567890"
    string2="!#$%^&*(){}[]:.,;<>?|"
    for char in string1:
            if char==str[0]:
                return False
    for char1 in string2:
        for char2 in str:
            if char2==char1:
                return False
    return True
def validate_email(email):
    if email.count('@')==1:
        temp1,temp2=email.split('@')
        if (temp2=="gmail.com" or temp2=="outlook.com" or temp2=="yahoo.com") and (len(temp1)>5) and (validate_string(temp1)==True):
           return True
        else:
           return False
    else:
        return False

def validate_student_rollnumber(roll_number):
    student_details=read_file("datafiles/student.json")
    for i in student_details:
        if i['Roll Number']==roll_number:
            return False
    return True

def validate_teacher_id(id):
    teacher_details=read_file("datafiles/teacher.json")
    for i in teacher_details:
        if i['id']==id:
            return False
    return True  
    
    

def is_digit(num):
    number="0123456789"
    for char in number:
        if (char==num):
          return True
    return False

def validate_ph(ph):
    for char in ph:
        if is_digit(char)==False and len(ph)!=10:
            return False
        break     
    return True

