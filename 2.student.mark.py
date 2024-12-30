class Ultra:
    def __init__(self):
        self.strudents=[]
        self.courses=[]
        self.marks={}
class students:
    def __init__(self,sid,name,dob):
        self.sid=sid
        self.name=name
        self.dob=dob
    def __str__(self):
        return f"id:{self.sid},name:{self.name},dob:{self.dob}"
class courses:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
    def __str__(self):
        return f"id:{self.cid},name:{self.name}"
def inputNumStudent(self):
    return int(input("enter the number of student"))
def inputNumCourse(self):
    return int(input("enter the number of courses"))
def inputInfoStudent(self):
    sid=input("enter student's id")
    name=input("enter student's name")
    dob=input("enter student's date of birth")
    self.students.append((sid,name,dob))
def inputInfoCourse(self):
    cid=input("enter course's id")
    name=input("enter course's name")
    self.courses.append((cid,name))
def inputMarksCourse(self):
    cid = input("Enter course ID for input: ")    
    checked = next((c for c in self.course if c.cid == cid), None)
    if not checked:
        print("Course unknown")
        return
    if cid not in self.marks:
        self.marks[cid] = {}
    for student in self.students:
        try:
            mark = float(input(f"Enter mark for student {student.sid}: "))
            self.marks[cid][student.sid] = mark
        except ValueError:
            print("Invalid mark. Skipping this student.")
def outputCourseList(self):
    print("courses:")
    for j in self.courses:
        print(j)
def outputStudentList(self):
    print("students:")
    for k in self.students:
        print(k)
def outputStudentMarks(self):
    cid=input("enter course id for output")
    if cid not in self.marks:
        print("course unknown")
        return
    print(f"marks for course {cid}:")
    for sid,mark in self.marks[cid].itens():
        print(f"student's id:{sid},mark:{mark}")
if __name__ == "__main__":
    Ultra = Ultra()

    num_students = Ultra.input_num_students()
    for _ in range(num_students):
        Ultra.input_student_info()

    num_courses = Ultra.input_num_courses()
    for _ in range(num_courses):
        Ultra.input_course_info()

    while True:
        print("\nOptions:")
        print("1. Input marks for a course")
        print("2. View courses")
        print("3. View students")
        print("4. View marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            Ultra.inputMarksCourse()
        elif choice == "2":
            Ultra.outputCourseList()
        elif choice == "3":
            Ultra.outputStudentList()
        elif choice == "4":
            Ultra.outputStudentMarks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

