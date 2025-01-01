"""
SELECT customer_number FROM Orders
GROUP BY customer_number HAVING COUNT(customer_number) =
(
    SELECT COUNT(order_number) FROM Orders GROUP BY customer_number
    ORDER BY 1 DESC LIMIT 1
)
"""