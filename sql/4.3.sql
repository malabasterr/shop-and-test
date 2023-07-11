SELECT movie_info.Movie_Name
FROM showings
INNER JOIN movie_info ON showings.Movie_ID = movie_info.Movie_ID
INNER JOIN screens ON showings.Screen_ID = screens.Screen_ID
GROUP BY movie_info.Movie_Name
HAVING COUNT(showings.Movie_ID) = (
    SELECT MAX(counts.showings_count)
    FROM (
        SELECT COUNT(showings.Movie_ID) AS showings_count
        FROM showings
        INNER JOIN movie_info ON showings.Movie_ID = movie_info.Movie_ID
        INNER JOIN screens ON showings.Screen_ID = screens.Screen_ID
        GROUP BY movie_info.Movie_Name
    ) AS counts
);