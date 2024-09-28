from App.models.staff import Staff
from App.models.course import Course
from App.models.staff_allocation import StaffAllocation
from App import db


class StaffAllocationController:
    def assign_staff(staff_id, course_id):
        staff = Staff.query.get(staff_id)
        course = Course.query.get(course_id)
        if not staff:
            raise ValueError(f"Staff with ID '{staff_id}' does not exist.")
        if not course:
            raise ValueError(f"Course with ID '{course_id}' does not exist.")

        existing_allocation = StaffAllocation.query.filter_by(staff_id=staff_id, course_id=course_id).first()
        if existing_allocation:
            raise ValueError(f"Staff with ID '{staff_id}' is already assigned to course '{course_id}'.")

        allocation = StaffAllocation(staff_id, course_id)
        db.session.add(allocation)
        db.session.commit()
        return allocation

    def view_course_staff(course_id):
        return StaffAllocation.query.filter_by(course_id=course_id).all()