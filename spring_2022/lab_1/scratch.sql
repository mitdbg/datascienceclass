WITH 
excellent_movies (primary_title, premiered, rating, votes) AS (
        SELECT 
                t.primary_title, t.premiered, r.rating, r.votes
        FROM 
                titles AS t, ratings AS r
        WHERE
                t.title_id = r.title_id -- Join condition 
                AND t.type = 'movie'
                AND r.rating >= 9 AND r.votes >= 100
)
SELECT
        primary_title, premiered, rating, votes,
        RANK() OVER (PARTITION BY premiered ORDER BY rating DESC) AS year_rank
FROM excellent_movies
ORDER BY premiered;