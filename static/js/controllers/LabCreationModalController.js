angular.module('Controllers').controller('LabCreationModalController', labCreationModalHandler);
labCreationModalHandler.$inject = ['$scope', '$modal'];

function labCreationModalHandler($scope, $modal) {
    $scope.showModal = function () {

        $scope.opts = {
            backdropClick: true,
            keyboard: true,
            templateUrl: 'partials/lab_creation_form.html',
            controller: ModalInstanceCtrl
        };

        var modalInstance = $modal.open($scope.opts);

        modalInstance.result.then(function () {
            //on ok button press
        }, function () {
            //on cancel button press
            console.log("Modal Closed");
        });
    };
};

function ModalInstanceCtrl($scope, $modalInstance, $log, ParentLabs, Lab) {
    ParentLabs.get().$promise.then(function (result) {
        $scope.parentLabCandidates = result.objects;
    });

    $scope.newLabFormData = {};


    $scope.ok = function () {
        //$modalInstance.close();
       // Lab.save($scope.newLabFormData);
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};