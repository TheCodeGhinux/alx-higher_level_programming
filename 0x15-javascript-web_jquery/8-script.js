$.get('https://swapi.co/api/films/?format=json', function (res) {
  $('UL#list_movies').append(
    ...res.results.map((data) => `<li>${data.title}</li>`)
  )
})
