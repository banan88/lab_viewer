angular.module('LabViewerApp', ['Controllers', 'ngRoute']);

angular.module('LabViewerApp').config(['$routeProvider', routeHandler]);

function routeHandler($routeProvider) {
    $routeProvider
        .when("/", {templateUrl: "partials/all_labs.html", controller: "LabController"});
}