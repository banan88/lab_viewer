angular.module('Controllers').controller('LabController', labControllerHandler);
labControllerHandler.$inject = ['$scope', '$rootScope', '$routeParams', 'Lab'];

function labControllerHandler($scope, $rootScope, $routeParams, Lab) {
    var labId = $routeParams.param;
    if (labId) {
        updateBreadcrumbsLink($scope, $rootScope, Lab, labId);
    } else {
        $scope.labs = Lab.get();
    }
};

function updateBreadcrumbsLink($scope, $rootScope, Lab, labId) {
    Lab.get({id: labId}).$promise.then(function (result) {
        $scope.lab = result;
        $scope.parentNode = Lab.get({id: $scope.lab.parent_id});
        $rootScope.resourceId = labId;
        $rootScope.resourceName = $scope.lab.name;
    });
};

