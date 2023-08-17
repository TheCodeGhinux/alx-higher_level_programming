-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN
      (SELECT j.title
      FROM tv_shows AS j
      JOIN tv_show_genres AS k
      ON j.id = k.show_id
      JOIN tv_genres AS l
      ON k.genre_id = l.id
      WHERE l.name = 'Comedy')
ORDER BY tv_shows.title ASC;
