app.controller('ApplicationController', ['$scope', '$rootScope', '$state', 'AuthService', 'AUTH_EVENTS',
    function ($scope, $rootScope, $state, AuthService, AUTH_EVENTS) {
        $scope.currentUser = null;
        $scope.isAdmin = AuthService.isAdmin;
        $scope.successMessage = null;
        $scope.errorMessage = null;

        $scope.setCurrentUser = function (user) {
            $scope.currentUser = user;
        };
        $scope.setSuccessMessage = function (message) {
            $scope.successMessage = message;
        };
        $scope.clearSuccessMessage = function () {
            $scope.successMessage = null;
        };
        $scope.setErrorMessage = function (message) {
            $scope.errorMessage = message;
        };
        $scope.clearErrorMessage = function () {
            $scope.errorMessage = null;
        };

        $scope.clearAllMessages = function () {
            $scope.clearSuccessMessage();
            $scope.clearErrorMessage();
        };

        $scope.logout = function () {
            AuthService.logout();
            $rootScope.$broadcast(AUTH_EVENTS.logoutSuccess);
        };

        // LOGIN SUCCESS
        $rootScope.$on(AUTH_EVENTS.loginSuccess, function (event, data) {
            $state.transitionTo('home.appointments');
        });

        // LOGIN FAILURE
        $rootScope.$on(AUTH_EVENTS.loginFailure, function (event, data) {
            $scope.setErrorMessage(data);
        });

        // LOGOUT SUCCESS
        $rootScope.$on(AUTH_EVENTS.logoutSuccess, function (event) {
            $state.transitionTo('login');
        });
    }]);