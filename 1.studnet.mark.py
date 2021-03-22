
#Init variables
students = list()
courses = []
mark = []
#Input functions
def InputFunction():
    nS=int(input("Num of students: "))
    #intput stuendts
    for i in range (1,nS+1):
        id = input("Enter " + str(i) + " student ID: ")
        name = input("Student name: ")
        dob = input("Students's date of birth: ")
        students.append({"id": id,"name":name,"date of birth: ":dob})
    #input courses
    nC = int(input("Enter number of courses: "))
    for i in range(1,nC+1):
        id = input("Course ID: ")
        name = input("Course name: ")
        courses.append({"id":id,"name":name})
    
def printStudents():
    print(students)

def printCourses():
    print(courses)

def printMark():
    #print all marks
    print(mark)
    #choose a student
    printStudents()
    sID = input("Which student? (Select by id): ")
    student = next(item for item in students if item["id"] == sID)
    print("Showing mark for student " + student.get("name") + ":")
    #show all mark by student id
    for m in mark:
        if m['studentID']==int(sID):
            print(m)


def addMark():
    printStudents()
    sID = int(input("Select a student by his id: "))
    printCourses()
    cID = int(input("Select a course by its id: "))
    m = input("Enter mark:")
    mark.append({"studentID":sID,"courseID":cID,"mark":m})



def main():
    
    option = "-1"
    while (option != "6"):
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

