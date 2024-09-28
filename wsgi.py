import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from datetime import datetime

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )

app = create_app()
migrate = get_migrate(app)
#-------------- SIR ---------------
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

user_cli = AppGroup('user', help='User object commands')

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli)

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)

from App.controllers.course_controller import CourseController
from App.controllers.staff_controller import StaffController
from App.controllers.staff_allocation_controller import StaffAllocationController

import click
#-----------------------------

# Command 1: Create a Course
@app.cli.command("create-course", help="Creates a new course")
@click.argument("course_name")
@click.argument("course_description")
def create_course_command(course_name, course_description):
    try:
        course = CourseController.create_course(course_name, course_description)
        print(f"Course '{course.course_name}' created with ID '{course.course_id}'!")
    except ValueError as e:
        print(e)



# Command 2: List All Courses
@app.cli.command("list-courses", help="Lists all available courses")
def list_courses_command():
    courses = CourseController.view_all_courses()
    for course in courses:
        print(course.get_json())

# Command 3: Update a Course
@app.cli.command("update-course", help="Updates an existing course")
@click.argument("course_id")
@click.argument("course_name", required=False)
@click.argument("course_description", required=False)
def update_course_command(course_id, course_name=None, course_description=None):
    course = CourseController.update_course(course_id, course_name, course_description)
    if course:
        print(f"Course '{course_id}' updated successfully!")
    else:
        print(f"Course with ID '{course_id}' not found.")

# Command 4: Delete a Course
@app.cli.command("delete-course", help="Deletes a course by ID")
@click.argument("course_id")
def delete_course_command(course_id):
    if CourseController.delete_course(course_id):
        print(f"Course '{course_id}' deleted successfully!")
    else:
        print(f"Course with ID '{course_id}' not found.")

# Command 5: Create a Staff Member
@app.cli.command("create-staff", help="Creates a new staff member")
@click.argument("name")
@click.argument("role")
def create_staff_command(name, role):
    staff = StaffController.create_staff(name, role)
    print(f'Staff member {staff.name} created with ID {staff.staff_id}!')


# Command 6: List All Staff Members
@app.cli.command("list-staff", help="Lists all staff members")
def list_staff_command():
    staff_list = StaffController.view_all_staff()
    for staff in staff_list:
        print(staff.get_json())

# Command 7: Update a Staff Member
@app.cli.command("update-staff", help="Updates an existing staff member")
@click.argument("staff_id")
@click.argument("name", required=False)
@click.argument("role", required=False)
def update_staff_command(staff_id, name=None, role=None):
    staff = StaffController.update_staff(staff_id, name, role)
    if staff:
        print(f"Staff '{staff_id}' updated successfully!")
    else:
        print(f"Staff with ID '{staff_id}' not found.")

# Command 8: Delete a Staff Member
@app.cli.command("delete-staff", help="Deletes a staff member by ID")
@click.argument("staff_id")
def delete_staff_command(staff_id):
    if StaffController.delete_staff(staff_id):
        print(f"Staff '{staff_id}' deleted successfully!")
    else:
        print(f"Staff with ID '{staff_id}' not found.")

# Command 9: Assign Staff to a Course
@app.cli.command("assign-staff", help="Assigns a staff member to a course")
@click.argument("staff_id")
@click.argument("course_id")
def assign_staff_command(staff_id, course_id):
    allocation = StaffAllocationController.assign_staff(staff_id, course_id)
    print(f"Staff '{staff_id}' assigned to course '{course_id}' successfully!")

# Command 10: View Staff Allocations for a Course
@app.cli.command("view-staff-allocations", help="Displays all staff assigned to a course")
@click.argument("course_id")
def view_staff_allocations_command(course_id):
    allocations = StaffAllocationController.view_course_staff(course_id)
    if allocations:
        for allocation in allocations:
            print(allocation.get_json())
    else:
        print(f"No staff assigned to course '{course_id}'")

