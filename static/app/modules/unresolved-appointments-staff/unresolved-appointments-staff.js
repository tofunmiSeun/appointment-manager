app.controller('unresolvedAppointmentsStaffController', ['$scope', '$state', 'appointmentsService', 'unresolvedAppointmentsStaffService',
    function ($scope, $state, appointmentsService, unresolvedAppointmentsStaffService) {

        $scope.unresolvedAppointmentCountForCurrentStaff = 0;

        $scope.unresolvedAppointmentsForStaff = [];
        $scope.statusToFilterBy = '';
        $scope.getAppointmentForStaffLoading = false;

        $scope.searchByDate = false;
        $scope.searchDateBeginDate = new Date();
        $scope.searchDateEndDate = new Date();

        $scope.appointmentToView = {};
        $scope.appointmentToResolve = {};
        $scope.resolveComment = '';

        $scope.init = function () {
            $scope.statusToFilterBy = 'Pending';
            $scope.searchDateBeginDate = new Date();
            $scope.searchDateEndDate = new Date();

            $scope.getUnresolvedAppointmentCountForStaff();

            $scope.clearAllMessages();
            $scope.getUnresolvedAppointmentsForStaff();
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

        $scope.getUnresolvedAppointmentsForStaff = function () {
            $scope.clearAllMessages();
            $scope.getAppointmentForStaffLoading = true;

            var staffId = $scope.currentUser.staffId;

            var successHandler = function (response) {
                $scope.unresolvedAppointmentsForStaff = response.data;
                $scope.getAppointmentForStaffLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentForStaffLoading = false;
                console.log(response)
            };

            unresolvedAppointmentsStaffService.getUnresolvedAppointmentsForStaffAndStatus(staffId, $scope.statusToFilterBy, successHandler, errorHandler);
        };

        $scope.getDateString = function (dateInMilliseconds) {
            var date = new Date(dateInMilliseconds);
            return date.toLocaleDateString() + ", " + date.toLocaleTimeString();
        };

        $scope.editTime = {};
        $scope.viewAppointment = function (appointment) {
            $scope.appointmentToView = appointment;
            $scope.editTime = new Date($scope.appointmentToView.dateTime);
            $('#viewAppointmentModal').modal('show');
        };

        $scope.showResolveAppointmentModal = function (appointment) {
            $scope.appointmentToResolve = appointment;
            $scope.resolveComment = '';
            $('#resolveAppointmentModal').modal('show');
        };

        $scope.resolveAppointment = function () {
            $scope.clearAllMessages();

            var updateObject = {
                appointmentId: $scope.appointmentToResolve.id,
                status: 'Resolved',
                resolvedComment: $scope.resolveComment
            };

            var successHandler = function (response) {
                var successMessage = "Resolved appointment successfully.";
                $scope.setSuccessMessage(successMessage);
                $('#resolveAppointmentModal').modal('hide');
                $scope.appointmentToResolve = {};

                $scope.getUnresolvedAppointmentsForStaff();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to resolve appointment";
                $scope.setErrorMessage(errorMessage);

                $scope.appointmentToResolve = {};
                $('#resolveAppointmentModal').modal('hide');

            };

            unresolvedAppointmentsStaffService.updateUnresolvedInfo(updateObject, successHandler, errorHandler);
        };

        $scope.getUnresolvedAppointmentsWithinSearchDate = function () {
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
                $scope.unresolvedAppointmentsForStaff = response.data;
                $scope.getAppointmentForStaffLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentForStaffLoading = false;
            };

            unresolvedAppointmentsStaffService.getUnresolvedAppointmentsForStaffAndStatusFilterByTime(staffId, $scope.statusToFilterBy, searchBeginTime, searchEndTime, successHandler, errorHandler);
        };
    }]);

app.service('unresolvedAppointmentsStaffService', ['$http', 'SERVER_URL', function ($http, SERVER_URL) {

    // GET UNRESOVLED APPOINTMENTS FOR STAFF AND STATUS
    this.getUnresolvedAppointmentsForStaffAndStatus = function (staffId, status, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments-unresolved/staff/' + staffId + '/status/' + status).then(successHandler, errorHandler);
    };

    // GET UNRESOLVED APPOINTMENTS FOR STAFF AND STATUS FILTER BY DATE TIME
    this.getUnresolvedAppointmentsForStaffAndStatusFilterByTime = function (staffId, status, startTime, endTime, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments-unresolved/staff/' + staffId + '/status/' + status + '/start-time/' + startTime + '/end-time/' + endTime).then(successHandler, errorHandler);
    };

    // UPDATE UNRESOLVED INFO
    this.updateUnresolvedInfo = function (updateObject, successHandler, errorHandler) {
        $http.put(SERVER_URL + "/appointment-unresolved", updateObject).then(successHandler, errorHandler);
    };
}]);