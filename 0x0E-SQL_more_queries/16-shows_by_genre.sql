-- lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT t.title, n.name
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
ON t.id = s.show_id
LEFT JOIN tv_genres AS n
ON s.genre_id = n.id
ORDER BY t.title ASC, n.name ASC;
