app.config(['$stateProvider', '$urlRouterProvider',

    function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/login");

        $stateProvider
            .state('login', {
                url: '/login',
                templateUrl: 'static/app/modules/login/login.html',
                data: {requiresLogin: false}
            })
            .state('home', {
                url: '/home',
                templateUrl: 'static/app/modules/home/home.html',
                data: {requiresLogin: true}
            })
            .state('home.appointments', {
                url: '/appointments',
                templateUrl: 'static/app/modules/appointments/appointments.html',
                data: {requiresLogin: true}
            })
            .state('home.appointments-history', {
                url: '/appointments-history',
                templateUrl: 'static/app/modules/history-apointment-staff/history-apointment-staff.html',
                data: {requiresLogin: true}
            })
            .state('home.unresolved-appointments-staff', {
                url: '/course/:courseId',
                templateUrl: 'static/app/modules/unresolved-appointments-staff/unresolved-appointments-staff.html',
                data: {requiresLogin: true}
            })
            .state('home.admin', {
                url: '/admin',
                templateUrl: 'static/app/modules/admin/admin.html',
                data: {requiresLogin: true, requiresAdmin: true}
            })
            .state('home.create-appointment-security', {
                url: '/new-appointment',
                templateUrl: 'static/app/modules/create-appointment-security/create-appointment-security.html',
                data: {requiresLogin: true, requiresAdmin: true}
            })
    }
]);