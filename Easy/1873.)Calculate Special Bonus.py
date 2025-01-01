"""
SELECT employee_id,
CASE
    WHEN MOD(employee_id, 2) != 0 AND MID(name, 1, 1) != "M" THEN salary
    ELSE 0
END as bonus
FROM Employees ORDER BY 1;
"""