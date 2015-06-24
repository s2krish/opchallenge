'use strict';

/* App Module */

var app = angular.module('app', [
  'ngRoute',
  'userServices',
  'userController',
  'messageServices',
  'messageController',
  'homeController',
]);


app.run(['$rootScope', '$location', 'User', function ($rootScope, $location, User) {
    $rootScope.$on('$routeChangeStart', function (event) {
          User.me.check(
              function(data){
                  //If logged in redirect to /users when user tries to go home
                  if (data.id) {
                      if ($location.path() == '/') {
                          $location.path("/users")
                      }
                      User.setUser(data);
                  }
              },
              function(erorr){
                  //If not logged in, redirect to home (=login page)
                  if ($location.path() != '/') {
                    $location.path("/")
                  }
              }
          );
    });
}]);

app.config(['$routeProvider', '$resourceProvider', '$httpProvider', 
    function($routeProvider, $resourceProvider, $httpProvider) {

        $resourceProvider.defaults.stripTrailingSlashes = false;
        // For Django
        // $httpProvider.defaults.headers.common['X-CSRF-Token'] = $('meta[name=csrf-token]').attr('content');

        $routeProvider.
          when('/', {
            templateUrl: 'views/home.html',
            controller: 'HomeCtrl'
          }).
          when('/users', {
            templateUrl: 'views/user-list.html',
            controller: 'UserListCtrl'
          }).
          when('/users/login', {
            controller: 'loginCtrl'
          }).
          when('/users/:Id', {
            templateUrl: 'views/user-detail.html',
            controller: 'UserDetailCtrl'
          }).
          when('/messages', {
            templateUrl: 'views/message-list.html',
            controller: 'MessageListCtrl'
          }).
          when('/message/send/:user', {
            templateUrl: 'views/message-send.html',
            controller: 'MessageSendCtrl'
          }).
          when('/message/:Id', {
            templateUrl: 'views/message-read.html',
            controller: 'MessageReadCtrl'
          }).
          otherwise({
            redirectTo: '/'
          });
    }]
);

