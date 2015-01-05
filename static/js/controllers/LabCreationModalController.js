angular.module('Controllers').controller('LabCreationModalController', labCreationModalHandler);
labCreationModalHandler.$inject = ['$scope', '$modal'];

function labCreationModalHandler($scope, $modal) {
    $scope.showModal = function () {

        $scope.opts = {
            backdrop: 'static',
            keyboard: true,
            templateUrl: 'partials/lab_creation_form.html',
            controller: ModalInstanceCtrl
        };

        var modalInstance = $modal.open($scope.opts);
    };
};

function ModalInstanceCtrl($scope, $modalInstance, $log, ParentLabs, Lab) {
    ParentLabs.get().$promise.then(function (result) {
        $scope.parentLabCandidates = result.objects;
    });

    $scope.newLabFormData = {};


    $scope.submit = function (form) {
        if (form.$valid) {
            $modalInstance.close();
            Lab.save($scope.newLabFormData);
            $(element).bootstrapGrowl("This is a test.");
        }
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};