from pymongo import MongoClient
from utils.constant import Constant


class AuthorizationDB:

    COLLECTION_NAME = 'authorizations'

    @staticmethod
    def new_authorization(authorization_object):
        try:
            obj = {
                'staffId': authorization_object['staffId'],
                'password': authorization_object['password']
            }

            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AuthorizationDB.COLLECTION_NAME]

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to add new authorization')
            raise Exception('Could not add new authorization to DB')

    @staticmethod
    def authorize(staff_id, password):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AuthorizationDB.COLLECTION_NAME]

            authorization = document.find_one({'staffId': staff_id})
            if authorization is None:
                return False

            a_pass = authorization['password']
            client.close()

            if password == a_pass:
                return True

            return False

        except Exception as e:
            print('unable to authorize staff')
            raise Exception('Could not authorize staff')
