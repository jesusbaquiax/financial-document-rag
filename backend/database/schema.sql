CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE,
    description VARCHAR(255),
    amount NUMERIC(12,2),
    category VARCHAR(100),
    source_file VARCHAR(255),
    created_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);