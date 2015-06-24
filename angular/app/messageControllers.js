'use strict';

var messageController = angular.module('messageController', []);

messageController.controller('MessageListCtrl', ['$scope', 'Message',
    function($scope, Message) {
        Message.query(
            function(data) {
                $scope.messages = data.results;
                $scope.maxSize = (data.count) ? count : data.results.length;
                $scope.currentPage = 1;
            },
            function(error){
                console.log(error);
            }
        );
  }]
);

messageController.controller('MessageReadCtrl', ['$scope', '$routeParams', 'Message', 'User',
    function($scope, $routeParams, Message, User) {
        Message.get({Id: $routeParams.Id}, 
            function(data){
                $scope.message = data;
                $scope.message.sent_by = User.user.get({Id: data.sent_by});
            },
            function(error){
                console.log(error)
            }
        )
    }]
);

messageController.controller('MessageSendCtrl', ['$scope', '$routeParams', '$location', 'Message', 'User',
  function($scope, $routeParams, $location, Message, User) {

    //Get receiver detail
    User.user.get({Id: $routeParams.user},
        function(data){
            $scope.user = data;
            $scope.reset();
        },
        function(error){
            console.log(error);
        }
    )

    //Send the message
    $scope.send = function() {
        Message.save($scope.message,
            function(data){
                $location.path("messages")
            },
            function(error){
                console.log(error);
            }
        );
    };

    $scope.reset = function() {
        var curUser = User.getUser();

        $scope.message = {
            'sent_by': curUser.id,
            'sent_to': $scope.user.id,
            'subject': '',
            'message': ''
        };
    };
    
  }]
);
