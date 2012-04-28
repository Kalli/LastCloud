$(document).ready(function(){
  var $container = $('#container');
  $container.imagesLoaded(function(){	
    $('#container').masonry({
   	  // options
   	  itemSelector : '.artist',
   	  columnWidth : 252,
		  isFitWidth: true
    });
  });
});