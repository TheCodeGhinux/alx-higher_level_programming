-- uses the hbtn_0d_tvshows database to
-- lists all genres of the show Dexter.
SELECT n.name AS name
FROM tv_genres AS n
JOIN tv_show_genres AS g
ON g.genre_id = n.id
JOIN tv_shows AS s
ON g.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY n.name ASC;
