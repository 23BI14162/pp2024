students=[]  
courses=[]  
marks={}    
def inputNumStudent():
    return int(input("Enter the number of students:"))
def inputInfoStudent():
    student_id=input("Enter student ID:")
    name=input("Enter student name:")
    dob=input("Enter student date of birth:")
    students.append((student_id, name, dob))
def inputNumCourses():
    return int(input("Enter the number of courses:"))
def inputInfoCourse():
    cid=input("Enter course ID:")
    name=input("Enter course name:")
    courses.append((cid, name))
def inputMarksCourses():
    cid=input("Enter course ID to input marks for:")
    if cid not in [c[0] for c in courses]:
        print("Course not found!")
        return
    marks[cid]={}
    for i in students:
        student_id=i[0]
        mark=float(input(f"Enter mark for student {student_id}:"))
        marks[cid][student_id]=mark
def outputCourseList():
    print("Courses:")
    for j in courses:
        print(f"ID:{j[0]}, Name:{j[1]}")
def outputStudentList():
    print("Students:")
    for k in students:
        print(f"ID:{k[0]}, Name:{k[1]}, DoB:{k[2]}")
def outputStudentMarks():
    cid=input("Enter course ID to view marks:")
    if cid not in marks:
        print("No marks found for this course!")
        return
    print(f"Marks for course {cid}:")
    for student_id, mark in marks[cid].items():
        print(f"Student ID:{student_id}, Mark:{mark}")
