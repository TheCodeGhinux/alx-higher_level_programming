$(document).ready(() => {
  $('#add_item').click(() => {
    const newItem = $('<li>Item</li>')
    $('ul.my_list').append(newItem)
  })
  $('#remove_item').click(() => {
    $('ul.my_list li:last-child').remove()
  })
  $('#clear_list').click(() => {
    $('ul.my_list').empty()
  })
})
