class Staff:
    def __init__(self, staff_id, name, department, phone_number, is_security_staff):
        self.id = staff_id
        self.name = name
        self.department = department
        self.phone_number = phone_number
        self.is_security_staff = is_security_staff

    @property
    def serialize(self):
        return {
            'staffId': self.id,
            'name': self.name,
            'department': self.department,
            'phoneNumber': self.phone_number,
            'isSecurityStaff': self.is_security_staff
        }
