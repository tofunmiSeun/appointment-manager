app.controller('appointmentHistoryController', ['$scope', '$state', 'appointmentsService',
    function ($scope, $state, appointmentsService) {

        $scope.unresolvedAppointmentCountForCurrentStaff = 0;

        $scope.appointmentsForStaff = [];
        $scope.statusToFilterBy = '';
        $scope.getAppointmentForStaffLoading = false;

        $scope.searchByDate = false;
        $scope.searchDateBeginDate = new Date();
        $scope.searchDateEndDate = new Date();

        $scope.newAppointmentObject = {};
        $scope.visitorsForNewAppointment = [];
        $scope.newVisitorForNewAppointment = {};

        $scope.appointmentToEdit = {};
        $scope.appointmentToDelete = {};

        $scope.init = function () {
            $scope.statusToFilterBy = 'All';
            $scope.searchDateBeginDate = new Date();
            $scope.searchDateEndDate = new Date();

            $scope.getUnresolvedAppointmentCountForStaff();

            $scope.clearAllMessages();
            $scope.getAppointmentsForStaff();
        };

        $scope.getUnresolvedAppointmentCountForStaff = function () {

            var staffId = $scope.currentUser.staffId;

            var successHandler = function (response) {
                $scope.unresolvedAppointmentCountForCurrentStaff = response.data;
            };

            var errorHandler = function (response) {
                console.log(response)
            };

            appointmentsService.getUnresolvedAppointmentsCountForStaff(staffId, successHandler, errorHandler);
        };

        $scope.getAppointmentsForStaff = function () {
            $scope.clearAllMessages();
            $scope.getAppointmentForStaffLoading = true;

            var staffId = $scope.currentUser.staffId;

            var successHandler = function (response) {
                $scope.appointmentsForStaff = response.data;
                $scope.getAppointmentForStaffLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentForStaffLoading = false;
                console.log(response)
            };

            if ($scope.statusToFilterBy === 'All') {
                appointmentsService.getAppointmentsForStaff(staffId, successHandler, errorHandler);
            } else {
                appointmentsService.getAppointmentsForStaffAndStatus(staffId, $scope.statusToFilterBy, successHandler, errorHandler);
            }
        };

        $scope.getDateString = function (dateInMilliseconds) {
            var date = new Date(dateInMilliseconds);
            return date.toLocaleDateString() + ", " + date.toLocaleTimeString();
        };

        $scope.editTime = {};
        $scope.viewAppointment = function (appointment) {
            $scope.appointmentToEdit = appointment;
            $scope.editTime = new Date($scope.appointmentToEdit.dateTime);
            $('#editAppointmentModal').modal('show');
        };

        $scope.showNewAppointmentModal = function () {
            $('#addAppointmentModal').modal('show');

            $scope.newAppointmentObject.dateTime = new Date();

            $scope.newVisitorForNewAppointment = {};
            $scope.newVisitorForNewAppointment.name = '';
            $scope.newVisitorForNewAppointment.address = '';
            $scope.newVisitorForNewAppointment.phoneNumber = '';
        };

        $scope.addNewVisitorToList = function () {
            $scope.visitorsForNewAppointment.push($scope.newVisitorForNewAppointment);
            $scope.newVisitorForNewAppointment = {};
            $scope.newVisitorForNewAppointment.name = '';
            $scope.newVisitorForNewAppointment.address = '';
            $scope.newVisitorForNewAppointment.phoneNumber = '';
        };

        $scope.deleteVisitorFromList = function (visitor) {
            var index = $scope.visitorsForNewAppointment.indexOf(visitor);
            $scope.visitorsForNewAppointment.splice(index, 1);
        };

        $scope.addNewAppointment = function () {
            $scope.clearAllMessages();

            var appointmentObj = {
                staffId: $scope.currentUser.staffId,
                subject: $scope.newAppointmentObject.subject,
                dateTime: $scope.newAppointmentObject.dateTime.getTime(),
                visitors: $scope.visitorsForNewAppointment
            };

            var successHandler = function (response) {
                var successMessage = "Added appointment successfully.";
                $scope.setSuccessMessage(successMessage);

                $('#addAppointmentModal').modal('hide');
                $scope.visitorsForNewAppointment = [];
                $scope.newAppointmentObject = {};
                $scope.newAppointmentObject.subject = '';
                $scope.newAppointmentObject.dateTime = new Date();

                $scope.visitorsForNewAppointment = [];

                $scope.getAppointmentsForStaff();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to add appointment. Try again later.";

                $('#addAppointmentModal').modal('hide');
                $scope.setErrorMessage(errorMessage);
                console.log(response)
            };

            appointmentsService.newAppointment(appointmentObj, successHandler, errorHandler);
        };

        $scope.editAppointment = function () {
            var appointmentObj = {
                id: $scope.appointmentToEdit.id,
                staffId: $scope.appointmentToEdit.staffId,
                subject: $scope.appointmentToEdit.subject,
                dateTime: $scope.editTime.getTime(),
                status: $scope.appointmentToEdit.status,
                visitorId: $scope.appointmentToEdit.visitorId,
                visitorName: $scope.appointmentToEdit.visitor.name,
                visitorAddress: $scope.appointmentToEdit.visitor.address,
                visitorPhoneNumber: $scope.appointmentToEdit.visitor.phoneNumber
            };

            var successHandler = function (response) {
                var successMessage = "Edited appointment successfully.";
                $scope.setSuccessMessage(successMessage);

                $('#editAppointmentModal').modal('hide');
                $scope.getAppointmentsForStaff();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to edit appointment. Try again later.";
                $('#editAppointmentModal').modal('hide');
                $scope.setErrorMessage(errorMessage);
            };

            appointmentsService.editAppointment(appointmentObj, successHandler, errorHandler);
        };

        $scope.showDeleteAppointmentModal = function (appointment) {
            $scope.appointmentToDelete = appointment;
            $('#deleteAppointmentModal').modal('show');
        };

        $scope.deleteAppointment = function () {
            $scope.clearAllMessages();

            var successHandler = function (response) {
                var successMessage = "Deleted appointment successfully.";
                $scope.setSuccessMessage(successMessage);
                $('#deleteAppointmentModal').modal('hide');
                $scope.appointmentToDelete = {};

                $scope.getAppointmentsForStaff();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to delete appointment";
                $scope.setErrorMessage(errorMessage);

                $scope.appointmentToDelete = {};
                $('#deleteAppointmentModal').modal('hide');

            };

            appointmentsService.deleteAppointment($scope.appointmentToDelete.id, $scope.appointmentToDelete.visitorId, successHandler, errorHandler);
        };

        $scope.getAppointmentsWithinSearchDate = function () {
            $scope.clearAllMessages();
            $scope.getAppointmentForStaffLoading = true;

            $scope.searchDateBeginDate.setHours(0);
            $scope.searchDateBeginDate.setMinutes(0);
            $scope.searchDateBeginDate.setSeconds(0);
            $scope.searchDateBeginDate.setMilliseconds(0);

            var searchBeginTime = $scope.searchDateBeginDate.getTime();

            $scope.searchDateEndDate.setHours(23);
            $scope.searchDateEndDate.setMinutes(59);
            $scope.searchDateEndDate.setSeconds(59);
            $scope.searchDateEndDate.setMilliseconds(999);

            var searchEndTime = $scope.searchDateEndDate.getTime();


            var staffId = $scope.currentUser.staffId;

            var successHandler = function (response) {
                $scope.appointmentsForStaff = response.data;
                $scope.getAppointmentForStaffLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentForStaffLoading = false;
            };

            if ($scope.statusToFilterBy === 'All') {
                appointmentsService.getAppointmentsForStaffFilterByTime(staffId, searchBeginTime, searchEndTime, successHandler, errorHandler);
            } else {
                appointmentsService.getAppointmentsForStaffAndStatusFilterByTime(staffId, $scope.statusToFilterBy, searchBeginTime, searchEndTime, successHandler, errorHandler);
            }
        };
    }]);
