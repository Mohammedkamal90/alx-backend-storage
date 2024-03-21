-- Task 2: best band ever! - rank country
-- ordered by the number of (non-fans)

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
