-- Write your query below
SELECT employee_id,
        Case
            WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
            ELSE 0
        END AS bonus
FROM employees
ORDER BY employee_id;