"""
SELECT contest_id, ROUND(100 * COUNT(*) / (SELECT COUNT(*) FROM Users), 2)
AS percentage FROM Register GROUP BY contest_id ORDER BY 2 DESC, 1;
"""