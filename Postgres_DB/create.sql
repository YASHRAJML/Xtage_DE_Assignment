-- Create the products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price FLOAT,
    stock_available INTEGER
);

-- Create the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    transaction_date DATE,
    total_amount FLOAT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Import the products CSV file
COPY products (product_id, product_name, category, price, stock_available)
FROM 'products.csv'
DELIMITER ','
CSV HEADER;

-- Import the transactions CSV file
COPY transactions (transaction_id, customer_id, product_id, quantity, transaction_date, total_amount)
FROM 'transactions.csv'
DELIMITER ','
CSV HEADER;