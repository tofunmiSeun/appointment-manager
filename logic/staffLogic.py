from db.staffDB import StaffDB


class StaffLogic:

    @staticmethod
    def get_staff_details_all():
        return StaffDB.get_staff_details_all()
