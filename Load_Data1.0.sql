SET client_encoding = 'ISO_8859_5';
COPY public."Movies"
FROM 'C:\Users\Public\SQL\Movies.csv'
DELIMITER ',' 
CSV HEADER ;