/*module declaration with dependencies*/
angular.module('Controllers', ['Services']);

/*controller declaration*/
angular.module('Controllers').controller('LabController', labControllerHandler);

function labControllerHandler($scope, $routeParams, Lab) {
    var labId = $routeParams.param;
    if (labId) {
        Lab.get({id: labId}).$promise.then(function (result) {
            $scope.lab = result;
            $scope.parentNode = Lab.get({id: $scope.lab.parent_id});
        });
    } else {
        $scope.labs = Lab.get();
    }
};
/*injecting from Services module*/
labControllerHandler.$inject = ['$scope', '$routeParams', 'Lab']

