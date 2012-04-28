$(document).ready(function(){
  var $container = $('#container');
  $container.imagesLoaded(function(){
	  $('#container').masonry({
		  itemSelector : '.cloudcast',
		  columnWidth : 300,
		  isFitWidth: true
	  });
  });
});