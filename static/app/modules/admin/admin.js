app.controller('securityAdminController', ['$scope', '$state', 'securityAdminService', 'appointmentsService',
    function ($scope, $state, securityAdminService, appointmentsService) {

        // VARIABLES
        $scope.appointments = [];
        $scope.statusToFilterBy = '';
        $scope.rangeToFilterBy = '';
        $scope.getAppointmentsLoading = false;

        $scope.searchByDate = false;
        $scope.searchDateBeginDate = new Date();
        $scope.searchDateEndDate = new Date();

        $scope.visitorsNameSearchString = '';

        $scope.appointmentToEdit = {};
        $scope.appointmentToSignIn = {};
        $scope.appointmentToSignOut = {};

        $scope.init = function () {
            $scope.clearAllMessages();

            $scope.statusToFilterBy = 'All';
            $scope.rangeToFilterBy = 'Today';

            $scope.getAppointments();
        };

        $scope.getDateString = function (dateInMilliseconds) {
            var date = new Date(dateInMilliseconds);
            return date.toLocaleDateString() + ", " + date.toLocaleTimeString();
        };

        $scope.getAppointments = function () {
            $scope.clearAllMessages();
            $scope.getAppointmentsLoading = true;

            var successHandler = function (response) {
                $scope.appointments = response.data;
                $scope.getAppointmentsLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentsLoading = false;
            };

            if ($scope.rangeToFilterBy === 'All') {
                if ($scope.statusToFilterBy === 'All') {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAllAppointments(successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAllAppointmentsSearch($scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                } else {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAppointmentsForStatus($scope.statusToFilterBy, successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAppointmentsForStatusSearch($scope.statusToFilterBy, $scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                }
            }
            else if ($scope.rangeToFilterBy === 'Today') {
                var searchBeginTime = new Date();

                searchBeginTime.setHours(0);
                searchBeginTime.setMinutes(0);
                searchBeginTime.setSeconds(0);
                searchBeginTime.setMilliseconds(0);

                var searchEndTime = new Date();

                searchEndTime.setHours(23);
                searchEndTime.setMinutes(59);
                searchEndTime.setSeconds(59);
                searchEndTime.setMilliseconds(999);

                if ($scope.statusToFilterBy === 'All') {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAppointmentsFilterByTime(searchBeginTime.getTime(), searchEndTime.getTime(), successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAppointmentsFilterByTimeSearch(searchBeginTime.getTime(), searchEndTime.getTime(), $scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                }
                else {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAppointmentsForStatusFilterByTime($scope.statusToFilterBy, searchBeginTime.getTime(), searchEndTime.getTime(), successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAppointmentsForStatusFilterByTimeSearch($scope.statusToFilterBy, searchBeginTime.getTime(), searchEndTime.getTime(), $scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                }
            }
            else if ($scope.rangeToFilterBy === 'This week') {
                var searchBeginTime = new Date();
                var day = searchBeginTime.getDay();

                searchBeginTime.setTime(searchBeginTime.getTime() - (1000 * 60 * 60 * 24 * day));
                searchBeginTime.setHours(0);
                searchBeginTime.setMinutes(0);
                searchBeginTime.setSeconds(0);
                searchBeginTime.setMilliseconds(0);

                var searchEndTime = new Date();
                var day = searchEndTime.getDay();
                searchEndTime.setTime(searchEndTime.getTime() + (1000 * 60 * 60 * 24 * (6 - day)));

                searchEndTime.setHours(23);
                searchEndTime.setMinutes(59);
                searchEndTime.setSeconds(59);
                searchEndTime.setMilliseconds(999);

                if ($scope.statusToFilterBy === 'All') {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAppointmentsFilterByTime(searchBeginTime.getTime(), searchEndTime.getTime(), successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAppointmentsFilterByTimeSearch(searchBeginTime.getTime(), searchEndTime.getTime(), $scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                }
                else {
                    if ($scope.visitorsNameSearchString.trim() === '') {
                        securityAdminService.getAppointmentsForStatusFilterByTime($scope.statusToFilterBy, searchBeginTime.getTime(), searchEndTime.getTime(), successHandler, errorHandler);
                    }
                    else {
                        securityAdminService.getAppointmentsForStatusFilterByTimeSearch($scope.statusToFilterBy, searchBeginTime.getTime(), searchEndTime.getTime(), $scope.visitorsNameSearchString.trim(), successHandler, errorHandler);
                    }
                }
            }
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

            var successHandler = function (response) {
                $scope.appointments = response.data;
                $scope.getAppointmentsLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get appointments. Try again");
                $scope.getAppointmentsLoading = false;
            };

            if ($scope.statusToFilterBy === 'All') {
                securityAdminService.getAppointmentsFilterByTime(searchBeginTime, searchEndTime, successHandler, errorHandler);
            }
            else {
                securityAdminService.getAppointmentsForStatusFilterByTime($scope.statusToFilterBy, searchBeginTime, searchEndTime, successHandler, errorHandler);
            }
        };

        $scope.editTime = {};
        $scope.viewAppointment = function (appointment) {
            $scope.appointmentToEdit = appointment;
            $scope.editTime = new Date($scope.appointmentToEdit.dateTime);
            $('#editAppointmentModal').modal('show');
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
                $scope.getAppointments();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to edit appointment. Try again later.";
                $('#editAppointmentModal').modal('hide');
                $scope.setErrorMessage(errorMessage);
            };

            appointmentsService.editAppointment(appointmentObj, successHandler, errorHandler);
        };

        $scope.showSignInVisitorModal = function (appointment) {
            $scope.appointmentToSignIn = appointment;
            $('#signInVisitorModal').modal('show');
        };

        $scope.showSignOutVisitorModal = function (appointment) {
            $scope.appointmentToSignOut = appointment;
            $('#signOutVisitorModal').modal('show');
        };

        $scope.signVisitorIn = function () {
            var appointmentObj = {
                id: $scope.appointmentToSignIn.id,
                staffId: $scope.appointmentToSignIn.staffId,
                subject: $scope.appointmentToSignIn.subject,
                dateTime: $scope.appointmentToSignIn.dateTime,
                status: 'Signed In',
                visitorId: $scope.appointmentToSignIn.visitorId,
                visitorName: $scope.appointmentToSignIn.visitor.name,
                visitorAddress: $scope.appointmentToSignIn.visitor.address,
                visitorPhoneNumber: $scope.appointmentToSignIn.visitor.phoneNumber
            };

            var successHandler = function (response) {
                var successMessage = "Signed in successfully.";
                $scope.setSuccessMessage(successMessage);

                $('#signInVisitorModal').modal('hide');
                $scope.getAppointments();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to sign in. Try again later.";
                $('#signInVisitorModal').modal('hide');
                $scope.setErrorMessage(errorMessage);
            };

            appointmentsService.editAppointment(appointmentObj, successHandler, errorHandler);
        };

        $scope.signVisitorOut = function () {
            var appointmentObj = {
                id: $scope.appointmentToSignOut.id,
                staffId: $scope.appointmentToSignOut.staffId,
                subject: $scope.appointmentToSignOut.subject,
                dateTime: $scope.appointmentToSignOut.dateTime,
                status: 'Signed Out',
                visitorId: $scope.appointmentToSignOut.visitorId,
                visitorName: $scope.appointmentToSignOut.visitor.name,
                visitorAddress: $scope.appointmentToSignOut.visitor.address,
                visitorPhoneNumber: $scope.appointmentToSignOut.visitor.phoneNumber
            };

            var successHandler = function (response) {
                var successMessage = "Signed out successfully.";
                $scope.setSuccessMessage(successMessage);

                $('#signOutVisitorModal').modal('hide');
                $scope.getAppointments();
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to sign out. Try again later.";
                $('#signOutVisitorModal').modal('hide');
                $scope.setErrorMessage(errorMessage);
            };

            appointmentsService.editAppointment(appointmentObj, successHandler, errorHandler);
        };

    }]);

app.service('securityAdminService', ['$http', 'SERVER_URL', function ($http, SERVER_URL) {

    // GET ALL APPOINTMENTS
    this.getAllAppointments = function (successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments').then(successHandler, errorHandler);
    };

    // GET ALL APPOINTMENTS VISITORS NAME SEARCH
    this.getAllAppointmentsSearch = function (keyword, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments?keyword=' + keyword).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FILTER BY DATE TIME
    this.getAppointmentsFilterByTime = function (startTime, endTime, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/start-time/' + startTime + '/end-time/' + endTime).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FILTER BY DATE TIME VISITORS NAME SEARCH
    this.getAppointmentsFilterByTimeSearch = function (startTime, endTime, keyword, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/start-time/' + startTime + '/end-time/' + endTime + "?keyword=" + keyword).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FOR STATUS
    this.getAppointmentsForStatus = function (status, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/status/' + status).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FOR STATUS VISITORS NAME SEARCH
    this.getAppointmentsForStatusSearch = function (status, keyword, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/status/' + status + "?keyword=" + keyword).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FOR STATUS FILTER BY DATE TIME
    this.getAppointmentsForStatusFilterByTime = function (status, startTime, endTime, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/status/' + status + '/start-time/' + startTime + '/end-time/' + endTime).then(successHandler, errorHandler);
    };

    // GET APPOINTMENTS FOR STATUS FILTER BY DATE TIME VISITORS NAME SEARCH
    this.getAppointmentsForStatusFilterByTimeSearch = function (status, startTime, endTime, keyword, successHandler, errorHandler) {
        $http.get(SERVER_URL + '/appointments/status/' + status + '/start-time/' + startTime + '/end-time/' + endTime + "?keyword=" + keyword).then(successHandler, errorHandler);
    };
}]);
