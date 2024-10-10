**IMPLEMENTATION TESTING** 

---

## Postman API Testing

To facilitate API testing for the Staff Allocations App, a Postman collection has been prepared. The collection contains pre-built requests for all major endpoints, including user authentication, course management, staff management, and staff allocations.

### Tested Collection Package:
The tested collection package , `Staff_Allocation_API_Collection.postman_test_run.json`, has been uploaded to the repository.

### Postman Collection Link:
You can also access the Postman collection directly via the following link:

[Staff Allocations API Postman Collection](https://www.postman.com/tramdeo816034662/workspace/staff-allocations-api-testing/collection/33339653-cd129fa5-485e-437b-ba77-23b8be33ff62?action=share&creator=33339653&active-environment=33339653-3547a9b0-c024-4a10-93ed-b816c0f59a13)

This collection includes all the necessary API requests to test the application's functionality through Postman, allowing you to interact with the API in a structured way.

---

Here’s an updated section for your `README.md` on how Integration Tests and Unit Tests were implemented and handled:

---

## Testing

### Unit Tests
Unit tests are designed to test individual components of the application in isolation. The tests for the application cover the following functionalities:

- **User Management**: Tests for creating, authenticating, updating, and retrieving users.
- **Staff Management**: Tests for creating, updating, deleting, and retrieving staff members.
- **Course Management**: Tests for creating, updating, and deleting courses.
- **Staff Allocation**: Tests for assigning staff to courses and viewing allocated staff.

Each test case ensures that the respective functions behave as expected, verifying the correctness of both input and output.

### Integration Tests
Integration tests check the interaction between different components of the application. These tests focus on the following aspects:

- **Database Interactions**: Validating that the application properly creates, updates, and deletes records in the database.
- **Functionality Workflow**: Ensuring that the different controllers and models work together seamlessly, such as user authentication and staff allocation processes.

The integration tests use an in-memory SQLite database, allowing for fast execution without affecting the production database. Each test runs within a test context, where the database is set up and torn down before and after each test.

### Running the Tests
To run the tests in the terminal, execute the following command:

```bash
pytest App/tests/
```

This command will discover and run all tests in the `App/tests/` directory, providing a summary of passed and failed tests.

---


---

Staff Allocations App - CLI Commands

This document contains all the CLI commands available in the Staff Allocations App.

---
Initital commands
---

## Create a New User for the Staff Allocations App
Command:
```bash
flask create-user <username> <password>
```
Description:  
Creates a new user with the given `username` and `password` for the app.

Example:
```bash
flask create-user "admin" "password123"
```

---

## Log In a User
Command:
```bash
flask login <username> <password>
```
Description:  
Logs in a user with the specified `username` and `password`.

Example:
```bash
flask login "admin" "password123"
```



# Main Functionalities of Staff Allocations App

## 1. Create a Course
Command:
```bash
flask create-course <course_name> <course_description>
```
Description:  
Creates a new course with the specified `course_name` and `course_description`.

Example:
```bash
flask create-course "Intro to Computer Science" "Basics of computer science and programming"
```

---

## 2. View All Courses
Command:
```bash
flask list-courses
```
Description:  
Lists all courses currently stored in the database.

Example:
```bash
flask list-courses
```

---

## 3. Update a Course
Command:
```bash
flask update-course <course_id> [course_name] [course_description]
```
Description:  
Updates the name and/or description of the course with the specified `course_id`. You can update the course name or description by leaving one of the arguments blank.

Example:
```bash
flask update-course "FST10001" "Introduction to CS"  # Only update the name
flask update-course "FST10001" "" "Introduction to Computer Science"  # Only update the description
```

---

## 4. Delete a Course
Command:
```bash
flask delete-course <course_id>
```
Description:
Deletes the course with the specified `course_id` from the database.

Example:
```bash
flask delete-course "FST1"
```

---

## 5. Create a Staff Member
Command:
```bash
flask create-staff <name> <role>
```
Description: 
Creates a new staff member with the given `name` and `role` (e.g., Lecturer, Teaching Assistant, etc.).

Example:
```bash
flask create-staff "Alice Smith" "Lecturer"
```

---

## 6. View All Staff
Command:
```bash
flask list-staff
```
Description:  
Lists all staff members currently stored in the database.

Example:
```bash
flask list-staff
```

---

## 7. Update a Staff Member
Command:
```bash
flask update-staff <staff_id> [name] [role]
```
Description:  
Updates the name and/or role of the staff member with the specified `staff_id`. You can choose to update only one attribute by leaving the other blank.

Example:
```bash
flask update-staff 1 "Alice Cooper"  # Only update name
flask update-staff 1 "" "Senior Lecturer"  # Only update role
```

---

## 8. Delete a Staff Member
Command:
```bash
flask delete-staff <staff_id>
```
Description:  
Deletes the staff member with the specified `staff_id` from the database.

Example:
```bash
flask delete-staff 1
```

---

## 9. Assign Staff to a Course
Command:
```bash
flask assign-staff <staff_id> <course_id>
```
Description:  
Assigns the staff member with the specified `staff_id` to the course with the specified `course_id`. Each staff member can only be assigned once to a course.

Example:
```bash
flask assign-staff 1 "FST1"
```

---

## 10. View Staff Allocations for a Course
Command:
```bash
flask view-staff-allocations <course_id>
```
Description:  
Displays all staff members assigned to the course with the specified `course_id`. Prints the details of each assignment.

Example:
```bash
flask view-staff-allocations "FST1"
```

---

## 11. View Help for All CLI Commands
Command:
```bash
flask --help
```
Description:  
Lists all available CLI commands with descriptions.

---
