"""
SELECT a0.machine_id, ROUND(AVG(a1.timestamp - a0.timestamp), 3) AS processing_time
FROM Activity AS a0 JOIN Activity AS a1 ON a0.machine_id = a1.machine_id
AND a0.process_id = a1.process_id
AND a0.activity_type = "start" AND a1.activity_type = "end" GROUP BY a0.machine_id;
"""