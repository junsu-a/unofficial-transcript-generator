class Course:
    def __init__(self, term, code, credit, title, num_grade, letter_grade, class_size, class_average):
        self.term = term
        self.code = code
        self.credit = credit
        self.title = title
        self.num_grade = num_grade
        self.letter_grade = letter_grade
        self.class_size = class_size
        self.class_average = class_average

    def __str__(self):
        return "Term: {} Code: {} Credit: {} Title: {} Numeric Grade: {} Letter Grade: {} Class Size: {} Class Average: {}".format(
            self.term, self.code, self.credit, self.title, self.num_grade, self.letter_grade, self.class_size, self.class_average
        )
