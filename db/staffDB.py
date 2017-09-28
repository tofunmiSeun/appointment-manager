from pymongo import MongoClient
from bson.objectid import ObjectId
from models.staff import Staff
from utils.constant import Constant


class StaffDB:
    COLLECTION_NAME = 'staff'

    @staticmethod
    def new_staff(staff_object, is_security_staff=False):
        try:
            obj = {
                'staffId': staff_object['staffId'],
                'name': staff_object['name'],
                'department': staff_object['department'],
                'phoneNumber': staff_object['phoneNumber'],
                'isSecurityStaff': is_security_staff
            }

            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][StaffDB.COLLECTION_NAME]

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to add new staff')
            raise Exception('Could not add new staff to DB')

    @staticmethod
    def get_staff_by_id(staff_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][StaffDB.COLLECTION_NAME]

            staff_object = document.find_one({'staffId': staff_id})
            staff = Staff(staff_id, staff_object['name'], staff_object['department'], staff_object['phoneNumber'],
                          staff_object['isSecurityStaff'])

            client.close()
            return staff

        except Exception as e:
            print('unable to get staff')
            raise Exception('Could not get staff from DB')

    @staticmethod
    def get_staff_details_all():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][StaffDB.COLLECTION_NAME]

            staffs = document.find({})
            staff_details_all = []

            for staff in staffs:
                staff_obj = {
                    'name': staff['name'],
                    'staffId': staff['staffId']
                }

                staff_details_all.append(staff_obj)

            client.close()
            return staff_details_all

        except Exception as e:
            print('unable to get staff')
            raise Exception('Could not get staff from DB')
