-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, NAME
FROM cities
WHERE state_id in (
    FROM states WHERE states.name = "California"
)
ORDER BY cities.id DESC;