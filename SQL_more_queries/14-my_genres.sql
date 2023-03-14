-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_genres.name ASC;