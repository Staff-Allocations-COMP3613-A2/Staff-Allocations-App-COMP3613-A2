import pytest
from App.main import create_app
from App.database import db
from App.models import Staff, Course, StaffAllocation  # Import models for Staff, Course, and StaffAllocation
from App.controllers import StaffController, CourseController, StaffAllocationController  # Import the controllers

@pytest.fixture(scope='function')
def test_app():
    # Setup your application and database here
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.session.remove()
        db.drop_all()  # Clean up after each test

def test_assign_staff(test_app):
    with test_app.app_context():
        # Create a staff member and a course for the allocation
        staff = StaffController.create_staff("John Doe", "Instructor")
        course = CourseController.create_course("FST101", "Fundamentals of Science and Technology")

        # Assign the staff member to the course
        allocation = StaffAllocationController.assign_staff(staff.staff_id, course.course_id)

        # Validate the staff allocation
        assert allocation is not None, "Staff allocation failed, allocation is None"
        assert allocation.staff_id == staff.staff_id, f"Expected staff ID: {staff.staff_id}, but got {allocation.staff_id}"
        assert allocation.course_id == course.course_id, f"Expected course ID: {course.course_id}, but got {allocation.course_id}"

        # Ensure the allocation is saved in the database
        retrieved_allocation = StaffAllocation.query.filter_by(staff_id=staff.staff_id, course_id=course.course_id).first()
        assert retrieved_allocation is not None, "Allocation not found in database"
        assert retrieved_allocation.staff_id == staff.staff_id, f"Expected staff ID: {staff.staff_id}, but got {retrieved_allocation.staff_id}"
        assert retrieved_allocation.course_id == course.course_id, f"Expected course ID: {course.course_id}, but got {retrieved_allocation.course_id}"

def test_view_course_staff(test_app):
    with test_app.app_context():
        # Create a new course and assign multiple staff members
        course = CourseController.create_course("FST101", "Fundamentals of Science and Technology")

        # Create and assign staff members
        staff1 = StaffController.create_staff("John Doe", "Instructor")
        staff2 = StaffController.create_staff("Jane Smith", "Lecturer")
        StaffAllocationController.assign_staff(staff1.staff_id, course.course_id)
        StaffAllocationController.assign_staff(staff2.staff_id, course.course_id)

        # Retrieve and validate the list of staff members assigned to the course
        course_staff = StaffAllocationController.view_course_staff(course.course_id)
        assert len(course_staff) == 2, f"Expected 2 staff members, but got {len(course_staff)}"
        
        # Check if both staff members are correctly listed in the course's staff
        staff_ids = [staff.staff_id for staff in course_staff]
        assert staff1.staff_id in staff_ids, f"Staff member {staff1.name} not found in course staff list"
        assert staff2.staff_id in staff_ids, f"Staff member {staff2.name} not found in course staff list"
