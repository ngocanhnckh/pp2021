import curses
from domains import student, course, mark, students, courses, marks
import numpy
import math


def getGPA(sid):
    smark = []
    for mark in marks:
        if (mark.sid == float(sid)):
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
