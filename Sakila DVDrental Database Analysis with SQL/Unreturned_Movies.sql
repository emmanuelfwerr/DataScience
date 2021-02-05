WITH t1 AS	(SELECT r.customer_id
			  	  , c.first_name
				  , c.last_name
				  , cat.name
				  , COUNT(*) OVER(PARTITION BY r.customer_id) AS unreturned_movies
				  , SUM(f.replacement_cost) OVER(PARTITION BY r.customer_id) AS dollars_owed
			 FROM rental r
			 JOIN customer c
			 ON c.customer_id = r.customer_id
			 JOIN inventory i
			 ON i.inventory_id = r.inventory_id
			 JOIN film f
			 ON f.film_id = i.film_id
			 JOIN film_category fc
			 ON fc.film_id = f.film_id
			 JOIN category cat
			 ON cat.category_id = fc.category_id
			 WHERE return_date IS NULL
			 ORDER BY 5 DESC, 6 DESC)

SELECT name Genre, COUNT(*) AS unreturned_movies, SUM(dollars_owed) AS total_owed
FROM t1
GROUP BY 1
ORDER BY 2 DESC
