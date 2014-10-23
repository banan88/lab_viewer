angular.module('Services', ['ngResource']);

angular.module('Services').factory('Lab', labServiceHandler);

function labServiceHandler($resource){
        return $resource('/api/v1/lab/:id');
}
labServiceHandler.$inject = ['$resource'];