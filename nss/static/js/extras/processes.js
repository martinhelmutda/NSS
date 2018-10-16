$(document).ready(function() {
  $('#create_description_segment').hide();
  $('#create_rol_segment').hide();

  $('#CreaSig1').on('click', function() {
    // console.log('dfsagsd');
    $('#create_project_segment').hide();
    $('#create_project_segment').removeClass('transition visible');
    $('#create_project_step').removeClass('active');
    $('#create_description_step').addClass('active');
    $('#create_description_segment').transition('fly left');
    $('#create_description_segment').show();
  });

  $( "#CreaPrev1" ).on('click',function() {
    // console.log('NNUBYUNIM');
    $('#create_description_segment').hide();
    $('#create_description_segment').removeClass('transition visible');
    $('#create_description_step').removeClass('active');
    $('#create_project_step').addClass('active');
    $('#create_project_segment').transition('fly right');
    $('#create_project_segment').show();
  });

  $('#CreaSig2').on('click', function() {
    // console.log('dfsagsd');
    $('#create_description_segment').hide();
    $('#create_description_segment').removeClass('transition visible');
    $('#create_description_step').removeClass('active');
    $('#create_rol_step').addClass('active');
    $('#create_rol_segment').transition('fly left');
    $('#create_rol_segment').show();
  });


  $('#CreaPrev2').on('click', function() {
    // console.log('dfsagsd');
    $('#create_rol_segment').hide();
    $('#create_rol_segment').removeClass('transition visible');
    $('#create_rol_step').removeClass('active');
    $('#create_description_step').addClass('active');
    $('#create_description_segment').transition('fly right');
    $('#create_description_segment').show();
  });

  $('#CreaSig3').on('click', function() {
    // console.log('dfsagsd');
    $('.ui.basic.modal').modal('show');
    $('#create_rol_form' ).submit();
    $('#create_project_form' ).submit();
    $('#create_description_form' ).submit();
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

//This is the function that will run every detepicker calendar
$(function() {
  $('input[name="pro_creation_date"]').daterangepicker({
    singleDatePicker: true,
    showDropdowns: true,
  });
});

$(function() {
  $('.ui.dropdown').dropdown();
});
