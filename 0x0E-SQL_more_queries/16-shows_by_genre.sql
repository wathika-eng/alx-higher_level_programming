-- Results are sorted in ascending order by the show title and genre name.
USE hbtn_0d_tvshows;
SELECT
    tv_shows.title,
    tv_genres.name AS genre
FROM
    hbtn_0d_tvshows.tv_shows
LEFT JOIN
    hbtn_0d_tvshows.show_genres ON tv_shows.id = show_genres.show_id
LEFT JOIN
    hbtn_0d_tvshows.tv_genres ON show_genres.genre_id = tv_genres.id
ORDER BY
    tv_shows.title ASC,
    genre ASC;
