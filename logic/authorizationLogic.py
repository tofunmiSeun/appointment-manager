from db.authorizationDB import AuthorizationDB
from db.staffDB import StaffDB


class AuthorizationLogic:

    @staticmethod
    def authorize(request_object):
        staff_id = request_object['userId']
        password = request_object['password']

        if AuthorizationDB.authorize(staff_id, password):
            staff = StaffDB.get_staff_by_id(staff_id)
            return staff

        else:
            raise Exception('Invalid login credentials')
