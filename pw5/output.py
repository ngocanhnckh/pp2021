import curses
from domains import student, course, mark, students, courses, marks
import numpy
import math
from zipfile import ZipFile
import os
def writeZip():
    with ZipFile("students.dat","w") as zip:
        zip.write("student.txt")
        zip.write("course.txt")
        zip.write("mark.txt")
    zip.close()
    os.remove("student.txt")
    os.remove("course.txt")
    os.remove("mark.txt")

def getGPA(sid):
    smark = []
    for mark in marks:
        if (str(mark.sid) == str(sid)):
            smark.append(float(mark.getMark()))
    return float(numpy.average(smark))
            
def getWeightedSum(sid):
    sum = 0
    for c in courses:
        smark = []
        warray = []
        for mark in marks:
            if (mark.sid == float(sid)):
                smark.append(mark.getMark())
                warray.append(c.etc)
        weights = numpy.array(warray)
        amark = numpy.array(smark)
        sum = sum + numpy.sum(numpy.dot(amark,weights))
    return sum

def printStudents():
    for student in students:
        student.display()

def printCourses():
    for course in courses:
        course.display()

def writeStudents():
    with open("student.txt","a") as txt_file:
        for s in students:
            txt_file.write("{0},{1},{2},{3}\n".format(s.name,s.studentid,s.dob, s.gpa))

def writeStudent(s):
    with open("student.txt","a") as txt_file:
        txt_file.write("{0},{1},{2},{3}\n".format(s.name,s.studentid,s.dob, s.gpa))

def writeMark(m):
    with open("mark.txt","a") as txt:
        txt.write("{0},{1},{2}\n".format(m.cid,m.sid,m.getMark()))

def writeCourse(c):
    with open("course.txt","a") as txt:
        txt.write("{0},{1},{2}\n".format(c.name,c.courseid,c.etc))


            


def printMark():
    #choose a student
    printStudents()
    sID = input("Which student? (Select by id): ")
    for mark in marks:
        if (str(mark.sid) == str(sID)):
            mark.printMark()

def sortstudentbyGPA():
    newlist = sorted(students, key=lambda x: x.gpa, reverse=True)
    for s in newlist:
        s.display()

def showAvarage():
    printStudents()
    sid = input("Please enter student id: ")
    s = next(item for item in students if int(item.studentid) == int(sid))
    print("The average score is: " + str(s.gpa))

def showWeightedSum():
    printStudents()
    sid = input("Please enter student id: ")
    print("The wighted sum is: " + str(getWeightedSum(sid)))
