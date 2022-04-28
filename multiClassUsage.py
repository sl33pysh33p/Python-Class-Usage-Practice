class Student:

    """
    Creates the Student class
    """

    def __init__(self, name, age, grade):
        """
        upon student class being called fetch the args of: Name, Age and Grade.
        """

        self.name = name
        self.age = age
        self.grade = grade

    def getName(self):
        # gets name from __init__ function
        return self.name

    def getAge(self):
        # gets age from __init__ function
        return self.age

    def getGrade(self):
        # gets grade from __init__ function
        return self.grade

    def getAll(self):
        # gets all data from __init__ function
        return self.name, self.age, self.grade


class Course:
    """
    Creates Course class
    """

    def __init__(self, course, maxStudents):
        """
        Upon Course class being called, fetch the args of course and maxStudents

        Args:
            course (String): What course?
            maxStudents (Integer): What is the maximum ammount of students in that course
        """
        self.course = course
        self.maxStudents = maxStudents
        self.classList = []

    def addToCourse(self, addStudent):
        """
        addToCourse function is used to add students to the classList array and check if there is enough
        space in the course for them to be added

        Args:
            addStudent: Which student should be added to the classList array

        """
        if len(self.classList) < self.maxStudents:
            self.classList.append(addStudent)
            print("Student added!")
        else:
            print("Student not added!")
        """
        checks if there is space in the course for the student to be added
        """


s1 = Student("Tom", 16, 87)
s2 = Student("Darcy", 16, 85)

course1 = Course("Science", 2)

course1.addToCourse(s1)
course1.addToCourse(s2)


print(course1.classList[0].name)
print(course1.classList[1].name)
