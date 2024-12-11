SELECT 
    users.user_id, 
    users.name, 
    COUNT(orders.order_id) AS total_orders, 
    SUM(orders.total_amount) AS total_spent
FROM users
INNER JOIN orders ON users.user_id = orders.user_id
GROUP BY users.user_id, users.name
HAVING COUNT(orders.order_id) > 5 AND SUM(orders.total_amount) > 10000;
