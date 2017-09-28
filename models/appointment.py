class Appointment:
    def __init__(self, _id, staff_id, visitor_id, subject_of_visit, date_time, status):
        self.id = _id
        self.staff_id = staff_id
        self.visitor_id = visitor_id
        self.subject = subject_of_visit
        self.date_time = date_time
        self.status = status

        self.staff = {}
        self.visitor = {}
        self.unresolved_info = {}

    def set_staff(self, staff):
        self.staff = staff

    def set_visitor(self, visitor):
        self.visitor = visitor

    def set_unresolved_info(self, unresolved_info):
        self.unresolved_info = unresolved_info

    @property
    def serialize(self):
        return {
            'id': self.id,
            'staffId': self.staff_id,
            'visitorId': self.visitor_id,
            'subject': self.subject,
            'dateTime': self.date_time,
            'status': self.status,
            'staff': self.staff,
            'visitor': self.visitor.serialize,
            'unresolvedInfo': self.unresolved_info
        }
