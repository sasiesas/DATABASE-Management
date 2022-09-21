-- Table: public.Movies

-- DROP TABLE IF EXISTS public."Movies";

CREATE TABLE IF NOT EXISTS public."Sales.temp"
(
    Movie_ID integer,
    year date,
    release_date VARCHAR,
    title VARCHAR,
    genre VARCHAR,
	international_box_office INTEGER,
	domestic_box_office integer,
	worldwide_box_office BIGINT,
	production_budget INTEGER,
	opening_weekend INTEGER,
	theatre_count INTEGER,
	avg_run_per_theatre FLOAT,
	runtime INTEGER,
	keywords VARCHAR,
	creative_type VARCHAR,
	url VARCHAR,
	PRIMARY KEY (Movie_ID)

)
