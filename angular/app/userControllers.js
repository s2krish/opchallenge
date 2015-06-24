'use strict';

var userController = angular.module('userController', []);

userController.controller('UserListCtrl', ['$scope', 'User',
    function($scope, User) {
        
        $scope.curUser = User.getUser();

        User.user.query(
            function(data) {
                $scope.users = data.results
                $scope.maxSize = (data.count) ? count : data.results.length
                $scope.currentPage = 1
            },
            function(error){
                console.log(error)
            }
        );
  }]
);


userController.controller('SignupCtrl', ['$scope', 'User',
  function($scope, User) {
    $scope.signup = function() {
        console.log("signup");
        User.user.save($scope.user,
            function(data){
                $scope.signed = true
                //$scope.reset();
            },
            function(error){
                console.log(error)
            }
        );
    };
    $scope.reset = function() {
        $scope.user = {
            'user_name': '',
            'password': '',
            'first_name': '',
            'last_name': '',
        }
    };
    $scope.reset();
  }]
);

userController.controller('LoginCtrl', ['$scope', '$location', 'User',
    function($scope, $location, User) {
        $scope.login = function() {
            User.auth.login($scope.user,
                function(data) {
                    $location.path('/users')
                },
                function(error) {
                    console.log(error) 
                }
            )
        };
        $scope.reset = function() {
            $scope.user = {
                'user_name': '',
                'password': ''
            }
        };

        $scope.reset();
    }]
);

userController.controller('MeCtrl', ['$scope', 'User',
    function($scope, User) {
        $scope.user = User.getUser()
    }]
);
