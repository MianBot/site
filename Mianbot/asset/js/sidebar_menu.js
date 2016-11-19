$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");

        $("#sidebar-brand").toggleClass("brand-center");
        $("#logo").toggleClass("brand-title-mini");
        $("#logo-remain").toggleClass("hide");

        $("#sidebar-panel").toggleClass("sidebar-padding");
    });
 $("#menu-toggle-2").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled-2");

    $("#sidebar-brand").toggleClass("brand-center");
    $("#logo").toggleClass("brand-title-mini");
    $("#logo-remain").toggleClass("hide");

    $("#sidebar-panel").toggleClass("sidebar-padding");
    $('#menu ul').hide();
});

 function initMenu() {
  $('#menu ul').hide();
  $('#menu ul').children('.current').parent().show();
  //$('#menu ul:first').show();
  $('#menu li a').click(
    function() {
      var checkElement = $(this).next();
      if((checkElement.is('ul')) && (checkElement.is(':visible'))) {
        return false;
        }
      if((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
        $('#menu ul:visible').slideUp('normal');
        checkElement.slideDown('normal');
        return false;
        }
      }
    );
  }
$(document).ready(function() {initMenu();});
