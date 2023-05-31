#!/usr/bin/node
/* edit html file using jquery click event, addclass, toggleclass mod */
$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
