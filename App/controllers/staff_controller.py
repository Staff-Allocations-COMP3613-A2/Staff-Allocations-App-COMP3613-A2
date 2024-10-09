from App.models.staff import Staff
from App.database import db

class StaffController:
    @staticmethod
    def create_staff(name, role):
        try:
            staff = Staff(name, role)
            db.session.add(staff)
            db.session.commit()
            return staff
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def view_all_staff():
        return Staff.query.all()

    @staticmethod
    def update_staff(staff_id, name=None, role=None):
        try:
            staff = Staff.query.get(staff_id)
            if staff:
                if name:
                    staff.name = name
                if role:
                    staff.role = role
                db.session.commit()
                return staff
            return None
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_staff(staff_id):
        try:
            staff = Staff.query.get(staff_id)
            if staff:
                db.session.delete(staff)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e
