from pymongo import MongoClient
from bson.objectid import ObjectId
from models.visitor import Visitor
from utils.constant import Constant


class VisitorDB:
    COLLECTION_NAME = 'visitors'

    @staticmethod
    def new_visitor(visitor_object):
        try:
            obj = {
                'name': visitor_object['name'],
                'address': visitor_object['address'],
                'phoneNumber': visitor_object['phoneNumber']
            }

            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][VisitorDB.COLLECTION_NAME]

            id = document.insert(obj)
            client.close()

            return id

        except Exception as e:
            print('unable to add new visitor: ' + str(e))
            raise Exception('Could not add new visitor to DB')

    @staticmethod
    def get_visitor_by_id(visitor_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][VisitorDB.COLLECTION_NAME]

            visitor_object = document.find_one({'_id': ObjectId(visitor_id)})
            visitor = Visitor(visitor_id, visitor_object['name'], visitor_object['address'], visitor_object['phoneNumber'])

            client.close()
            return visitor

        except Exception as e:
            print('unable to get visitor: ' + str(e))
            raise Exception('Could not get visitor from DB')

    @staticmethod
    def edit_visitor(visitor_id, visitor_object):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][VisitorDB.COLLECTION_NAME]

            command = {
                "$set": {
                    "name": visitor_object['name'],
                    "address": visitor_object['address'],
                    "phoneNumber": visitor_object['phoneNumber']
                }
            }

            document.update({'_id': ObjectId(visitor_id)}, command)
            client.close()

        except Exception as e:
            print('unable to get visitor: ' + str(e))
            raise Exception('Could not get visitor from DB')

    @staticmethod
    def delete_visitor(visitor_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][VisitorDB.COLLECTION_NAME]

            document.delete_one({'_id': ObjectId(visitor_id)})
        except Exception as e:
            print(e)
