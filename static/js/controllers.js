/*module declaration with dependencies*/
angular.module('Controllers', ['Services']);

angular.module('Controllers').controller('LabController', labControllerHandler);
angular.module('Controllers').controller('TagController', tagControllerHandler);

function labControllerHandler($scope, $rootScope, $routeParams, Lab) { //TODO refactor this
    var labId = $routeParams.param;
    if (labId) {
        Lab.get({id: labId}).$promise.then(function (result) {
            $scope.lab = result;
            $scope.parentNode = Lab.get({id: $scope.lab.parent_id});
            $rootScope.resourceId = labId;
            $rootScope.resourceName = $scope.lab.name;
        });
    } else {
        $scope.labs = Lab.get();
        $rootScope.resourceId = undefined;
        $rootScope.resourceName = undefined;
    }
};
labControllerHandler.$inject = ['$scope', '$rootScope', '$routeParams', 'Lab']

function tagControllerHandler($scope, $routeParams, Tag) {
    var tagId = $routeParams.param;
    if (tagId) {
        $scope.tag = Tag.get({id: tagId});
    } else {
        $scope.tags = Tag.get();
    }
};
tagControllerHandler.$inject = ['$scope', '$routeParams', 'Tag']
