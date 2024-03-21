-- Task 2: best band ever! - rank country

SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
