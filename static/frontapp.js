var app = angular.module('myfrontapp', []);

app.controller('myMainCtrl', function($scope, $http) {


  // var stringConstructor = "test".constructor;
  // var arrayConstructor = [].constructor;
  var objectConstructor = {}.constructor;

  function whatIsIt(object) {
      if (object === null) {
          return "null";
      }
      else if (object === undefined) {
          return "undefined";
      }
      // else if (object.constructor === stringConstructor) {
      //     return "String";
      // }
      // else if (object.constructor === arrayConstructor) {
      //     return "Array";
      // }
      else if (object.constructor == objectConstructor) {
          return "Object";
      }
      else {
          return "don't know";
      }
  }

  $scope.HitApi=function(url,method){


        if (method=="PUT"){
          payload={
            method: method,
            data:$scope.apibody,
            url:url
          }
        }else if (method=="GET") {
          payload={
            method: method,
            url:url
          }
        }

        console.log(method);
        $http(payload).then(function successCallback(response) {
          // this callback will be called asynchronously
          // when the response is available
          $scope.status=response.status;
          $scope.config=JSON.stringify(response.config,undefined,4);
          $scope.apiresponse=JSON.stringify(response.data,undefined,4);
          mytest($scope);
        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          $scope.status=response.status;
          $scope.config=JSON.stringify(response.config,undefined,4);
          $scope.apiresponse=JSON.stringify(response.data,undefined,4);
          mytest($scope);
        });
  }
  function isJSON(str) {
      try {
          JSON.parse(str);
      } catch (e) {
          return false;
      }
      return true;
  }
  $scope.apibody = {
    "client": "abk1",
    "id": 2
};
  $scope.apibodyjson = angular.toJson($scope.apibody);



  $scope.update = function() {
    if(isJSON($scope.apibodyjson)){
            $scope.apibody = angular.fromJson($scope.apibodyjson);
            $scope.myjsonvalidationmessage="Valid JSON";
          }else{
          $scope.myjsonvalidationmessage="Invalid JSON";
        }
    }
});




var mytest=function($scope){
  $scope.apitest="";
  if($scope.status==200){
    $scope.apitest=$scope.apitest + "\nTest case :validate status code is Passed with status :" + $scope.status;
  }else{
    $scope.apitest=$scope.apitest + "\nTest case :validate status code is Failed with status :" + $scope.status;
  }
  var textfind=$scope.apiresponse.search("name");
  if (textfind>-1){
      $scope.apitest=$scope.apitest + "\nTest case :validate mentioned text present is Passed";
  }else{
      $scope.apitest=$scope.apitest + "\nTest case :validate mentioned text present is Failed";
  }
}
