-- Count scores in second_table table for a given database
SELECT score, COUNT(score) AS number FROM second_table DESC GROUP BY score;
