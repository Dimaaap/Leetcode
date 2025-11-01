"""
SELECT name FROM employee WHERE id IN (
  SELECT managerid FROM Employee
  GROUP BY managerid HAVING COUNT(*) >= 5
);
"""