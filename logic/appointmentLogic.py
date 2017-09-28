from db.appointmentDB import AppointmentDB
from db.visitorDB import VisitorDB
from db.unresolvedInfoDB import UnresolvedInfoDB


class AppointmentLogic:
    @staticmethod
    def add_new_appointment(appointment_object):
        staff_id = appointment_object['staffId']
        subject_of_visit = appointment_object['subject']
        date_time = appointment_object['dateTime']

        visitors = appointment_object['visitors']
        for visitor in visitors:
            visitor_id = VisitorDB.new_visitor(visitor)

            appointment_obj = {
                'staffId': staff_id,
                'visitorId': str(visitor_id),
                'subject': subject_of_visit,
                'dateTime': date_time,
            }

            AppointmentDB.new_appointment(appointment_obj)

    @staticmethod
    def edit_appointment(appointment_object):
        visitor_id = appointment_object['visitorId']

        visitor_object = {
            'name': appointment_object['visitorName'],
            'address': appointment_object['visitorAddress'],
            'phoneNumber': appointment_object['visitorPhoneNumber']
        }

        VisitorDB.edit_visitor(visitor_id, visitor_object)

        staff_id = appointment_object['staffId']
        subject_of_visit = appointment_object['subject']
        date_time = appointment_object['dateTime']
        status = appointment_object['status']

        appointment_obj = {
            'staffId': staff_id,
            'visitorId': visitor_id,
            'subject': subject_of_visit,
            'dateTime': date_time,
            'status': status
        }

        AppointmentDB.edit_appointment(appointment_object['id'], appointment_obj)

    @staticmethod
    def delete_appointment(appointment_id, visitor_id):
        VisitorDB.delete_visitor(visitor_id)
        AppointmentDB.delete_appointment(appointment_id)

    @staticmethod
    def get_all_appointments():
        return AppointmentDB.get_all_appointments()

    @staticmethod
    def search_all_appointments_visitors_name(keyword):
        return AppointmentDB.search_all_appointments_visitors_name(keyword)

    @staticmethod
    def get_all_appointments_filter_by_date_time(start_time, end_time):
        return AppointmentDB.get_all_appointments_filter_by_date_time(start_time, end_time)

    @staticmethod
    def get_all_appointments_filter_by_date_time_visitors_name_search(start_time, end_time, keyword):
        return AppointmentDB.get_all_appointments_filter_by_date_time_visitors_name_search(start_time, end_time,
                                                                                           keyword)

    @staticmethod
    def get_appointments_for_status(status):
        return AppointmentDB.get_appointments_for_status(status)

    @staticmethod
    def get_appointments_for_status_visitors_name_search(status, keyword):
        return AppointmentDB.get_appointments_for_status_visitors_name_search(status, keyword)

    @staticmethod
    def get_appointments_for_staff(staff_id):
        return AppointmentDB.get_appointments_for_staff(staff_id)

    @staticmethod
    def get_appointments_for_staff_and_status(staff_id, status):
        return AppointmentDB.get_appointments_for_staff_and_status(staff_id, status)

    @staticmethod
    def get_appointments_for_staff_filter_by_date_time(staff_id, start_time, end_time):
        return AppointmentDB.get_appointments_for_staff_filter_by_date_time(staff_id, start_time, end_time)

    @staticmethod
    def get_appointments_for_staff_and_status_filter_by_date_time(staff_id, status, start_time, end_time):
        return AppointmentDB.get_appointments_for_staff_and_status_filter_by_date_time(staff_id, status, start_time,
                                                                                       end_time)

    @staticmethod
    def get_appointments_for_status_filter_by_date_time(status, start_time, end_time):
        return AppointmentDB.get_appointments_for_status_filter_by_date_time(status, start_time, end_time)

    @staticmethod
    def get_appointments_for_status_filter_by_date_time_visitors_name_search(status, start_time, end_time, keyword):
        return AppointmentDB.get_appointments_for_status_filter_by_date_time_visitors_name_search(status, start_time,
                                                                                                  end_time, keyword)

    @staticmethod
    def get_unresolved_appointments_with_status_for_staff(staff_id, status):
        if status == UnresolvedInfoDB.STATUS_RESOLVED:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_resolved_unresolved_infos()
        elif status == UnresolvedInfoDB.STATUS_PENDING:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_pending_unresolved_infos()
        else:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_all_unresolved_infos()

        appointments = AppointmentDB.get_appointments_for_staff_in(staff_id, appointment_ids)
        for appointment in appointments:
            unresolved_info = UnresolvedInfoDB.get_unresolved_info_for_appointment(appointment.id)
            appointment.set_unresolved_info(unresolved_info)

        return appointments

    @staticmethod
    def get_unresolved_appointments_with_status_for_staff_filter_by_date_time(staff_id, status, start_time,
                                                                              end_time):
        if status == UnresolvedInfoDB.STATUS_RESOLVED:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_resolved_unresolved_infos()
        elif status == UnresolvedInfoDB.STATUS_PENDING:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_pending_unresolved_infos()
        else:
            appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_all_unresolved_infos()

        appointments = AppointmentDB.get_appointments_for_staff_in_filter_by_date_time(staff_id, appointment_ids,
                                                                                       start_time, end_time)
        for appointment in appointments:
            unresolved_info = UnresolvedInfoDB.get_unresolved_info_for_appointment(appointment.id)
            appointment.set_unresolved_info(unresolved_info)

        return appointments

    @staticmethod
    def update_unresolved_info(update_object):
        appointment_id = update_object['appointmentId']
        status = update_object['status']
        resolved_comment = update_object['resolvedComment']

        UnresolvedInfoDB.edit_unresolved_info(appointment_id, status, resolved_comment)

    @staticmethod
    def get_unresolved_appointments_count_for_staff(staff_id):
        appointment_ids = UnresolvedInfoDB.get_appointment_ids_of_pending_unresolved_infos()

        return AppointmentDB.get_appointments_count_for_staff_in(staff_id, appointment_ids)
