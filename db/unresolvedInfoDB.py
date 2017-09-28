from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.constant import Constant


class UnresolvedInfoDB:
    COLLECTION_NAME = 'unresolvedInfo'
    STATUS_PENDING = 'Pending'
    STATUS_RESOLVED = 'Resolved'

    @staticmethod
    def new_unresolved_info(appointment_id):
        try:
            obj = {
                'appointmentId': appointment_id,
                'status': UnresolvedInfoDB.STATUS_PENDING,
                'resolvedComment': ''
            }

            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to add new unresolved info')
            raise Exception('Could not add new unresolved info to DB')

    @staticmethod
    def get_unresolved_info_for_appointment(appointment_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            result = document.find_one({'appointmentId': appointment_id})

            unresolved_info = {
                'appointmentId': appointment_id,
                'status': result['status'],
                'resolvedComment': result['resolvedComment']
            }

            client.close()
            return unresolved_info

        except Exception as e:
            print('unable to get unresolved info for appointment')
            raise Exception('Could not get unresolved info for appointment')

    @staticmethod
    def edit_unresolved_info(appointment_id, new_status, resolved_comment):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            command = {
                "$set": {
                    'status': new_status,
                    'resolvedComment': resolved_comment
                }
            }

            document.update({'appointmentId': appointment_id}, command)
            client.close()

        except Exception as e:
            print('unable to update unresolved info: ' + str(e))
            raise Exception('Could not unpdate unresolved info from DB')

    @staticmethod
    def is_appointment_unresolved(appointment_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            result = document.find_one({'appointmentId': appointment_id})
            client.close()

            return result is not None

        except Exception as e:
            print('unable to get unresolved info for appointment - ' + str(e))
            raise Exception('Could not get unresolved info for appointment')

    @staticmethod
    def get_appointment_ids_of_all_unresolved_infos():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            result = document.find({})
            appointment_ids = []
            for item in result:
                appointment_id = item['appointmentId']
                appointment_ids.append(appointment_id)

            client.close()

            return appointment_ids

        except Exception as e:
            print('unable to get appointment IDs - ' + str(e))
            raise Exception('Could not get appointment IDs')

    @staticmethod
    def get_appointment_ids_of_pending_unresolved_infos():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            result = document.find({'status': UnresolvedInfoDB.STATUS_PENDING})
            appointment_ids = []
            for item in result:
                appointment_id = item['appointmentId']
                appointment_ids.append(appointment_id)

            client.close()

            return appointment_ids

        except Exception as e:
            print('unable to get appointment IDs - ' + str(e))
            raise Exception('Could not get appointment IDs')

    @staticmethod
    def get_appointment_ids_of_resolved_unresolved_infos():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][UnresolvedInfoDB.COLLECTION_NAME]

            result = document.find({'status': UnresolvedInfoDB.STATUS_RESOLVED})
            appointment_ids = []
            for item in result:
                appointment_id = item['appointmentId']
                appointment_ids.append(appointment_id)

            client.close()

            return appointment_ids

        except Exception as e:
            print('unable to get appointment IDs - ' + str(e))
            raise Exception('Could not get appointment IDs')
