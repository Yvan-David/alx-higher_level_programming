-- list order by score >= 10
SELECT score, name
FROM second_table
ORDER BY score
WHERE score >= 10