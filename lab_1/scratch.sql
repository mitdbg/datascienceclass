/* avg. stars per review */
SELECT
        AVG(stars)
FROM
        reviews;

/* agg. over multiple columns at once */
SELECT
        MAX(strftime('%Y', date)) AS max_year,
        MAX(useful + funny + cool) AS max_upvotes,
        MAX(stars) AS max_stars
FROM
        reviews;

/* agg. max upvotes and group by year */
SELECT 
        strftime('%Y', date) AS year,
        MAX(useful + funny + cool) AS max_upvotes
FROM 
        reviews
GROUP BY 
        year;

/* same query as above, but (desc.) order by max_upvotes and limit to first 5 rows */
SELECT 
        strftime('%Y', date) AS year,
        MAX(useful + funny + cool) AS max_upvotes
FROM 
        reviews
GROUP BY 
        year
ORDER BY
        max_upvotes DESC
LIMIT 5;

/* count distinct # of names of users */
SELECT 
        COUNT(DISTINCT name)
FROM 
        users;

/* 4+ star restaurant reviews by users with >= 100 fans */
SELECT 
        b.name AS 'business', r.stars, u.name AS 'influencer'
FROM 
        reviews AS r, businesses AS b, users as u
WHERE
        r.business_id = b.business_id -- Join condition 
        AND r.user_id = u.user_id     -- Join condition
        AND r.stars >= 4
        AND b.categories LIKE '%restaurant%' -- LIKE is case-insensitive by default
        AND u.fans >= 100
ORDER BY
        r.stars DESC
LIMIT 10;
