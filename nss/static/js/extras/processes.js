$(document).ready(function() {
  var ct = 0;

  $('.next1').one('click', function(e) {
    e.preventDefault();
    $('#account').animate('slow', function() {
      if (ct > 0) {
        $('#account').removeClass('transition visible');
        $('#account').addClass('transition hidden');
      }
      $('#account').css('display', 'none');
      $('#accountS').addClass('disabled');
      $('#socialP').removeClass('disabled');
      $('#socialP').addClass('active');
      $("#social").transition('fly right');
      // $('body').css('background-color', '#06000a');
      $('#social button').removeClass('inverted violet');
      $('#social button').addClass('inverted blue');
      ct++;
    });
  });


  $('.prev1').one('click', function(e) {
    e.preventDefault();
    $('#personal').animate('slow', function() {

      $('#social').transition('hide');
      $('#socialP').addClass('disabled');
      $('#accountS').removeClass('disabled');
      $('#accountS').addClass('active');
      $("#account").transition('fly left');
      // $('body').css('background-color', '#06000a');
      $('#social button').removeClass('inverted violet');
      $('#social button').addClass('inverted blue');
      ct++;
    });
  });

  $('.next2').one('click', function(e) {
    e.preventDefault();
    $('#personal').animate('slow', function() {
      if (ct > 0) {
        $('#personal').removeClass('transition visible');
        $('#personal').addClass('transition hidden');
      }
      $('#social').transition('hide');
      $('#socialP').addClass('disabled');
      $('#details').removeClass('disabled');
      $('#details').addClass('active');
      $("#personal").transition('fly right');
      // $('body').css('background-color', '#06000a');
      $('#social button').removeClass('inverted violet');
      $('#social button').addClass('inverted blue');
      ct++;
    });
  });


  $('.prev2').one('click', function(e) {
    e.preventDefault();
    $('#social').animate('slow', function() {
      // if (ct > 0) {
      //   $('#social').removeClass('transition visible');
      //   $('#social').addClass('transition hidden');
      // }
      $('#personal').transition('hide');
      $('#details').addClass('disabled');
      $('#socialP').removeClass('disabled');
      $('#socialP').addClass('active');
      $("#social").transition('fly left');
      // $('body').css('background-color', '#06000a');
      $('#social button').removeClass('inverted violet');
      $('#social button').addClass('inverted blue');
      ct++;
    });
  });

  $('.submit').one('click', function(p) {

    p.preventDefault();

    $('#personal').stop();
  });
  // fix main menu to page on passing
  $('.main.menu').visibility({
    type: 'fixed'
  });
  $('.overlay').visibility({
    type: 'fixed',
    offset: 80
  });

  // lazy load images
  $('.image').visibility({
    type: 'image',
    transition: 'vertical flip in',
    duration: 500
  });

  // show dropdown on hover
  $('.main.menu  .ui.dropdown').dropdown({
    on: 'click'
  });

});
