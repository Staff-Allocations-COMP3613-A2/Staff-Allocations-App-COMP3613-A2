import pytest
from App.models import User  # Import your User model
from App.database import db  # Import your database instance
from App.main import create_app
from App.database import db, create_db
from App.models import User
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,
    authenticate_user
)

@pytest.fixture(scope='module')
def test_app():
    # Setup your application and database here
    from App import create_app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
    with app.app_context():
        db.create_all()  # Create tables
        yield app
        db.drop_all()  # Clean up after tests

def test_create_user(test_app):
    with test_app.app_context():
        user = create_user("test_user", "test_password")
        assert user.username == "test_user"  # Check username
        assert user.set_password != "test_password"  # Ensure password is hashed
        assert User.query.filter_by(username="test_user").first() is not None  # User exists in DB

def test_authenticate_user(test_app):
    with test_app.app_context():
        # Ensure user exists only once
        existing_user = User.query.filter_by(username="test_user").first()
        if existing_user is None:
            create_user("test_user", "test_password")  # Create user if not exists

        # Test valid credentials
        assert authenticate_user("test_user", "test_password") is True
        
        # Test invalid credentials
        assert authenticate_user("test_user", "wrong_password") is False
        assert authenticate_user("wrong_user", "test_password") is False

def test_update_user():
    user = create_user("admin", "password123")
    update_user(user.id, "newadmin")
    updated_user = get_user(user.id)
    assert updated_user.username == "newadmin"
