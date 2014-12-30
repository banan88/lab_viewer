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

    $scope.formTemplate = [
        {
            "type": "text",
            "label": "Lab name",
            "model": "name",
            "placeholder": "lab name",
            "display": "block;",
            "minLength":"3",
            "attributes": {
                "data-ng-required":"true"
            }
        },
        {
            "type": "submit",
            "callback": "ok()",
            "label": "Create",
            "disabled" : "labForm.$invalid",
            "attributes": {
                "class": "btn btn-success"
            }
        },
        {
            "type": "submit",
            "callback": "cancel()",
            "label": "Cancel",
            "attributes": {
                "class": "btn btn-warning"
            }
        }
    ];

    $scope.ok = function () {
        //$modalInstance.close();
        Lab.save($scope.formData);
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
};