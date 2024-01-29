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
        r.stars DESC,
        b.name ASC
LIMIT 10;


/* same query as above, but using CTEs */
WITH 
good_reviews AS ( -- Precompute 4+ star reviews
        SELECT review_id, business_id, user_id, stars, text
        FROM reviews
        WHERE stars >= 4
),
restaurants AS ( -- Precompute restaurants
        SELECT business_id, name AS 'business'
        FROM businesses
        WHERE categories LIKE '%restaurant%'
),
influencers AS ( -- Precompute influencers
        SELECT user_id, name AS 'influencer'
        FROM users
        WHERE fans >= 100
)

SELECT business, stars, influencer  -- Join them.
FROM good_reviews AS gr, restaurants AS r, influencers as i
WHERE gr.business_id = r.business_id AND gr.user_id = i.user_id
ORDER BY stars DESC, business ASC
LIMIT 10;

/* use window function to compute rank w/in each year */
WITH 
good_restaurants (business, stars, year) AS (
        SELECT 
                b.name AS 'business', r.stars, strftime('%Y', r.date) AS year
        FROM 
                reviews as r, businesses AS b, users AS u
        WHERE
                r.business_id = b.business_id AND r.user_id = u.user_id -- Join condition 
                AND r.stars >= 4
                AND b.categories LIKE '%restaurant%'
                AND u.fans >= 100
)
SELECT
        business, stars, year,
        RANK() OVER (PARTITION BY year ORDER BY stars DESC, business ASC) as year_rank
FROM good_restaurants
ORDER BY year;
