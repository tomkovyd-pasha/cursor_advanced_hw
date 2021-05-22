-- modify table products add user_id as foreign key

ALTER TABLE products
ADD COLUMN user_id INT NOT NULL;

UPDATE products
SET user_id = 1 
WHERE id = 1;

ALTER TABLE products
ADD FOREIGN KEY (user_id) REFERENCES users(id);

-- select users their products, categories and images

USE shop;

SELECT 
	CONCAT(u.first_name, ' ', u.last_name) AS user_full_name 
    ,p.meta_title
    ,c.meta_title
    ,pi.file
FROM
	users u 
	JOIN products p ON u.id = p.user_id
	JOIN categories_products cp ON p.id = cp.product_id
	JOIN categories c ON cp.category_id = c.id
	JOIN product_images pi ON p.id = pi.product_id


