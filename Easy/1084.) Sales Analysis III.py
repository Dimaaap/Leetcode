"""
SELECT p.product_id, p.product_name
FROM product AS p
WHERE NOT EXISTS (
  SELECT 1
  FROM Sales AS s
  WHERE s.product_id = p.product_id
    AND s.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31'
) AND p.product_id IN (SELECT product_id FROM Sales);
"""