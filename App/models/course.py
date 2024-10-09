from App.database import db

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.String(10), primary_key=True)
    course_name = db.Column(db.String(100), nullable=False, unique=True)
    course_description = db.Column(db.String(200), nullable=False)

    def __init__(self, course_name, course_description):
        self.course_name = course_name
        self.course_description = course_description
        self.course_id = self.generate_course_id()

    @classmethod
    def generate_course_id(cls):
        last_course = cls.query.order_by(cls.course_id.desc()).first()
        if last_course:
            last_id_num = int(last_course.course_id.replace('FST', ''))
            new_id_num = last_id_num + 1
        else:
            new_id_num = 1
        return f"FST{new_id_num}"

    def get_json(self):
        return {
            'Course ID': self.course_id,
            'Course Name': self.course_name,
            'Course Description': self.course_description
        }
