-- ============================================================
-- USERS
-- ============================================================

INSERT INTO users (id, email, name, password)
VALUES
(
    '11111111-1111-1111-1111-111111111111',
    'john.doe@example.com',
    'John Doe',
    '$2b$12$dummyhashedpassword'
)
ON CONFLICT (email) DO NOTHING;


-- ============================================================
-- TRANSACTIONS
-- July 2026
-- ============================================================

INSERT INTO transactions
(user_id, date, type, amount, currency, description, merchant, category)
VALUES

-- Income
(
'11111111-1111-1111-1111-111111111111',
'2026-07-01',
'CREDIT',
6500.00,
'USD',
'Monthly Salary',
'ABC Technologies',
'Income'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-15',
'CREDIT',
250.00,
'USD',
'Freelance Payment',
'Upwork',
'Income'
),

-- Housing
(
'11111111-1111-1111-1111-111111111111',
'2026-07-02',
'DEBIT',
2100.00,
'USD',
'Monthly Rent',
'Sunset Apartments',
'Housing'
),

-- Groceries
(
'11111111-1111-1111-1111-111111111111',
'2026-07-03',
'DEBIT',
148.72,
'USD',
'Weekly Groceries',
'Costco',
'Groceries'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-11',
'DEBIT',
84.33,
'USD',
'Groceries',
'Trader Joe''s',
'Groceries'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-20',
'DEBIT',
96.45,
'USD',
'Groceries',
'Whole Foods',
'Groceries'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-28',
'DEBIT',
105.90,
'USD',
'Groceries',
'Safeway',
'Groceries'
),

-- Dining
(
'11111111-1111-1111-1111-111111111111',
'2026-07-04',
'DEBIT',
17.45,
'USD',
'Coffee',
'Starbucks',
'Dining'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-09',
'DEBIT',
32.50,
'USD',
'Lunch',
'Chipotle',
'Dining'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-17',
'DEBIT',
68.90,
'USD',
'Dinner',
'Olive Garden',
'Dining'
),

-- Transportation
(
'11111111-1111-1111-1111-111111111111',
'2026-07-05',
'DEBIT',
62.40,
'USD',
'Fuel',
'Shell',
'Transportation'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-19',
'DEBIT',
59.80,
'USD',
'Fuel',
'Chevron',
'Transportation'
),

-- Utilities
(
'11111111-1111-1111-1111-111111111111',
'2026-07-06',
'DEBIT',
89.65,
'USD',
'Internet Bill',
'Xfinity',
'Utilities'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-08',
'DEBIT',
118.20,
'USD',
'Electricity Bill',
'PG&E',
'Utilities'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-10',
'DEBIT',
42.15,
'USD',
'Water Bill',
'City Utilities',
'Utilities'
),

-- Entertainment
(
'11111111-1111-1111-1111-111111111111',
'2026-07-12',
'DEBIT',
15.99,
'USD',
'Netflix Subscription',
'Netflix',
'Entertainment'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-13',
'DEBIT',
11.99,
'USD',
'Spotify Premium',
'Spotify',
'Entertainment'
),

-- Shopping
(
'11111111-1111-1111-1111-111111111111',
'2026-07-18',
'DEBIT',
129.99,
'USD',
'Wireless Mouse',
'Amazon',
'Shopping'
),

(
'11111111-1111-1111-1111-111111111111',
'2026-07-22',
'DEBIT',
89.50,
'USD',
'Clothing',
'Target',
'Shopping'
),

-- Healthcare
(
'11111111-1111-1111-1111-111111111111',
'2026-07-24',
'DEBIT',
35.00,
'USD',
'Prescription',
'CVS Pharmacy',
'Healthcare'
),

-- Travel
(
'11111111-1111-1111-1111-111111111111',
'2026-07-26',
'DEBIT',
120.00,
'USD',
'Weekend Trip',
'Uber',
'Travel'
);