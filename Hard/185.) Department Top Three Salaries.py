"""
SELECT
  Department,
  Employee,
  Salary
FROM (
  SELECT
    de.name AS Department,
    e2.name AS Employee,
    e2.salary AS Salary,
    DENSE_RANK() OVER (PARTITION BY de.id ORDER BY e2.salary DESC) AS rn
  FROM Department AS de
  JOIN Employee AS e2 ON e2.departmentId = de.id
) ranked
WHERE rn <= 3
ORDER BY department, salary DESC;
"""