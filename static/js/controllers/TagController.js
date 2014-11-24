angular.module('Controllers').controller('TagController', tagControllerHandler);
tagControllerHandler.$inject = ['$scope', '$routeParams', 'Tag'];

function tagControllerHandler($scope, $routeParams, Tag) {
    var tagId = $routeParams.param;
    if (tagId) {
        $scope.tag = Tag.get({id: tagId});
    } else {
        $scope.tags = Tag.get();
    }
};
