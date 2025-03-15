# SQL Basics

## Selecting Data

### Selecting All Fields
```sql
SELECT * FROM customers;
```
This command retrieves **all fields** from the `customers` table.

### Selecting Specific Fields
```sql
SELECT name FROM artists;
```
This command retrieves only the `name` field from the `artists` table.

```sql
SELECT FirstName, LastName FROM customers;
```
This command retrieves the `FirstName` and `LastName` fields from the `customers` table.

### Renaming Selected Fields
```sql
SELECT FirstName AS customer_firstname, LastName AS customer_lastname FROM customers;
```
This command retrieves `FirstName` and `LastName` fields but renames them as `customer_firstname` and `customer_lastname` in the output.

## Filtering Data

### Filtering by ID
```sql
SELECT * FROM customers WHERE CustomerId = 1;
```
This command retrieves **all fields** from the `customers` table where `CustomerId` is equal to `1`.

### Filtering by Country
```sql
SELECT FirstName, LastName FROM customers WHERE Country = 'Canada';
```
This command retrieves `FirstName` and `LastName` fields only for customers whose `Country` is `Canada`.

## Combining Filters

### Using AND Condition
```sql
SELECT * FROM customers WHERE Country = 'Canada' AND State = 'ON';
```
This command retrieves **all fields** from the `customers` table where both conditions are met: `Country` is `Canada` **and** `State` is `ON`.

### Using OR Condition
```sql
SELECT * FROM customers WHERE Country = 'Canada' OR Country = 'USA';
```
This command retrieves **all fields** from the `customers` table where the `Country` is either `Canada` **or** `USA`.

## Sorting Results

### Ordering in Ascending Order
```sql
SELECT * FROM customers WHERE Country = 'Canada' OR Country = 'USA' ORDER BY FirstName;
```
This command retrieves **all fields** from the `customers` table where the `Country` is either `Canada` **or** `USA`, and sorts the results in **ascending order** based on `FirstName`.

### Ordering in Descending Order
```sql
SELECT * FROM customers WHERE Country = 'Canada' OR Country = 'USA' ORDER BY CustomerId DESC;
```
This command retrieves **all fields** from the `customers` table where the `Country` is either `Canada` **or** `USA`, and sorts the results in **descending order** based on `CustomerId`.

## Limiting Results

### Limiting the Number of Rows
```sql
SELECT * FROM customers WHERE Country = 'Canada' OR Country = 'USA' ORDER BY CustomerId DESC LIMIT 5;
```
This command retrieves **all fields** from the `customers` table where the `Country` is either `Canada` **or** `USA`, sorts the results in **descending order** based on `CustomerId`, and **limits** the output to the top `5` rows.
