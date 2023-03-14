-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.title = tv_show_genres.show_id
ORDER BY number_of_shows DESC;