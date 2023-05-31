#!/usr/bin/node
/* edit html file using jquery click event */
$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('#red_header').css('color', 'red');
  });
});
