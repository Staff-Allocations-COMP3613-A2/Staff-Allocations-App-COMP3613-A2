from App.database import db

class StaffAllocation(db.Model):
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), primary_key=True)
    course_id = db.Column(db.String(100), db.ForeignKey('course.course_id'), primary_key=True)

    def __init__(self, staff_id, course_id):
        self.staff_id = staff_id
        self.course_id = course_id

    def get_json(self):
        return{
        'Staff ID': self.staff_id,
        'Course ID': self.course_id
        }