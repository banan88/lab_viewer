angular.module('Controllers').controller('LabCreationModalController', labCreationModalHandler);
labCreationModalHandler.$inject = ['$scope', '$modal', '$log'];

function labCreationModalHandler($scope, $modal, $log) {
    $scope.open = function () {

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
}