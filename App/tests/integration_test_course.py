import pytest
from App.main import create_app
from App.database import db
from App.models import Course
from App.controllers import CourseController

@pytest.fixture(scope='module')
def test_app():
    # Setup your application and database here
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Clean up after tests

def test_create_course(test_app):
    with test_app.app_context():
        course = CourseController.create_course("Math 101", "Basic Mathematics")
        assert course.course_id.startswith("FST")
        assert course.course_name == "Math 101"

def test_update_course(test_app):
    with test_app.app_context():
        # Create a unique course for the update test
        course = CourseController.create_course("Math 102", "Basic Mathematics")
        updated_course = CourseController.update_course(course.course_id, course_name="Advanced Math 102")
        assert updated_course.course_name == "Advanced Math 102"

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

