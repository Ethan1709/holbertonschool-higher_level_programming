$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movie = data.results;
  $.each(movie, function (index, movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
