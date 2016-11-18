

(function(){
	var app = angular.module("app", ["xeditable", "ngTagsInput"]);
  //var app = angular.module('rule', ["xeditable"],function($interpolateProvider) {$interpolateProvider.startSymbol('[[').endSymbol(']]');});

  app.controller('NgTagsCtrl', function($scope, $http) {
	$scope.contents = null;
	$http.get('./qa_data.json') //get data
        .success(function(data) {
            $scope.contents = data;
        })
        .error(function(data,status,error,config){
            $scope.contents = [{question:"Error",answers:"Could not load data"}];
        });
	$scope.loadTags = function(query) {	//load answers
		return $http.get('/tags?query=' + query);
	};
	$scope.newrule={"question":"","answers":""}
    $scope.newadd = function()	//add question (not finish)
    {
		$scope.contents.push($scope.newrule);
		$scope.newrule={"question":"","answers":""};
	}
	$scope.data_submit = function(data) 
	{
		$http({
            method: 'POST',
            url: 'test.php',
            data: 
                $scope.contents
            
        })
		.success(function(data, status, headers, config) {
            console.log(data);
            console.log(status);
        })
        .error(function(data, status, headers, config) {
            // Error
        });

	};
});

})();
