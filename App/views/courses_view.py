from flask import Blueprint, request, jsonify
from App.controllers.course_controller import CourseController

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/api/courses', methods=['GET'])
def get_courses():
    courses = CourseController.view_all_courses()
    return jsonify([course.get_json() for course in courses]), 200

@courses_bp.route('/api/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    course_name = data.get('course_name')
    course_description = data.get('course_description')
    try:
        course = CourseController.create_course(course_name, course_description)
        return jsonify(course.get_json()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@courses_bp.route('/api/courses/<course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    course_name = data.get('course_name')
    course_description = data.get('course_description')
    try:
        course = CourseController.update_course(course_id, course_name, course_description)
        if course:
            return jsonify(course.get_json()), 200
        return jsonify({"error": "Course not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@courses_bp.route('/api/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    if CourseController.delete_course(course_id):
        return jsonify({"message": "Course deleted successfully"}), 200
    return jsonify({"error": "Course not found"}), 404
