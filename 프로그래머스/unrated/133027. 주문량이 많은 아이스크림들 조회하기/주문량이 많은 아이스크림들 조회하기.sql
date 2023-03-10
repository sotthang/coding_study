SELECT t1.FLAVOR FROM FIRST_HALF AS `t1`
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS `TOTAL_ORDER` FROM JULY GROUP BY FLAVOR) AS `t2`
ON t1.FLAVOR = t2.FLAVOR
ORDER BY t1.TOTAL_ORDER+t2.TOTAL_ORDER DESC LIMIT 3
;