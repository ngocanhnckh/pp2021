import domains
import output
from domains import student, course, mark, students, courses, marks
import os
from zipfile import ZipFile

def addMarkFunction(sid,cid,m):
    s = next(item for item in students if int(item.studentid) == int(sid))
    ma = mark(sid,cid)
    ma.setMark(m)
    marks.append(ma)
    output.writeMark(ma)
    s.gpa = output.getGPA(sid)
            

def addMark():
    output.printStudents()
    sID = input("Select a student by his id: ")
    print("You selected " + str(sID))
    for student in students:
        #print("checking " + student.getID())
        if (int(student.getID()) == int(sID)):
            print("Matched!")
            output.printCourses()
            cID = int(input("Select a course by its id: "))
            m = input("Enter mark:")
            addMarkFunction(sID,cID,m)

def lazyInput():
    students.append(student("Nguyen Ngoc Anh","23/03/2001",10))
    students.append(student("Tran Ngoc Hieu Nam","01/12/2001",54))
    courses.append(course("Math",1,4))
    courses.append(course("Python",2,3))
    addMarkFunction(10,1,20)
    addMarkFunction(10,1,15)
    addMarkFunction(10,1,13.342)
    addMarkFunction(10,1,8.5)
    addMarkFunction(10,2,15)
    addMarkFunction(10,2,20)
    addMarkFunction(10,2,19)
    addMarkFunction(10,2,12)
    addMarkFunction(54,1,5)
    addMarkFunction(54,1,15)
    addMarkFunction(54,1,19.123)
    addMarkFunction(54,1,12)
    addMarkFunction(54,2,20.34)
    addMarkFunction(54,2,20)
    addMarkFunction(54,2,19)
    addMarkFunction(54,2,18)
    #output.writeStudents()
    #output.writeCourses()
    #output.writeMarks()

def loadData():
    with open("student.txt","r") as stxt:
        lines = stxt.readlines()
        for line in lines:
            if (line):
                a = line.split(",")
                name = a[0]
                studentid = a[1]
                dob = a[2]
                gpa= a[3]
            students.append(student(name,dob,studentid))
    with open("course.txt") as ctxt:
        lines = ctxt.readlines()
        for line in lines:
            if (line):
                a = line.split(",")
                name = a[0]
                courseid = a[1]
                etc = a[2]
                courses.append(course(name,courseid,etc))
    with open("mark.txt") as mtxt:
        lines = mtxt.readlines()
        for line in lines:
            if (line):
                a = line.split(",")
                cid = a[0]
                sid = a[1]
                value = a[2]
                addMarkFunction(sid,cid,value)

def InputFunction():
    nS=int(input("Num of students: "))
    #intput stuendts
    for i in range (1,nS+1):
        id = input("Enter " + str(i) + " student ID: ")
        name = input("Student name: ")
        dob = input("Students's date of birth: ")
        students.append(student(name,dob,id))
        output.writeStudent(student(name,dob,id))
  
    #input courses
    nC = int(input("Enter number of courses: "))
    for i in range(1,nC+1):
        id = input("Course ID: ")
        name = input("Course name: ")
        etc = input("How many etcs? ")
        courses.append(course(name,id,etc))
        output.writeCourse(course(name,id,etc))
    