"""
SELECT name FROM SalesPerson WHERE sales_id NOT IN
(
    SELECT s.sales_id FROM SalesPerson AS s LEFT JOIN Orders AS o
    ON s.sales_id = o.sales_id LEFT JOIN Company AS c ON c.com_id = o.com_id
    WHERE c.name = "RED"
);
"""