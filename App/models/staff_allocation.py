from App.database import db

class StaffAllocation(db.Model):
    __tablename__ = 'staff_allocation'

    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), primary_key=True)
    course_id = db.Column(db.String(10), db.ForeignKey('course.course_id'), primary_key=True)

    staff = db.relationship('Staff', backref=db.backref('allocations', cascade='all, delete-orphan'))
    course = db.relationship('Course', backref=db.backref('allocations', cascade='all, delete-orphan'))

    def __init__(self, staff_id, course_id):
        self.staff_id = staff_id
        self.course_id = course_id

    def get_json(self):
        return {
            'Staff ID': self.staff_id,
            'Course ID': self.course_id,
            'Staff Member Name': self.staff.name,
            'Course Name': self.course.course_name
        }
