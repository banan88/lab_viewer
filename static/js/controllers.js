/*module declaration with dependencies*/
angular.module('Controllers', ['Services']);

/*controller declaration*/
angular.module('Controllers').controller('TestController', testControllerHandler);

function testControllerHandler($scope, Lab) {
    $scope.someValue = Lab.get();
};
/*injecting from Services module*/
testControllerHandler.$inject = ['$scope','Lab']

