"""
WITH acc_queue AS (
  SELECT person_name, weight, turn, SUM(weight) OVER (ORDER BY turn) as acc_weight
  FROM Queue
)

SELECT person_name FROM acc_queue WHERE acc_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
"""