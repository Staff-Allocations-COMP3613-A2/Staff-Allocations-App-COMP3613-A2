from App.models.staff import Staff
from App.database import db

class StaffController:
    def create_staff(name, role):
        staff = Staff(name, role)
        db.session.add(staff)
        db.session.commit()
        return staff

    
    def view_all_staff():
        return Staff.query.all()

    
    def update_staff(staff_id, name=None, role=None):
        staff = Staff.query.get(staff_id)
        if staff:
            if name:
                staff.name = name
            if role:
                staff.role = role
            db.session.commit()
            return staff
        return None

    def delete_staff(staff_id):
        staff = Staff.query.get(staff_id)
        if staff:
            db.session.delete(staff)
            db.session.commit()
            return True
        return False