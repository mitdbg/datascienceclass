
WITH
actors (title_id, person_id, actor_name) AS (
    SELECT c.title_id, c.person_id, p.name 
    FROM crew c, people p
    WHERE p.person_id=c.person_id AND (category='actor' OR category='actress')
    AND c.title_id IN (SELECT t.title_id FROM titles t WHERE t.premiered=2021 AND t.type='movie')
)
    SELECT COUNT(*)
    FROM actors a1, actors a2
    WHERE a1.title_id=a2.title_id AND a1.person_id <> a2.person_id;
