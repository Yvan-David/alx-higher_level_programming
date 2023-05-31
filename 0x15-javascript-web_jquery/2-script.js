#!/usr/bin/node
/* edit html file using jquery click event */
$(document).ready(function () {
  $('div').on('click', function () {
    $('#red_header').css('color', 'red');
  });
});
