"""
Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.
"""


"""
SELECT c.name AS Customers 
FROM Customers as c LEFT JOIN Orders as o ON o.customerId = c.id 
WHERE o.id IS NULL;
"""