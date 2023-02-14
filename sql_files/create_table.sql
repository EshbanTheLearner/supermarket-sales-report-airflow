CREATE TABLE IF NOT EXISTS
supermarket_sales(
    Invoice_ID varchar(50),
    Branch varchar(50),
    City varchar(50),
    Customer_type varchar(50),
    Gender varchar(50),
    Product_line varchar(50),
    Unit_price float,
    Quantity int,
    Tax_5_percent float,
    Total float,
    Date date,
    Time varchar(50),
    Payment float,
    cogs float,
    gross_margin_percentage float,
    gross_income float,
    Rating float
);