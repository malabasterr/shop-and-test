CREATE DATABASE foundation_assessment_ii;

USE foundation_assessment_ii;

CREATE TABLE movie_info (
    Movie_ID INT NOT NULL,
    Movie_Name VARCHAR(50) NOT NULL,
    Movie_Length TIME(0),
    Age_Rating VARCHAR(3),
	PRIMARY KEY (Movie_ID)
);

CREATE TABLE screens (
    Screen_ID INT NOT NULL,
    Four_K BOOLEAN,
	PRIMARY KEY (Screen_ID)
);

CREATE TABLE showings (
    Showing_ID INT NOT NULL,
    Movie_ID INT NOT NULL,
    Screen_ID INT NOT NULL,
    Start_Time TIME(0),
    Available_Seats INT,
	PRIMARY KEY (Showing_ID)
)