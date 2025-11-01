"""
WITH count_less_3 AS (
  SELECT
    query_name,
    COUNT(*) AS count_less
  FROM queries
  WHERE rating < 3
  GROUP BY query_name
)
SELECT
  q.query_name,
  ROUND( AVG(q.rating::NUMERIC / q.position), 2 ) AS quality,
  ROUND( (coalesce(cl.count_less, 0)::NUMERIC / COUNT(*)) * 100, 2 ) AS poor_query_percentage
FROM queries q
LEFT JOIN count_less_3 cl
  ON q.query_name = cl.query_name
GROUP BY q.query_name, cl.count_less
ORDER BY q.query_name;
"""