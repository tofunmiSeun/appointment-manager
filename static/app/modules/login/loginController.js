app.controller('loginController', ['$scope', '$rootScope', '$state', 'AuthService', 'AUTH_EVENTS',
    function ($scope, $rootScope, $state, AuthService, AUTH_EVENTS) {
        $scope.credentials = {
            userId: '',
            password: ''
        };

        $scope.inProgress = false;

        $scope.login = function (credentials) {
            $scope.inProgress = true;
            $scope.clearErrorMessage();
            console.log("user trying to log in");

            var handler = function (data) {
                console.log("login successful");
                if (data.user){
                    $scope.setCurrentUser(data.user);
                $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
                }else{
                    $rootScope.$broadcast(AUTH_EVENTS.loginFailure, data.errorMessage);
                }
                $scope.inProgress = false;
            };

            var errorHandler = function (responseMessage) {
                $scope.inProgress = false;
                $rootScope.$broadcast(AUTH_EVENTS.loginFailure, responseMessage);
                console.log("login failed " + responseMessage);
            };

            AuthService.login(credentials).then(handler, errorHandler);
        };
    }]);