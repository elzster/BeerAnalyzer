drop table brew_data;
--brewery_id	brewery_name	review_time	review_overall	review_aroma	review_appearance	
-- review_profilename	beer_style	review_palate	review_taste	beer_name	beer_abv	beer_beerid

CREATE TABLE brew_data(
	id serial primary key,
	brewery_id varchar,
	brewery_name varchar,
	review_time timestamp,
	review_overall double precision, 
	review_aroma varchar,
	review_appearance varchar,
	review_profilename varchar,
	beer_style varchar,
	review_palate varchar,
	review_taste varchar,
	beer_name varchar,
	beer_abv double precision,
	beer_beerid varchar
);

SELECT * FROM brew_data
limit 10;


SELECT *
FROM pg_settings
WHERE name = 'port';