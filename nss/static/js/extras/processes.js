$(document).ready(function() {
  $('#create_description_segment').hide();
  $('#create_rol_segment').hide();

  $('#CreaSig1').on('click', function() {
    // console.log('dfsagsd');
    $('#create_project_segment').hide();
    $('#create_project_segment').removeClass('transition visible');
    $('#create_description_segment').transition('fly left');
    $('#create_description_segment').show();
  });

  $( "#CreaPrev1" ).on('click',function() {
    // console.log('NNUBYUNIM');
    $('#create_description_segment').hide();
    $('#create_description_segment').removeClass('transition visible');
    $('#create_project_segment').transition('fly right');
    $('#create_project_segment').show();
  });

  $('#CreaSig2').on('click', function() {
    // console.log('dfsagsd');
    $('#create_description_segment').hide();
    $('#create_description_segment').removeClass('transition visible');
    $('#create_rol_segment').transition('fly left');
    $('#create_rol_segment').show();
  });


  $('#CreaPrev2').on('click', function() {
    // console.log('dfsagsd');
    $('#create_rol_segment').hide();
    $('#create_rol_segment').removeClass('transition visible');
    $('#create_description_segment').transition('fly right');
    $('#create_description_segment').show();
  });


  $('.submit').one('click', function(p) {
    p.preventDefault();
    // $('#personal').stop();
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


$(function() {
  $('.ui.dropdown').dropdown();
});
