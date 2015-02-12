

var MainApp = angular.module("MainApp", [ "ngRoute" ])
  .config(['$locationProvider',  function ($locationProvider) {
    $locationProvider.html5Mode({
      enabled: true
    });
  }
]);


MainApp.config(function($routeProvider){
  $routeProvider
  .when('/',  {
    controller: "mainCtrl",
    templateUrl: "/static/views/top.html",
  })
  .when('/article/:id', {
    controller: "mainCtrl",
    templateUrl: "/static/views/article.html",
  })
  .otherwise({
    redirectTo: "/"
  })
})

MainApp.controller("mainCtrl", function($http, $scope){
  $scope.page_name = "default page";

  var path_str = location.href;
  var path_dict = path_str.split('/');
  var href_length = path_dict.length
  var api_url = "/api/" + path_dict[ href_length -2 ]
               + "/"
               + path_dict[ href_length -1 ];
  $scope.page_id = path_dict[ href_length -1 ];
  $http({
    url: api_url,
    method: 'GET'
  })
  .success(function (data, status, headers, config) {
    console.info( data );
    $scope.json_data = data;
    $scope.page_name = data.page_name;
  })


});
