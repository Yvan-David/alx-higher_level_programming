#!/usr/bin/node
/* edit html file using jquery click event, append mod, html */
$(document).ready(function () {
  $('DIV#update_header').on('click', function (e) {
    $('header').html('New Header!!!');
  });
});
