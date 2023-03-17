-- LISTING ALL with constraint of name not null
SELECT score, name
FROM second_table
WHERE name <> ''
ORDER BY score DESC;