WITH t1 AS	(SELECT r.inventory_id, r.rental_id, DATE_PART('dow', r.rental_date) rental_day_week, DATE_PART('dow', r.return_date) return_day_week
			FROM rental r
			JOIN inventory i
			ON i.inventory_id = r.inventory_id
			JOIN film f
			ON f.film_id = i.film_id
			WHERE return_date IS NOT NULL),
			
	 t2 AS  (SELECT rental_day_week,
			        return_day_week,
			        COUNT(rental_id) OVER(PARTITION BY rental_day_week) AS rental_day_count,
			        COUNT(rental_id) OVER(PARTITION BY return_day_week) AS return_day_count
		     FROM t1
		     ORDER BY 1, 2)
			 
SELECT rental_day_week,
	   return_day_week,
	   rental_day_count,
	   return_day_count
FROM t2
GROUP BY 1, 2, 3, 4
ORDER BY 3 DESC, 4 DESC
