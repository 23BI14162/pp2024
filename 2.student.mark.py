class Ultra:
    def _init_(self): 
        self.students=[]  
        self.courses=[]      
        self.marks={}    
class student:
    def __init__(self,sid,name,dob):
        self.sid=sid
        self.name=name
        self.dob=dob
    def _str_(self):
        return f"ID:{self.student_id},Name:{self.name},DoB:{self.dob}"
class course:
    def _init_(self,cid,name):
        self.cid=cid
        self.name=name
    def __str__(self):
        return f"ID:{self.cid},Name:{self.name}"
def inputNumStudent(self):
    return int(input("Enter the number of students:"))
def inputInfoStudent(self):
    student_id=input("Enter student ID:")
    name=input("Enter student name:")
    dob=input("Enter student date of birth:")
    self.students.append((student_id,name,dob))
def inputNumCourses(self):
    return int(input("Enter the number of courses:"))
def inputInfoCourse(self):
    cid=input("Enter course ID:")
    name=input("Enter course name:")
    self.courses.append((cid,name))
def inputMarksCourses(self):
    cid=input("Enter course ID to input marks for:")
    correct=((c for c in self.course if c.cid==cid),None)
    if not correct:
        print("course unknown")
        return
    if cid not in self.marks:
        self.marks[cid]={}
        for i in self.students:
            try:
                mark = float(input(f"Enter mark for student {i.student_id}: "))
                self.marks[cid][i.student_id] = mark
            except ValueError:
                print("Invalid mark entered. Skipping this student.")
def outputCourseList(self):
    print("Courses:")
    for j in self.courses:
        print(j)
def outputStudentList(self):
    print("Students:")
    for k in self.students:
        print(k)
def outputStudentMarks(self):
    cid=input("Enter course ID to view marks:")
    if cid not in self.marks:
        print("No marks found for this course!")
        return
    print(f"Marks for course {cid}:")
    for student_id,mark in self.marks[cid].items():
        print(f"Student ID:{student_id},Mark:{mark}")

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
            Ultra.input_marks_for_course()
        elif choice == "2":
            Ultra.output_course_list()
        elif choice == "3":
            Ultra.output_student_list()
        elif choice == "4":
            Ultra.output_student_marks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

