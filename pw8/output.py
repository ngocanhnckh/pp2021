import curses
from domains import student, course, mark, students, courses, marks
import numpy
import math
from zipfile import ZipFile
import os
import pickle
import threading

def writeZip():
    with ZipFile("students.dat","w") as zip:
        zip.write("students")
        zip.write("courses")
        zip.write("marks")
    zip.close()
    os.remove("students")
    os.remove("courses")
    os.remove("marks")

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

class backdgroundWrite(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        with open("students","wb") as sfile:
            sfile.write(pickle.dumps(students))
        with open("courses","wb") as cfile:
            cfile.write(pickle.dumps(courses))
        with open("marks","wb") as mfile:
            mfile.write(pickle.dumps(marks))

def writeAll():
    bWrite = backdgroundWrite()
    bWrite.start()
    bWrite.join()

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
