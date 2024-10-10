from flask import Blueprint, request, jsonify
from App.controllers.staff_controller import StaffController

staff_bp = Blueprint('staff', __name__)

@staff_bp.route('/api/staff', methods=['GET'])
def get_staff():
    staff = StaffController.view_all_staff()
    return jsonify([member.get_json() for member in staff]), 200

@staff_bp.route('/api/staff', methods=['POST'])
def create_staff():
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    try:
        staff_member = StaffController.create_staff(name, role)
        return jsonify({'name': staff_member.name, 'Role': staff_member.role}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@staff_bp.route('/api/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    data = request.get_json()
    name = data.get('name')
    role = data.get('role')
    try:
        staff_member = StaffController.update_staff(staff_id, name, role)
        if staff_member:
            return jsonify(staff_member.get_json()), 200
        return jsonify({"error": "Staff not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@staff_bp.route('/api/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    if StaffController.delete_staff(staff_id):
        return jsonify({"message": "Staff deleted successfully"}), 200
    return jsonify({"error": "Staff not found"}), 404
