import math
import numpy 
import curses

marks=[]
students=[]
courses=[]

class student():
    name = ""
    dob = ""
    gpa = 0.0
    studentid=0
    def __init__(self, name, dob,studentid):
        self.name=name
        self.dob=dob
        self.studentid=studentid

    def display(self):
        print("Student {0} has ID {1} with date of birth: {2} and GPA: {3} ".format(self.name,self.studentid,self.dob, self.gpa))
        
    def getID(self):
        return self.studentid

class course():
    name = ""
    courseid = 0
    etc = 0
    def __init__(self,name,courseid,etc):
        self.name=name
        self.courseid=courseid
        self.etc = etc
    
    def display(self):
        print("Course id " + str(self.courseid) + " name: " + self.name + " with " + str(self.etc) + "etc(s)")


class mark():
    cid=0
    sid=0
    #encapsulation
    __value=0.0
    def __init__(self,sid,cid):
        self.sid=sid
        self.cid=cid

    def setMark(self,value):
        self.__value = math.floor(float(value)*10)/10

    def getMark(self):
        return self.__value

    def printMark(self):
        studentMark = next(item for item in students if int(item.studentid) == int(self.sid))
        courseMark = next(item for item in courses if int(item.courseid)==int(self.cid))
        print("Mark for student {0} at course {1} is {2}".format(studentMark.name,courseMark.name,self.__value))
