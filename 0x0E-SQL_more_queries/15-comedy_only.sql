-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
FROM tv_shows AS t
JOIN tv_show_genres AS s
ON t.id = s.show_id
JOIN tv_genres AS g
ON s.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY t.title ASC;
