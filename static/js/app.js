angular.module('LabViewerApp', ['ngRoute', 'ui.bootstrap', 'Controllers', 'dynform']);

angular.module('LabViewerApp').config(['$routeProvider', routeHandler]);

function routeHandler($routeProvider) {
    $routeProvider
        .when("/", {templateUrl: "partials/all_labs.html", controller: "LabController"})
        .when("/lab/:param", {templateUrl: "partials/lab_details.html", controller: "LabController"});
}