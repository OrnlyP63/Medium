[tutorial](https://www.sqlitetutorial.net/)

---
# SQL basics
## Example 1:
```sql
SELECT * FROM customers;
```
This command means getting **all feilds** from **table**.

## Example 2:
```sql
SELECT name FROM artists;
```

```sql
SELECT FirstName, LastName FROM customers;
```
This command means getting **any feilds** from **table**.

```sql
SELECT 
	FirstName AS customer_firstname, 
	LastName AS customer_lastname
FROM customers;
```
This command means getting **any feilds** from **table** by name defining.

## Example 3:
```sql
SELECT * FROM customers
WHERE CustomerId = 1;
```

This command means getting **all feilds** from **table** by feilds filtering.

```sql
SELECT FirstName, LastName FROM customers
WHERE CustomerId = 1;
```

```sql
SELECT FirstName, LastName FROM customers
WHERE Country = 'Canada';
```

```sql
SELECT 
	CustomerId, FirstName, LastName, Address 
FROM customers
WHERE CustomerId <= 10;
```
This command means getting **any feilds** from **table** by feilds filtering.

## Example 4

```sql
SELECT * FROM customers
WHERE Country = 'Canada' AND State = 'ON';
```

This command means getting **all feilds** from **table** by *filter 1* **and** *filter 2*.

```sql
SELECT * FROM customers
WHERE Country = 'Canada' OR Country = 'USA';
```

This command means getting **all feilds** from **table** by *filter 1* **or** *filter 2*.


## Example 5

```sql
SELECT * FROM customers
WHERE Country = 'Canada' OR Country = 'USA'
ORDER BY FirstName;
```
This command means getting **all feilds** from **table** by *filter 1* **or** *filter 2* and order (ascending) the table by some feilds.

```sql
SELECT * FROM customers
WHERE Country = 'Canada' OR Country = 'USA'
ORDER BY CustomerId DESC;
```
This command means getting **all feilds** from **table** by *filter 1* **or** *filter 2* and order (descending) the table by some feilds.

## Example 6
```sql
SELECT * FROM customers
WHERE Country = 'Canada' OR Country = 'USA'
ORDER BY CustomerId DESC
LIMIT 5;

```
This command means getting **all feilds** from **table** by *filter 1* **or** *filter 2* and order (descending) the table by some feilds. Also, the table rows are limited by any number.

---

## Example 7
```sql
INSERT INTO customers
VALUES(
	60,
	'Phiphat',
	'Chomchit',
	'Freelancer',
	'50130',
	'Chiang Mai',
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	'takezocmu@gmail.com',
	NULL
);
```

```sql
INSERT INTO customers (FirstName, LastName, Email)
VALUES(
	'Phiphat',
	'Chomchit',
	'takezocmu@gmail.com'
);
```









