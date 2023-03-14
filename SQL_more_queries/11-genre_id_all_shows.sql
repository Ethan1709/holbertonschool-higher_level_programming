-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
LEFT JOIN WHERE tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;