"""
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee AS e JOIN Department as d ON e.departmentId = d.id
WHERE e.salary IN (
  SELECT MAX(e2.salary)
  FROM Department AS de JOIN Employee AS e2 ON e2.departmentId = de.id
  WHERE de.id = d.id
  GROUP BY de.id, de.name
);
"""