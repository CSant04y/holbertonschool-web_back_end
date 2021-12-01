-- This SQL script country of origin for bands
-- Ordered by country of origin and fans in non-unique
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;