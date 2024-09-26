from App.database import db

class Course(db.Model):
    course_id = db.Column(db.String(100), primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_description = db.Column(db.String(200), nullable=False)

    def __init__(self, course_id, course_name, course_description):
        self.course_id = course_id
        self.course_name = course_name
        self.course_description = course_description

    def get_json(self):
        return {
            'Course ID': self.course_id,
            'Course Name': self.course_name,
            'Course Description': self.course_description
        }
