-- Results are sorted in ascending order by the show title
USE hbtn_0d_tvshows;
SELECT
    tv_shows.title
FROM
    hbtn_0d_tvshows.tv_shows
JOIN
    hbtn_0d_tvshows.show_genres ON tv_shows.id = show_genres.show_id
JOIN
    hbtn_0d_tvshows.tv_genres ON show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = 'Comedy'
ORDER BY
    tv_shows.title ASC;
