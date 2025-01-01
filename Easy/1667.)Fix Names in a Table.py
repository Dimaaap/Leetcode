"""
SELECT user_id, CONCAT(UCASE(MID(name, 1, 1)), LCASE(MID(name, 2))) AS name
FROM Users ORDER BY user_id;
"""