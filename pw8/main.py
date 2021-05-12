import math
import numpy 
#import curses
from domains import student, course, mark
import input as inp
import output
import os
from zipfile import ZipFile


def main():
    with ZipFile("students.dat","r") as zip:
        zip.extractall()
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
    #inp.loadData()
    inp.readAll()
    
    while (option != "9"):
        option = input("Your option: ")
        if (option=="1"):
            inp.InputFunction()
        if (option=="2"):
            inp.addMark()
        if (option=="3"):
            output.printStudents()
        if (option=="4"):
            output.printCourses()
        if (option=="5"):
            output.printMark()
        if (option=="6"):
            output.showAvarage()
        if (option=="7"):
            output.showWeightedSum()
        if (option=="8"):
            output.sortstudentbyGPA()
    output.writeAll()
    output.writeZip()
    print("Just a friendly goodbye")

if __name__ == "__main__":
    main()