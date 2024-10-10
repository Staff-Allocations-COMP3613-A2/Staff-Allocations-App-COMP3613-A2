import pytest
from App.main import create_app
from App.database import db
from App.models import Course
from App.controllers import CourseController

@pytest.fixture(scope='function')
def test_app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.session.remove()
        db.drop_all()  # Clean up after tests

def test_create_course(test_app):
    with test_app.app_context():
        # Create a new course
        course_name = "Mathematics 101"
        course_description = "An introductory course in mathematics"
        course = CourseController.create_course(course_name, course_description)
        
        # Validate course creation
        assert course is not None, "Course creation failed, course is None"
        assert course.course_name == course_name, f"Expected course name: {course_name}, but got {course.course_name}"
        assert course.course_description == course_description, f"Expected description: {course_description}, but got {course.course_description}"
        assert isinstance(course.course_id, str), f"Expected course ID to be an integer, but got {type(course.course_id)}"
        
        # Ensure the course is saved in the database
        retrieved_course = Course.query.get(course.course_id)
        assert retrieved_course is not None, f"Retrieved course is None, expected to find course with ID {course.course_id}"
        assert retrieved_course.course_name == course_name, f"Retrieved course name mismatch. Expected: {course_name}, Found: {retrieved_course.course_name}"
        assert retrieved_course.course_description == course_description, f"Retrieved course description mismatch. Expected: {course_description}, Found: {retrieved_course.course_description}"

def test_update_course(test_app):
    with test_app.app_context():
        # Create a course to update
        course = CourseController.create_course("Mathematics 101", "An introductory course in mathematics")
        
        # Update course details
        updated_name = "Mathematics 102"
        updated_description = "A more advanced course in mathematics"
        updated_course = CourseController.update_course(course.course_id, course_name=updated_name, course_description=updated_description)
        
        # Validate course update
        assert updated_course is not None
        assert updated_course.course_name == updated_name
        assert updated_course.course_description == updated_description

        # Test updating a non-existent course ID
        assert CourseController.update_course(9999, course_name="New Name") is None  # Should return None for invalid ID

def test_delete_course(test_app):
    with test_app.app_context():
        # Create a course to delete
        course = CourseController.create_course("Physics 101", "An introductory course in physics")
        
        # Delete the course
        result = CourseController.delete_course(course.course_id)
        
        # Validate course deletion
        assert result is True
        assert Course.query.get(course.course_id) is None  # Course should not exist in DB after deletion

        # Test deleting a non-existent course ID
        assert CourseController.delete_course(9999) is False  # Should return False for invalid ID
