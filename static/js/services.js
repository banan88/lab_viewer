angular.module('Services', ['ngResource']);

angular.module('Services').factory('Lab', labServiceHandler);
angular.module('Services').factory('ParentLabs', parentLabsServiceHandler);
angular.module('Services').factory('Tag', tagServiceHandler);

function labServiceHandler($resource){
        return $resource('/api/v1/lab/:id');
}
labServiceHandler.$inject = ['$resource'];

function parentLabsServiceHandler($resource){
        return $resource('/api/v1/lab?q={"filters": [{"name": "parent_id", "op": "is_null"}]}');
}
parentLabsServiceHandler.$inject = ['$resource'];

function tagServiceHandler($resource){
        return $resource('/api/v1/tag/:id');
}
tagServiceHandler.$inject = ['$resource'];