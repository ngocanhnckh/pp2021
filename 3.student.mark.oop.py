import math
import numpy 
import curses
#Init variables
students = []
courses = []
marks = []

## Init all the classes

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
        self.__value = math.floor(value*10)/10

    def getMark(self):
        return self.__value

    def printMark(self):
        studentMark = next(item for item in students if int(item.studentid) == int(self.sid))
        courseMark = next(item for item in courses if int(item.courseid)==int(self.cid))
        print("Mark for student {0} at course {1} is {2}".format(studentMark.name,courseMark.name,self.__value))

def getGPA(sid):
    smark = []
    for mark in marks:
        if (mark.sid == float(sid)):
            smark.append(mark.getMark())
    return numpy.average(smark)
            
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


def InputFunction():
    nS=int(input("Num of students: "))
    #intput stuendts
    for i in range (1,nS+1):
        id = input("Enter " + str(i) + " student ID: ")
        name = input("Student name: ")
        dob = input("Students's date of birth: ")
        students.append(student(name,dob,id))
    #input courses
    nC = int(input("Enter number of courses: "))
    for i in range(1,nC+1):
        id = input("Course ID: ")
        name = input("Course name: ")
        etc = input("How many etcs? ")
        courses.append(course(name,id,etc))

def addMarkFunction(sid,cid,m):
    s = next(item for item in students if int(item.studentid) == int(sid))
    ma = mark(sid,cid)
    ma.setMark(m)
    marks.append(ma)
    s.gpa = getGPA(sid)

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
        if (mark.sid == float(sID)):
            mark.printMark()


## AddMark

def addMark():
    printStudents()
    sID = input("Select a student by his id: ")
    print("You selected " + str(sID))
    for student in students:
        print("checking " + student.getID())
        if (int(student.getID()) == int(sID)):
            print("Matched!")
            printCourses()
            cID = int(input("Select a course by its id: "))
            m = input("Enter mark:")
            addMarkFunction(sID,cID,m)

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

def main():
    
    option = "-1"
    print("""
    (                                                                                     
    )\ )    )        (                   )                                                
    (()/( ( /(   (    )\ )   (         ( /(      )       )            )  (  (     (   (    
    /(_)))\()) ))\  (()/(  ))\  (     )\())    (     ( /(   (     ( /(  )\))(   ))\  )(   
    (_)) (_))/ /((_)  ((_))/((_) )\ ) (_))/     )\  ' )(_))  )\ )  )(_))((_))\  /((_)(()\  
    / __|| |_ (_))(   _| |(_))  _(_/( | |_    _((_)) ((_)_  _(_/( ((_)_  (()(_)(_))   ((_) 
    \__ \|  _|| || |/ _` |/ -_)| ' \))|  _|  | '  \()/ _` || ' \))/ _` |/ _` | / -_) | '_| 
    |___/ \__| \_,_|\__,_|\___||_||_|  \__|  |_|_|_| \__,_||_||_| \__,_|\__, | \___| |_|   
                                                                        |___/              
    by ngocanhnckh                                                                BI10-010
    --------------------------------------------------------------------------------------
    Please select an option from menu:
    1. Input students and courese
    2. Add mark
    3. List current student list
    4. List current course list
    5. List current mark list
    6. Calculate average score
    7. Calculate weighted sum
    8. Show sorted students
    9. Exit()
    """)
    lazyInput()
    while (option != "9"):
        option = input("Your option: ")
        if (option=="1"):
            InputFunction()
        if (option=="2"):
            addMark()
        if (option=="3"):
            printStudents()
        if (option=="4"):
            printCourses()
        if (option=="5"):
            printMark()
        if (option=="6"):
            showAvarage()
        if (option=="7"):
            showWeightedSum()
        if (option=="8"):
            sortstudentbyGPA()
    print("Just a friendly goodbye")

if __name__ == "__main__":
    main()