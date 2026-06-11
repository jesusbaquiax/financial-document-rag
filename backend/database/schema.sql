-- table creation SQL

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL,
    description VARCHAR(255) NOT NULL,
    amount NUMERIC(12,2) NOT NULL,
    category VARCHAR(100),
    source_file VARCHAR(255),
    created_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);