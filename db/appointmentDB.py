from pymongo import MongoClient
from bson.objectid import ObjectId
from models.appointment import Appointment
from db.visitorDB import VisitorDB
from db.staffDB import StaffDB
from utils.constant import Constant


class AppointmentDB:
    COLLECTION_NAME = 'appointments'

    @staticmethod
    def new_appointment(appointment_object):
        try:
            obj = {
                'staffId': appointment_object['staffId'],
                'visitorId': appointment_object['visitorId'],
                'subject': appointment_object['subject'],
                'dateTime': appointment_object['dateTime'],
                'status': Constant.APPOINTMENT_STATUS[2]
            }

            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            document.insert(obj)
            client.close()

        except Exception as e:
            print('unable to add new appointment')
            raise Exception('Could not add new appointment to DB')

    @staticmethod
    def get_all_appointments():
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments')
            raise Exception('Could not get appointments')

    @staticmethod
    def search_all_appointments_visitors_name(visitor_name_keyword):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                if visitor_name_keyword.lower() not in visitor.name.lower():
                    continue

                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments')
            raise Exception('Could not get appointments')

    @staticmethod
    def get_all_appointments_filter_by_date_time(start_time, end_time):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_all_appointments_filter_by_date_time_visitors_name_search(start_time, end_time, visitor_name_keyword):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                if visitor_name_keyword.lower() not in visitor.name.lower():
                    continue

                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_staff(staff_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'staffId': staff_id})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_staff_filter_by_date_time(staff_id, start_time, end_time):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'staffId': staff_id, 'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_status(status):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'status': status})

            appointments_for_status = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], status)

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_status.append(a)

            client.close()
            return appointments_for_status

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_status_visitors_name_search(status, visitor_name_keyword):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'status': status})

            appointments_for_status = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'], appointment['dateTime'], status)

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                if visitor_name_keyword.lower() not in visitor.name.lower():
                    continue

                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_status.append(a)

            client.close()
            return appointments_for_status

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_staff_and_status(staff_id, status):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find({'staffId': staff_id, 'status': status})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_status_filter_by_date_time(status, start_time, end_time):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find(
                {'status': status, 'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], status)

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments')
            raise Exception('Could not get appointments')

    @staticmethod
    def get_appointments_for_status_filter_by_date_time_visitors_name_search(status, start_time, end_time, visitor_name_keyword):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find(
                {'status': status, 'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), appointment['staffId'], appointment['visitorId'],
                                appointment['subject'],
                                appointment['dateTime'], status)

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                if visitor_name_keyword.lower() not in visitor.name.lower():
                    continue

                a.set_visitor(visitor)

                staff = StaffDB.get_staff_by_id(appointment['staffId'])
                a.set_staff(staff.serialize)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments')
            raise Exception('Could not get appointments')

    @staticmethod
    def get_appointments_for_staff_and_status_filter_by_date_time(staff_id, status, start_time, end_time):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointments = document.find(
                {'staffId': staff_id, 'status': status, 'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff')
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_staff_in(staff_id, appointment_ids):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointment_ids_obj = [ObjectId(item) for item in appointment_ids]

            appointments = document.find({'_id': {'$in': appointment_ids_obj}, 'staffId': staff_id})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff - ' + str(e))
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_for_staff_in_filter_by_date_time(staff_id, appointment_ids, start_time, end_time):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointment_ids_obj = [ObjectId(item) for item in appointment_ids]

            appointments = document.find({'_id': {'$in': appointment_ids_obj}, 'staffId': staff_id,
                                          'dateTime': {'$gte': start_time, '$lte': end_time}})

            appointments_for_staff = []

            for appointment in appointments:
                a = Appointment(str(appointment['_id']), staff_id, appointment['visitorId'], appointment['subject'],
                                appointment['dateTime'], appointment['status'])

                visitor = VisitorDB.get_visitor_by_id(appointment['visitorId'])
                a.set_visitor(visitor)

                appointments_for_staff.append(a)

            client.close()
            return appointments_for_staff

        except Exception as e:
            print('unable to get appointments for staff - ' + str(e))
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def get_appointments_count_for_staff_in(staff_id, appointment_ids):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            appointment_ids_obj = [ObjectId(item) for item in appointment_ids]

            return document.find({'_id': {'$in': appointment_ids_obj}, 'staffId': staff_id}).count()

        except Exception as e:
            print('unable to get appointments for staff - ' + str(e))
            raise Exception('Could not get appointments for staff')

    @staticmethod
    def edit_appointment(appointment_id, appointment_object):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            command = {
                "$set": {
                    'staffId': appointment_object['staffId'],
                    'visitorId': appointment_object['visitorId'],
                    'subject': appointment_object['subject'],
                    'dateTime': appointment_object['dateTime'],
                    'status': appointment_object['status']
                }
            }

            document.update({'_id': ObjectId(appointment_id)}, command)
            client.close()

        except Exception as e:
            print('unable to update appointment: ' + str(e))
            raise Exception('Could not update appointment in DB')

    @staticmethod
    def delete_appointment(appointment_id):
        try:
            client = MongoClient(Constant.DB_CONNECTION_URL)
            document = client[Constant.DB_NAME][AppointmentDB.COLLECTION_NAME]

            document.delete_one({'_id': ObjectId(appointment_id)})
        except Exception as e:
            print(e)
