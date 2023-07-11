SELECT movie_info.Movie_Name, showings.Start_Time 
FROM (( showings
INNER JOIN movie_info ON showings.Movie_ID = movie_info.Movie_ID)
INNER JOIN screens ON showings.Screen_ID = screens.Screen_ID)
WHERE showings.Start_Time > "12:00:00" AND showings.Available_Seats >= 1 ORDER BY showings.Start_Time ASC