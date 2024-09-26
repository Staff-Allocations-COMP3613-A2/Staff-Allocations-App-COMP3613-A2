from App.models.staff_allocation import StaffAllocation
from App.database import db

class StaffAllocationController:
    def assign_staff(staff_id, course_id):
        staff_allocation = StaffAllocation(staff_id, course_id)
        db.session.add(staff_allocation)
        db.session.commit()
        return staff_allocation

    def view_course_staff(course_id):
        return StaffAllocation.query.filter_by(course_id=course_id).all()