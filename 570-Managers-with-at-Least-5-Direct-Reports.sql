# Write your MySQL query statement below
SELECT name
FROM Employee e
WHERE (
    SELECT COUNT(*)
    FROM Employee 
    WHERE managerId = e.id
) >= 5;