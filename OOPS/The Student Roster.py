class student:
    total_student = 0
    def __init__(self,name,grade):

        self.name=name
        self.grade=grade
        student.total_student +=1




name1=input("enter the name of Student :- ")
grade1=input(" enter the grade :- ")
st1=student(name1,grade1)

name2=input(" \nenter the name of Student :- ")
grade2=input("\n enter the grade :- ")
st2=student(name2,grade2)
print( " total number of student :-  ",student.total_student)
