'use strict';

/* Services */
var userServices = angular.module('userServices', ['ngResource']);

userServices.factory('User', ['$resource',
  function($resource) {
    //return $resource('http://45.63.6.251/api/v1/users/:Id', {Id: "@Id" });

    var user;

    return {
        setUser: function(loggedUser) {
            user = loggedUser;
        },
        getUser: function() {
            return user;
        },
        isLoggedIn : function(){
            return(user)? user : false;
        },
        auth: $resource('api/users/login', {}, {
            login: {method: 'POST'},
            logout: {method: 'DELETE'}
        }),
        me: $resource('api/users/me', {}, {
            check: {method: 'GET'}
        }),
        user: $resource('api/users/:Id', {Id: "@Id" }, {
            query: {method: 'GET'}
        })
    };
  }
]);