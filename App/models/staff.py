from App.database import db

class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    def get_json(self):
        return{
        'Staff ID': self.staff_id,
        'Staff Member Name': self.name,
        'Role': self.role
    }