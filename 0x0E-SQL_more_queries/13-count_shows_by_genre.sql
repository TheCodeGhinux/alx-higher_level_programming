--  lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT n.name AS genre, COUNT(g.genre_id) AS number_of_shows
FROM tv_genres n
INNER JOIN tv_show_genres g
ON n.id = g.genre_id
GROUP BY g.genre_id
ORDER BY number_of_shows DESC;
