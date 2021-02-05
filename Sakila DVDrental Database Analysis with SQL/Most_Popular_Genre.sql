SELECT c.name Genre, COUNT(r.rental_id) Times_Rented
FROM inventory i
JOIN film f
ON f.film_id = i.film_id
JOIN rental r
ON r.inventory_id = i.inventory_id
JOIN film_category fc
ON fc.film_id = f.film_id
JOIN category c
ON c.category_id = fc.category_id
GROUP BY 1
ORDER BY 2 DESC
