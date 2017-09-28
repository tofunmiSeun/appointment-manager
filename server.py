from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from logic.staffLogic import StaffLogic
from logic.authorizationLogic import AuthorizationLogic
from logic.appointmentLogic import AppointmentLogic

app = Flask(__name__)
CORS(app)


@app.route('/api/login', methods=['POST'])
def staff_login():
    try:
        login_request = request.json
        staff = AuthorizationLogic.authorize(login_request)
        return jsonify({'user': staff.serialize})

    except Exception as e:
        return jsonify({'errorMessage': str(e)})


@app.route('/api/staff-details/all')
def get_staff_details_all():
    staff_details_all = StaffLogic.get_staff_details_all()
    return jsonify(staff_details_all)


@app.route('/api/appointments')
def get_all_appointments():
    keyword = request.args.get('keyword')
    if keyword is None:
        appointments = AppointmentLogic.get_all_appointments()
    else:
        appointments = AppointmentLogic.search_all_appointments_visitors_name(keyword)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments/start-time/<int:start_time>/end-time/<int:end_time>')
def get_all_appointments_filter_by_date_time(start_time, end_time):
    keyword = request.args.get('keyword')
    if keyword is None:
        appointments = AppointmentLogic.get_all_appointments_filter_by_date_time(start_time, end_time)
    else:
        appointments = AppointmentLogic.get_all_appointments_filter_by_date_time_visitors_name_search(start_time,
                                                                                                      end_time, keyword)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments/status/<status>')
def get_appointments_for_status(status):
    keyword = request.args.get('keyword')
    if keyword is None:
        appointments = AppointmentLogic.get_appointments_for_status(status)
    else:
        appointments = AppointmentLogic.get_appointments_for_status_visitors_name_search(status, keyword)

    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments/status/<status>/start-time/<int:start_time>/end-time/<int:end_time>')
def get_appointments_for_status_filter_by_date(status, start_time, end_time):
    keyword = request.args.get('keyword')
    if keyword is None:
        appointments = AppointmentLogic.get_appointments_for_status_filter_by_date_time(status, start_time, end_time)
    else:
        appointments = AppointmentLogic.get_appointments_for_status_filter_by_date_time_visitors_name_search(status,
                                                                                                             start_time,
                                                                                                             end_time,
                                                                                                             keyword)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments/staff/<staff_id>')
def get_appointments_for_staff(staff_id):
    appointments_for_staff = AppointmentLogic.get_appointments_for_staff(staff_id)
    return jsonify([course.serialize for course in appointments_for_staff])


@app.route('/api/appointments/staff/<staff_id>/status/<status>')
def get_appointments_for_staff_and_status(staff_id, status):
    appointments_for_staff = AppointmentLogic.get_appointments_for_staff_and_status(staff_id, status)
    return jsonify([course.serialize for course in appointments_for_staff])


@app.route('/api/appointments/staff/<staff_id>/start-time/<int:start_time>/end-time/<int:end_time>')
def get_appointments_for_staff_filter_by_date(staff_id, start_time, end_time):
    appointments = AppointmentLogic.get_appointments_for_staff_filter_by_date_time(staff_id, start_time, end_time)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments/staff/<staff_id>/status/<status>/start-time/<int:start_time>/end-time/<int:end_time>')
def get_appointments_for_staff_and_status_filter_by_date(staff_id, status, start_time, end_time):
    appointments = AppointmentLogic.get_appointments_for_staff_and_status_filter_by_date_time(staff_id, status,
                                                                                              start_time,
                                                                                              end_time)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointment', methods=['POST'])
def add_new_appointment():
    try:
        appointment_json_object = request.json
        if appointment_json_object:
            AppointmentLogic.add_new_appointment(appointment_json_object)

    except Exception as exception_object:
        print(exception_object)
        return "Internal Server error", 500, {'ContentType': 'application/json'}

    return "", 200, {'ContentType': 'application/json'}


@app.route('/api/appointment', methods=['PUT'])
def edit_appointment():
    try:
        appointment_json_object = request.json
        if appointment_json_object:
            AppointmentLogic.edit_appointment(appointment_json_object)

    except Exception as exception_object:
        print(exception_object)
        return "Internal Server error", 500, {'ContentType': 'application/json'}

    return "", 200, {'ContentType': 'application/json'}


@app.route('/api/appointment/<appointment_id>/visitor/<visitor_id>', methods=['DELETE'])
def delete_appointment(appointment_id, visitor_id):
    try:
        AppointmentLogic.delete_appointment(appointment_id, visitor_id)

    except Exception as exception_object:
        print(exception_object)
        return "Internal Server error", 500, {'ContentType': 'application/json'}

    return "", 200, {'ContentType': 'application/json'}


@app.route('/api/appointments-unresolved/staff/<staff_id>/status/<status>')
def get_unresolved_appointments_for_staff_and_status(staff_id, status):
    appointments_for_staff = AppointmentLogic.get_unresolved_appointments_with_status_for_staff(staff_id, status)
    return jsonify([course.serialize for course in appointments_for_staff])


@app.route(
    '/api/appointments-unresolved/staff/<staff_id>/status/<status>/start-time/<int:start_time>/end-time/<int:end_time>')
def get_unresolved_appointments_for_staff_and_status_filter_by_date(staff_id, status, start_time, end_time):
    appointments = AppointmentLogic.get_unresolved_appointments_with_status_for_staff_filter_by_date_time(staff_id,
                                                                                                          status,
                                                                                                          start_time,
                                                                                                          end_time)
    return jsonify([course.serialize for course in appointments])


@app.route('/api/appointments-unresolved-count/staff/<staff_id>')
def get_unresolved_appointments_count_for_staff(staff_id):
    return jsonify(AppointmentLogic.get_unresolved_appointments_count_for_staff(staff_id))


@app.route('/api/appointment-unresolved', methods=['PUT'])
def update_unresolved_info():
    try:
        update_json_object = request.json
        if update_json_object:
            AppointmentLogic.update_unresolved_info(update_json_object)

    except Exception as exception_object:
        print(exception_object)
        return "Internal Server error", 500, {'ContentType': 'application/json'}

    return "", 200, {'ContentType': 'application/json'}


@app.route("/")
def serve_index_page():
    return send_file('index.html')


if __name__ == "__main__":
    app.run(port=8080, debug=True)
