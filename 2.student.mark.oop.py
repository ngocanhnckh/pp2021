#Init variables
students = []
courses = []
marks = []

## Init all the classes

class student():
    name = ""
    dob = ""
    studentid=0
    def __init__(self, name, dob,studentid):
        self.name=name
        self.dob=dob
        self.studentid=studentid

    def display(self):
        print("Student {0} has ID {1} with date of birth: {2}".format(self.name,self.studentid,self.dob))
        
    def getID(self):
        return self.studentid

class course():
    name = ""
    courseid = 0
    def __init__(self,name,courseid):
        self.name=name
        self.courseid=courseid
    
    def display(self):
        print("Course id " + self.courseid + " name: " + self.name)

class mark():
    cid=0
    sid=0
    #encapsulation
    __value=0
    def __init__(self,sid,cid):
        self.sid=sid
        self.cid=cid

    def setMark(self,value):
        self.__value = value

    def printMark(self):
        studentMark = next(item for item in students if int(item.studentid) == int(self.sid))
        courseMark = next(item for item in courses if int(item.courseid)==int(self.cid))
        print("Mark for student {0} at course {1} is {2}".format(studentMark.name,courseMark.name,self.__value))

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
        courses.append(course(name,id))

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
        if (mark.sid == sID):
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
            obm=mark(sID,cID)
            obm.setMark(m)
            marks.append(obm)

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
    6. Exit
    """)
    while (option != "6"):
      
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
    print("Just a friendly goodbye")
if __name__ == "__main__":
    main()