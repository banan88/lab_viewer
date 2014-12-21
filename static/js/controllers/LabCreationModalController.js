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

    $scope.formData = {};

    $scope.ok = function () {
        $modalInstance.close();
        $log.info($scope.formData);
        Lab.save($scope.formData).$promise.then(undefined, function (result) {
            alert('an error ocurred when creating lab.');
        });
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};