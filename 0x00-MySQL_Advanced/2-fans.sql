-- rank country origin of bands ordered by number of fans
SELECT origin, 0 + fans AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans
