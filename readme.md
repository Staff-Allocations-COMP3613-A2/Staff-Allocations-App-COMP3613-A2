---

Staff Allocations App - CLI Commands

This document contains all the CLI commands available in the Staff Allocations App.

---

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
