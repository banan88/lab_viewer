angular.module('Services', ['ngResource']);

angular.module('Services').service('LabService', labServiceHandler);

function labServiceHandler(){
    this.getLabs = function(){
        return [1,2,3,4,5];
    };
}