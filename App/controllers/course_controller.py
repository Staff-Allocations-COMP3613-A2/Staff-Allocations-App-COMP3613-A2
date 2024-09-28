from App.models.course import Course
from App.database import db

class CourseController:
    def create_course(course_name, course_description):
        existing_course = Course.query.filter_by(course_name=course_name).first()
        if existing_course:
            raise ValueError(f"A course with the name '{course_name}' already exists.")

        course = Course(course_name, course_description)
        db.session.add(course)
        db.session.commit()
        return course

    def view_all_courses():
        return Course.query.all()

    
    def update_course(course_id, course_name=None, course_description=None):
        course = Course.query.get(course_id)
        if course:
            if course_name:
                existing_course = Course.query.filter_by(course_name=course_name).first()
                if existing_course and existing_course.course_id != course_id:
                    raise ValueError(f"A course with the name '{course_name}' already exists.")
                course.course_name = course_name
            if course_description:
                course.course_description = course_description
            db.session.commit()
            return course
        return None

    
    def delete_course(course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()
            return True
        return False