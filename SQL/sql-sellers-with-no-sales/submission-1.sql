-- Write your query below
SELECT seller.seller_name FROM seller
WHERE seller.seller_id NOT IN(SELECT orders.seller_id FROM orders WHERE orders.sale_date >= DATE '2020-01-01'
AND orders.sale_date <  DATE '2021-01-01')
ORDER BY(seller.seller_name);

-- SELECT s.seller_name
-- FROM Seller s
-- WHERE s.seller_id NOT IN (
--     SELECT o.seller_id
--     FROM Orders o
--     WHERE YEAR(o.sale_date) = 2020
-- )
-- ORDER BY s.seller_name;