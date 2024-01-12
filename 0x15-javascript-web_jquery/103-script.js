$(document).ready(function () {
  // Function to fetch and display the translation
  function translateHello() {
    // Get the language code from the input field
    const languageCode = $('#language_code').val()

    // Make an AJAX request to the hello API
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode },
      method: 'GET',
      success: function (response) {
        // Display the translation in the #hello div
        $('#hello').text(response.hello)
      },
      error: function () {
        // Handle errors if any
        $('#hello').text('Error fetching translation.')
      },
    })
  }

  // Bind the translateHello function to button click and input enter events
  $('#btn_translate').click(translateHello)
  $('#language_code').keypress(function (event) {
    // Check if the key pressed is Enter (key code 13)
    if (event.which === 13) {
      translateHello()
    }
  })
})
