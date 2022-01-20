SELECT
        MAX(premiered),
        MAX(runtime_minutes),
        COUNT(DISTINCT genres) AS num_genres -- Compute the number of unique genres.
FROM
        titles;
