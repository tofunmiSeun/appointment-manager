app.controller('createAppointmentController', ['$scope', '$state', 'appointmentsService',
    function ($scope, $state, appointmentsService) {

        $scope.newAppointmentObject = {};
        $scope.visitorsForNewAppointment = [];
        $scope.newVisitorForNewAppointment = {};

        $scope.staffsObject = [];
        $scope.selectedStaffObject = {};

        $scope.init = function () {
            $scope.newAppointmentObject.dateTime = new Date();
            $scope.newVisitorForNewAppointment = {};
            $scope.newVisitorForNewAppointment.name = '';
            $scope.newVisitorForNewAppointment.address = '';
            $scope.newVisitorForNewAppointment.phoneNumber = '';

            $scope.getStaffDetailsAll();
        };

        $scope.getStaffDetailsAll = function () {

            var successHandler = function (response) {
                 $scope.staffsObject = response.data;

                 if ($scope.staffsObject.length > 0){
                     $scope.selectedStaffObject = $scope.staffsObject[0];
                 }
            };

            var errorHandler = function (response) {
                console.log(response)
            };

            appointmentsService.getStaffDetails(successHandler, errorHandler);
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
                staffId: $scope.selectedStaffObject.staffId,
                subject: $scope.newAppointmentObject.subject,
                dateTime: $scope.newAppointmentObject.dateTime.getTime(),
                visitors: $scope.visitorsForNewAppointment
            };

            var successHandler = function (response) {
                var successMessage = "Added appointment successfully.";
                $scope.setSuccessMessage(successMessage);

                $scope.visitorsForNewAppointment = [];
                $scope.newAppointmentObject = {};
                $scope.newAppointmentObject.subject = '';
                $scope.newAppointmentObject.dateTime = new Date();

                $scope.visitorsForNewAppointment = [];
            };

            var errorHandler = function (response) {
                var errorMessage = "Failed to add appointment. Try again later.";

                $scope.setErrorMessage(errorMessage);
                console.log(response)
            };

            appointmentsService.newAppointment(appointmentObj, successHandler, errorHandler);
        };
    }]);
