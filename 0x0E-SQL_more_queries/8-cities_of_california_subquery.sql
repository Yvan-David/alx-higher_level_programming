-- script that uses subquery to of two rlated tables
SELECT cities.name
FROM cities
WHERE cities.state_id=(SELECT state.id FROM states WHERE name=California);