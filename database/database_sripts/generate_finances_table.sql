CREATE TABLE "finances"
(
    transaction_id integer PRIMARY KEY AUTOINCREMENT,
    date_ date NOT NULL,
    description text NOT NULL,
    original_description text NOT NULL,
    amount real NOT NULL,
    transaction_type text NOT NULL,
    category text NOT NULL,
    account_name text NOT NULL,
    labels text,
    notes text
)