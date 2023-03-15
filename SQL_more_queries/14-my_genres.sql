-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_shows, tv_genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.id
ORDER BY tv_genres.name ASC;