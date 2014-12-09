angular.module('Controllers').controller('LabCreationModalController', labCreationModalHandler);
labCreationModalHandler.$inject = ['$scope', '$modal', '$log', 'ParentLabs'];

function labCreationModalHandler($scope, $modal, $log, ParentLabs) {
    $scope.labCreationForm = {};
    $scope.saveLab = saveLab($scope, $log);
    $scope.openModal = openModal($scope, $modal, $log);
    $scope.parentLabs = ParentLabs.get();
}

function openModal($scope, $modal, $log) {
    return function () {
        var modalInstance = $modal.open({
            templateUrl: 'partials/lab_creation_form.html',
            /*controller: 'ModalInstanceCtrl',*/
            resolve: {
                items: function () {
                    return $scope.items;
                }
            }
        });

        modalInstance.result.then(function (selectedItem) {
            $scope.selected = selectedItem;
        }, function () {
            $log.info('Modal dismissed at: ' + new Date());
        });
    };
};

function saveLab($scope, $log) {
    return function () {
        $log.info('saveLab called, labname: '
            + $scope.labCreationForm.name + 'parent_id: ' + $scope.labCreationForm.parent_id);
        $log.info($scope.parentLabs);
    };
};