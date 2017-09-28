from db.staffDB import StaffDB
from db.authorizationDB import AuthorizationDB


class Bootstrap:

    @staticmethod
    def init():
        staff_obj = {
            'staffId': 'toffs',
            'name': 'Ogungbaigbe Tofunmi',
            'department': 'Procurement',
            'phoneNumber': '08167494821',
            'isSecurityStaff': True,
        }

        StaffDB.new_staff(staff_obj)

        auth_object = {
            'staffId': 'tofunmi',
            'password': 'tofunmi'
        }

        AuthorizationDB.new_authorization(auth_object)

        staff_obj = {
            'staffId': 'gbemi',
            'name': 'Gbemi Falade',
            'department': 'Sales',
            'phoneNumber': '08167494821',
            'isSecurityStaff': False,
        }

        StaffDB.new_staff(staff_obj)

        auth_object = {
            'staffId': 'gbemi',
            'password': 'gbemi'
        }

        AuthorizationDB.new_authorization(auth_object)