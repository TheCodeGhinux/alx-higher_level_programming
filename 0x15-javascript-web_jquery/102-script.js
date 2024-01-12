$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val()
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: languageCode },
      method: 'GET',
      success: (response) => {
        $('#hello').text(response.hello)
      },
      error: () => {
        $('#hello').text('Error fetching translation.')
      },
    })
  })
})

