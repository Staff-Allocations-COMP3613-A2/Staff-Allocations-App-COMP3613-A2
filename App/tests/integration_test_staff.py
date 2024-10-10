import pytest
from App.main import create_app
from App.database import db
from App.models import Staff  # Import the Staff model
from App.controllers import StaffController  # Import the StaffController for handling staff operations

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

def test_create_staff(test_app):
    with test_app.app_context():
        # Create a new staff member
        name = "John Doe"
        role = "Instructor"
        staff = StaffController.create_staff(name, role)

        # Validate staff member creation
        assert staff is not None, "Staff creation failed, staff is None"
        assert staff.name == name, f"Expected name: {name}, but got {staff.name}"
        assert staff.role == role, f"Expected role: {role}, but got {staff.role}"
        assert isinstance(staff.staff_id, int), f"Expected staff_id to be an integer, but got {type(staff.staff_id)}"
        
        # Ensure the staff member is saved in the database
        retrieved_staff = Staff.query.get(staff.staff_id)
        assert retrieved_staff is not None, f"Retrieved staff is None, expected to find staff with ID {staff.staff_id}"
        assert retrieved_staff.name == name, f"Retrieved staff name mismatch. Expected: {name}, Found: {retrieved_staff.name}"
        assert retrieved_staff.role == role, f"Retrieved staff role mismatch. Expected: {role}, Found: {retrieved_staff.role}"

def test_update_staff(test_app):
    with test_app.app_context():
        # Create a staff member to update
        staff = StaffController.create_staff("John Doe", "Instructor")
        
        # Update staff details
        updated_name = "Jane Doe"
        updated_role = "Head of Department"
        updated_staff = StaffController.update_staff(staff.staff_id, name=updated_name, role=updated_role)
        
        # Validate staff update
        assert updated_staff is not None, "Staff update failed, returned None"
        assert updated_staff.name == updated_name, f"Expected name: {updated_name}, but got {updated_staff.name}"
        assert updated_staff.role == updated_role, f"Expected role: {updated_role}, but got {updated_staff.role}"

        # Test updating a non-existent staff ID
        assert StaffController.update_staff(9999, name="New Name") is None, "Expected None for invalid staff ID"  # Should return None for invalid ID

def test_delete_staff(test_app):
    with test_app.app_context():
        # Create a staff member to delete
        staff = StaffController.create_staff("John Doe", "Instructor")
        
        # Delete the staff member
        result = StaffController.delete_staff(staff.staff_id)
        
        # Validate staff member deletion
        assert result is True, "Staff deletion failed, expected True but got False"
        assert Staff.query.get(staff.staff_id) is None, f"Staff with ID {staff.staff_id} still exists after deletion"
        
        # Test deleting a non-existent staff ID
        assert StaffController.delete_staff(9999) is False, "Expected False for invalid staff ID"  # Should return False for invalid ID
