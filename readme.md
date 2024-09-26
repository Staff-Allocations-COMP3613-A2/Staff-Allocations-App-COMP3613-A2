# Staff Allocations App - CLI Commands

This document contains all the CLI commands available in the Staff Allocations App.

## 1. Create a Course
Command:
```bash
flask create-course <course_id> <course_name> [course_description]
```
Description:  
Creates a new course with the specified `course_id`, `course_name`, and an optional `course_description`.

Example:
```bash
flask create-course cs101 "Intro to Computer Science" "Basics of computer science and programming"
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
Updates the name and/or description of the course with the specified `course_id`. You can update the course name or description by leaving the other argument blank.

Example:
```bash
flask update-course cs101 "Introduction to CS"  # Only update the name
flask update-course cs101 "" "Introduction to Computer Science"  # Only update the description
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
flask delete-course cs101
```

---

## 5. Create a Staff Member
Command:
```bash
flask create-staff <staff_id> <name> <role>
```
Description: 
Creates a new staff member with the given `staff_id`, `name`, and `role` (e.g., Lecturer, Teaching Assistant, etc.).

Example:
```bash
flask create-staff 1 "Alice Smith" "Lecturer"
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
Assigns the staff member with the specified `staff_id` to the course with the specified `course_id`. Staff can be assigned to multiple courses.

Example:
```bash
flask assign-staff 1 cs101
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
flask view-staff-allocations cs101
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

### Conclusion

This document lists all available commands for managing courses, staff, and staff allocations within the Staff Allocations App. Each command can be used in a terminal or command-line interface that supports Flask CLI commands.

---