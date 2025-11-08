"""
SELECT name AS results FROM (
    SELECT u.name
    FROM MovieRating as mr JOIN Users as u ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name ORDER BY COUNT(mr.movie_id) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
SELECT title FROM (
    SELECT m.title FROM MovieRating AS mr JOIN Movies as m ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);
"""