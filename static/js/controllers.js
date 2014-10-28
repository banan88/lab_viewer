/*module declaration with dependencies*/
angular.module('Controllers', ['Services']);

/*controller declaration*/
angular.module('Controllers').controller('LabController', labControllerHandler);

function labControllerHandler($scope, Lab) {
    $scope.labs = Lab.get();
};
/*injecting from Services module*/
labControllerHandler.$inject = ['$scope','Lab']

