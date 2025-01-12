import math
import numpy as np
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

class Ultra:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def inputNumStudent(self):
        return int(input(Fore.WHITE + "Enter the number of students: "))

    def inputNumCourse(self):
        return int(input(Fore.WHITE + "Enter the number of courses: "))

    def inputInfoStudent(self):
        sid = input(Fore.WHITE + "Enter student's ID: ")
        name = input(Fore.WHITE + "Enter student's name: ")
        dob = input(Fore.WHITE + "Enter student's date of birth: ")
        self.students.append(Student(sid, name, dob))

    def inputInfoCourse(self):
        cid = input(Fore.WHITE + "Enter course's ID: ")
        name = input(Fore.WHITE + "Enter course's name: ")
        credit = int(input(Fore.WHITE + "Enter course's credit: "))
        self.courses.append(Course(cid, name, credit))

    def inputMarksCourse(self):
        cid = input(Fore.WHITE + "Enter course ID for input: ")
        for course in self.courses:
            if course.cid == cid:
                break
        else:
            print(Fore.WHITE + "Course unknown")
            return
        if cid not in self.marks:
            self.marks[cid] = {}
        for student in self.students:
            try:
                mark = float(input(Fore.WHITE + f"Enter mark for student {student.sid}: "))
                self.marks[cid][student.sid] = mark
            except ValueError:
                print(Fore.WHITE + "Invalid mark. Skipping this student.")

    def outputCourseList(self):
        print(Fore.WHITE + "\nCourses List:")
        for course in self.courses:
            print(course)

    def outputStudentList(self):
        print(Fore.WHITE + "\nStudents List:")
        for student in self.students:
            print(student)

    def outputStudentMarks(self):
        cid = input(Fore.WHITE + "Enter course ID for output: ")
        if cid not in self.marks:
            print(Fore.WHITE + "Course unknown.")
            return
        print(Fore.WHITE + f"Marks for course {cid}:")
        for sid, mark in self.marks[cid].items():
            print(Fore.WHITE + f"Student's ID: {sid}, Mark: {mark}")

    def calculateGPA(self, sid):
        totalCredit = 0
        weightedMark = 0
        for student in self.students:
            if student.sid == sid:
                break
        else:
            print(Fore.WHITE + f"Student ID {sid} unknown")
            return

        for course in self.courses:
            if sid in self.marks.get(course.cid, {}):
                mark = self.marks[course.cid][sid]
                credit = course.credit
                weightedMark += mark * credit
                totalCredit += credit

        if totalCredit == 0:
            return 0
        return weightedMark / totalCredit

    def sortGPA(self):
        GPA = []
        for student in self.students:
            gpa = self.calculateGPA(student.sid)
            GPA.append((student.sid, gpa))
        GPA.sort(key=lambda x: x[1], reverse=True)
        print(Fore.WHITE + "\nSorted GPA (Descending):")
        for sid, gpa in GPA:
            print(Fore.WHITE + f"Student ID: {sid}, GPA: {gpa}")


class Student:
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, DOB: {self.dob}"


class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.cid}, Name: {self.name}, Credit: {self.credit}"


if __name__ == "__main__":
    ultra = Ultra()

    num_students = ultra.inputNumStudent()
    for _ in range(num_students):
        ultra.inputInfoStudent()

    num_courses = ultra.inputNumCourse()
    for _ in range(num_courses):
        ultra.inputInfoCourse()

    while True:
        print(Fore.WHITE + "\nOptions:")
        print(Back.BLACK + Fore.WHITE + "1. Input marks for a course")
        print(Back.BLACK + Fore.WHITE + "2. View courses")
        print(Back.BLACK + Fore.WHITE + "3. View students")
        print(Back.BLACK + Fore.WHITE + "4. View marks for a course")
        print(Back.BLACK + Fore.WHITE + "5. View GPA (Sorted by GPA descending)")
        print(Back.BLACK + Fore.WHITE + "6. Exit")

        choice = input(Fore.WHITE + "Choose an option: ")

        if choice == "1":
            ultra.inputMarksCourse()
        elif choice == "2":
            ultra.outputCourseList()
        elif choice == "3":
            ultra.outputStudentList()
        elif choice == "4":
            ultra.outputStudentMarks()
        elif choice == "5":
            ultra.sortGPA()
        elif choice == "6":
            break
        else:
            print(Fore.WHITE + "Invalid choice. Please try again.")
