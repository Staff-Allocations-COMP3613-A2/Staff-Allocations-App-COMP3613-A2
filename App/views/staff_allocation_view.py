from flask import Blueprint, request, jsonify
from App.controllers.staff_allocation_controller import StaffAllocationController

staff_allocation_bp = Blueprint('staff_allocation', __name__)

@staff_allocation_bp.route('/api/staff_allocation', methods=['POST'])
def assign_staff():
    data = request.get_json()
    staff_id = data.get('staff_id')
    course_id = data.get('course_id')
    try:
        allocation = StaffAllocationController.assign_staff(staff_id, course_id)
        return jsonify(allocation.get_json()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@staff_allocation_bp.route('/api/courses/<course_id>/staff', methods=['GET'])
def get_course_staff(course_id):
    staff = StaffAllocationController.view_course_staff(course_id)
    return jsonify([allocation.get_json() for allocation in staff]), 200
