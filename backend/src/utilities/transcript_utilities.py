from .course_utilities import Course

class Transcript:
    def __init__(self, student_surname, student_given_name, student_number):
        self.student_surname = student_surname
        self.student_given_name = student_given_name
        self.student_number = student_number
        self.sessions = {}

    def __str__(self):
        return "Student Name: {} {}\nStudent Number: {}\nSessions: {}" \
            .format(self.student_given_name, self.student_surname, self.student_number, self.sessions)

    def add_course(self, session: str, course: Course):
        if session in self.sessions:
            self.sessions[session].append(course)
        else:
            self.sessions[session] = [course]
