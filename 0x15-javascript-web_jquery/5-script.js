#!/usr/bin/node
/* edit html file using jquery click event, addclass mod */
$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
