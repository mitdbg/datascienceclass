CREATE TABLE titles_sample AS SELECT * FROM titles WHERE premiered >= 2015;
CREATE TABLE akas_sample AS SELECT * FROM akas o WHERE o.title_id IN (SELECT t.title_id FROM titles_sample t);
CREATE TABLE crew_sample AS SELECT * FROM crew o WHERE o.title_id IN (SELECT t.title_id FROM titles_sample t);
CREATE TABLE episodes_sample AS SELECT * FROM episodes o WHERE o.show_title_id IN (SELECT t.title_id FROM titles_sample t);
-- CREATE TABLE people_sample AS SELECT * FROM people o WHERE o.title_id IN (SELECT t.title_id FROM titles_sample t);
CREATE TABLE ratings_sample AS SELECT * FROM ratings o WHERE o.title_id IN (SELECT t.title_id FROM titles_sample t);


DROP TABLE titles;
DROP TABLE akas;
DROP TABLE crew;
DROP TABLE episodes;
-- DROP TABLE people;
DROP TABLE ratings;

ALTER TABLE titles_sample RENAME TO titles;
ALTER TABLE akas_sample RENAME TO akas;
ALTER TABLE crew_sample RENAME TO crew;
ALTER TABLE episodes_sample RENAME TO episodes;
-- ALTER TABLE people_sample RENAME TO people;
ALTER TABLE ratings_sample RENAME TO ratings;


.headers on
.mode csv

.output titles.csv
SELECT * FROM titles;

.output akas.csv
SELECT * FROM akas;

.output crew.csv
SELECT * FROM crew;

.output episodes.csv
SELECT * FROM episodes;

.output people.csv
SELECT * FROM people;

.output ratings.csv
SELECT * FROM ratings;