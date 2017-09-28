from db.staffDB import StaffDB
from db.authorizationDB import AuthorizationDB


class Bootstrap:

    @staticmethod
    def init():
        staff_obj = {
            'staffId': 'toffs',
            'name': 'Ogungbaigbe Tofunmi',
            'department': 'Procurement',
            'phoneNumber': '08167494821'
        }

        StaffDB.new_staff(staff_obj)

        auth_object = {
            'staffId': 'toffs',
            'password': 'spartans'
        }

        AuthorizationDB.new_authorization(auth_object)

