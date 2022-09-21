CREATE TABLE Genre
 AS (
SELECT  "Genre_Temp1".* , "Movies".movie_id
FROM      "Genre_Temp1" LEFT JOIN "Movies"
ON "Movies".title = "Genre_Temp1".title
)