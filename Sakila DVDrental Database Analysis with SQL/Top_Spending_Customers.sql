WITH t1 AS	(SELECT c.customer_id
				  , c.first_name
				  , c.last_name
				  , COUNT(r.rental_id) AS movies_rented
				  , SUM(p.amount) AS total_spent
				  , DATE_PART('day',MAX(DATE_TRUNC('day',r.rental_date)) - MIN(DATE_TRUNC('day',r.rental_date))) AS active_days
		   	FROM customer c
			JOIN rental r
			ON r.customer_id = c.customer_id
			JOIN payment p
			ON p.rental_id = r.rental_id
			GROUP BY 1, 2, 3
			ORDER BY 4 DESC)
			
SELECT customer_id
	 , first_name
	 , last_name
	 , movies_rented
	 , total_spent
	 , active_days
	 , movies_rented/active_days AS movies_per_day
	 , total_spent/active_days AS dollars_per_day
FROM t1
ORDER BY 7 DESC, 8 DESC
	
