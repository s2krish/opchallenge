'use strict';

/* Services */
var messageServices = angular.module('messageServices', ['ngResource']);

messageServices.factory('Message', ['$resource',
    function($resource) {
        return $resource('api/messages/:Id', {}, {
            query: {method: 'GET', isArray: false}
        });
    }
]);