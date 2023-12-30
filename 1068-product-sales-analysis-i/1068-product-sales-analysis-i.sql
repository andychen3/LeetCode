# Write your MySQL query statement below
SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
Join Product
On Sales.product_id = Product.product_id;