--  uses the hbtn_0d_tvshows database to list
-- all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
      (SELECT g.name AS name
      FROM tv_genres AS g
      JOIN tv_show_genres AS s
      ON s.genre_id = g.id
      JOIN tv_shows AS t
      ON s.show_id = t.id
      WHERE t.title = 'Dexter')
ORDER BY tv_genres.name ASC;
