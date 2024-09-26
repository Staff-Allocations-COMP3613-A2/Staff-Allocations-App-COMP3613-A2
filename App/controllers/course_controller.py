from App.models.course import Course
from App.database import db

class CourseController:
    def create_course(course_id, course_name, course_description):
        course = Course(course_id, course_name, course_description)
        db.session.add(course)
        db.session.commit()
        return course

    def view_all_courses():
        return Course.query.all()

    
    def update_course(course_id, course_name=None, course_description=None):
        course = Course.query.get(course_id)
        if course:
            if course_name:
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