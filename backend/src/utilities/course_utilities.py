class Course:
    def __init__(self, session, section, term, subject, code, credit, title, num_grade, letter_grade, average, year, standing):
        self.session = session
        self.section = section 
        self.term = term 
        self.subject = subject 
        self.code = code 
        self.credit = credit 
        self.title = title 
        self.num_grade = num_grade 
        self.letter_grade = letter_grade 
        # self.class_size = class_size # Tricky to get this data while possible, but not so important
        self.average = average 
        self.year = year
        self.standing = standing

    def __str__(self):
        return "Term: {} Code: {} Credit: {} Title: {} Numeric Grade: {} Letter Grade: {} Average: {} Year: {} Standing: {}".format(
            self.term, self.code, self.credit, self.title, self.num_grade, self.letter_grade, self.average, self.year, self.standing
        )
