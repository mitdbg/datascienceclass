        SELECT 
                t.primary_title, t.premiered, r.rating, r.votes
        FROM 
                titles AS t, ratings AS r
        WHERE
                t.title_id = r.title_id -- Join condition 
                AND t.type = 'movie'
                AND r.rating >= 9 AND r.votes >= 100
        ORDER BY
            r.rating DESC
        LIMIT 10;