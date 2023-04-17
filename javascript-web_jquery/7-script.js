$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const name = data.name;
  $('#character').text(name);
});
