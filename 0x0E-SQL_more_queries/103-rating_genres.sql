-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating
FROM tv_genres AS g
JOIN tv_show_genres AS s
ON g.id = s.genre_id
JOIN tv_show_ratings AS r
ON s.show_id = r.show_id
GROUP BY g.name
ORDER BY rating DESC;
