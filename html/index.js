

var app = angular.module("ContentManagement", ['ngSanitize']);


//Controller Part
app.controller("RukuController", function($scope, $http) {

    $scope.content = {};
    _refreshPageData();

    function _refreshPageData() {
        $scope.rukuContent = JSON.parse(atob(rukuContent));
        console.log($scope.rukuContent);
    }

});
