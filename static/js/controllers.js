/*module declaration with dependencies*/
angular.module('Controllers', ['Services']);

/*controller declaration*/
angular.module('Controllers').controller('TestController', testControllerHandler);

function testControllerHandler($scope, LabService) {
    $scope.someValue = LabService.getLabs();
};
/*injecting from Services module*/
testControllerHandler.$inject = ['$scope','LabService']

