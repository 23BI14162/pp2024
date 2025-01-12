class Ultra:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def inputNumStudent(self):
        return int(input("Enter the number of students: "))

    def inputNumCourse(self):
        return int(input("Enter the number of courses: "))

    def inputInfoStudent(self):
        sid = input("Enter student's ID: ")
        name = input("Enter student's name: ")
        dob = input("Enter student's date of birth: ")
        self.students.append(Student(sid, name, dob))

    def inputInfoCourse(self):
        cid = input("Enter course's ID: ")
        name = input("Enter course's name: ")
        self.courses.append(Course(cid, name))

    def inputMarksCourse(self):
        cid = input("Enter course ID for input: ")
        for course in self.courses:
            if course[0] == cid:
                break
        else:
            print("course unknown")
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
        print("Courses:")
        for course in self.courses:
            print(course)

    def outputStudentList(self):
        print("Students:")
        for student in self.students:
            print(student)

    def outputStudentMarks(self):
        cid = input("Enter course ID for output: ")
        if cid not in self.marks:
            print("Course unknown.")
            return
        print(f"Marks for course {cid}:")
        for sid, mark in self.marks[cid].items():
            print(f"Student's ID: {sid}, Mark: {mark}")


class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, DOB: {self.dob}"


class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name

    def __str__(self):
        return f"ID: {self.cid}, Name: {self.name}"


if __name__ == "__main__":
    ultra = Ultra()

    num_students = ultra.inputNumStudent()
    for _ in range(num_students):
        ultra.inputInfoStudent()

    num_courses = ultra.inputNumCourse()
    for _ in range(num_courses):
        ultra.inputInfoCourse()

    while True:
        print("\nOptions:")
        print("1. Input marks for a course")
        print("2. View courses")
        print("3. View students")
        print("4. View marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            ultra.inputMarksCourse()
        elif choice == "2":
            ultra.outputCourseList()
        elif choice == "3":
            ultra.outputStudentList()
        elif choice == "4":
            ultra.outputStudentMarks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
