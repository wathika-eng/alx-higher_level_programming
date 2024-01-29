-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
USE hbtn_0d_tvshows;
SELECT 
        tv_shows.title
        COALESCE(tv_shows_genres.genre_id, NULL) as genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tgenre_id ASC;