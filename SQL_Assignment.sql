/* QUES 1. 
  Create a table called employees with the following structure?
: emp_id (integer, should not be NULL and should be a primary key)
: emp_name (text, should not be NULL)
: age (integer, should have a check constraint to ensure the age is at least 18)
: email (text, should be unique for each employee)
: salary (decimal, with a default value of 30,000).
Write the SQL query to create the above table with all constraints. */

create database employee_info;
use employee_info;
create table employees(
emp_id int primary key,
emp_name char(30) not null,
age int check(age >= 18),
email varchar(320) unique,
salary decimal(10,2) default 30000.00);


/* QUES 6 . You created a products table without constraints as follows:

CREATE TABLE products (

    product_id INT,

    product_name VARCHAR(50),

    price DECIMAL(10, 2));  
Now, you realise that?
: The product_id should be a primary keyQ
: The price should have a default value of 50.00 */

create database product_info;
use product_info;
create table products(
product_id INT,
product_name VARCHAR(50),
price DECIMAL(10, 2));

/*adding constraint that The product_id should be a primary key.*/
alter table products add constraint product_id_pk primary key(product_id);

 /*adding constraint that the price should have a default value of 50.00 */
alter table products modify price DECIMAL(10, 2) default 50.00;


/* QUES 7. You have two tables:
Students:

| student_id | student_name | class_id |
|------------|--------------|----------|
|     1      |     Alice    |    101   |
|     2      |     Bob      |    102   |
|     3      |    Charlie   |    101   |

Classes:

| class_id | class_name |
|----------|------------|
|   101    |    Math    |
|   102    |  Science   |
|   103    |  History   |
Write a query to fetch the student_name and class_name for each student using an INNER JOIN.*/

create database student_info;
use student_info;
create table students(
student_id int,
student_name char(40),
class_id char(20));

create table classes(
class_id char(20),
class_name char(20));

insert into students 
values(1, 'Alice', 101),(2,'Bob', 102), (3,'Charlie', 101);

insert into classes 
values (101, 'Math'), (102, 'Science'), (103, 'History');

select * from students;
select * from classes;

/*query to fetch the student_name and class_name for each student using an INNER JOIN.*/
select stu.student_name, cls.class_name 
from students stu
inner join classes cls
on 
stu.class_id = cls.class_id;


/* QUES 8. Consider the following three tables:
Orders:
| order_id | order_date | customer_id |
|----------|------------|-------------|
|    1     | 2024-01-01 |     101     |
|    2     | 2024-01-03 |     102     |
Customers:
| customer_id | customer_name |
|-------------|---------------|
|     101     |     Alice     |
|     102     |     Bob       |
Products_new:
| product_id | product_name | order_id |
|------------|--------------|----------|
|     1      |   Laptop     |     1    |
|     2      |    Phone     |   NULL   |

Write a query that shows all order_id, customer_name, and product_name, ensuring that all products are 
listed even if they are not associated with an order 

Hint: (use INNER JOIN and LEFT JOIN)*/

create database sales_system;
use sales_system;
create table orders (
order_id char (30),
order_date date,
customer_id char(30));

create table customers (
customer_id char(30),
customer_name char(40));

create table products_new (
product_id char(30),
product_name char(40),
order_id char(30));

insert into orders 
values(1,'2024-01-01',101),(2,'2024-01-03',102);

insert into customers 
values (101,'Alice'),(102,'Bob');

insert into products_new
values(1,'Laptop',1),(2,'Phone', NULL);

/*query that shows all order_id, customer_name, and product_name, ensuring that all products are 
listed even if they are not associated with an order */

select o.order_id, c.customer_name, p.product_name 
from products_new p
left join orders o
on 
p.order_id = o.order_id
left join customers c
on 
o.customer_id = c.customer_id;

/* QUES 9.  Given the following tables:
Sales:
sale_id	product_id	amount
1	101	500
2	102	300
3	101	700

Products_2:
product_id	product_name
101	Laptop
102	Phone
Write a query to find the total sales amount for each product using an INNER JOIN and the SUM() function */

create database sales_info;
use sales_info;
create table sales(
sales_id char(20), 
product_id char(20),
amount decimal (10,2));

create table products_2 (
product_id char(30),
product_name char(40));

insert into sales 
values (1,101,500),(2,102,300),(3,101,700);

insert into products_2
values(101,'Laptop'),(102,'Phone');

select * from sales;
select* from products_2;

/*  query to find the total sales amount for each product using an INNER JOIN and the SUM() function  */

select pro.product_id, sum(sal.amount) as Total_sales from sales sal
inner join products_2 pro
on
sal.product_id = pro.product_id
group by product_id;

/* QUES 10.  You are given three tables:
Orders Table:
order_id	order_date	customer_id
1	2024-01-02	1
2	2024-01-05	2

Customers Table:
customer_id	customer_name
1	Alice
2	Bob

Order_Details Table:
order_id	product_id	quantity
1	101	2
1	102	1
2	101	3
Write a query to display the order_id, customer_name, and the quantity of products ordered by each 
customer using an INNER JOIN between all three tables.
Note - The above-mentioned questions don't require any dataset*/

SELECT 
    o.order_id, 
    c.customer_name, 
    od.quantity
FROM 
    Orders o
INNER JOIN 
    Customers c ON o.customer_id = c.customer_id
INNER JOIN 
    Order_Details od ON o.order_id = od.order_id;
     
# SQL COMMANDS--

/* QUES 1 Identify the primary keys and foreign keys in maven movies db. Discuss the differences */

# For primary key 
SELECT TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE CONSTRAINT_NAME = 'PRIMARY'
AND TABLE_SCHEMA = 'mavenmovies';

#For foreign key
SELECT TABLE_NAME, 
       COLUMN_NAME, 
       CONSTRAINT_NAME, 
       REFERENCED_TABLE_NAME, 
       REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE REFERENCED_TABLE_NAME IS NOT NULL
AND TABLE_SCHEMA = 'mavenmovies';

## DIFFERENCES-
/* Aspect	             Primary Key	                                                Foreign Key
Definition	    Uniquely identifies a record in a table.	        Links two tables by referencing the primary key.
Uniqueness	    Must be unique for each record in the table.	    Can have duplicate values if the relationship allows.
Nullability	    Cannot contain NULL values.	                        Can contain NULL values if not all records are linked.
Purpose	        Ensures each record has a unique identifier.	    Maintains referential integrity between tables.
Number 	        A table can have only one primary key.	            A table can have multiple foreign keys. */


/* QUES 2.  List all details of actors */ 
use mavenmovies;
select * from actor;

/* QUES 3. List all customer information from DB.*/
select * from customer;

/* QUES 4. List different countries.*/
select distinct country, country_id from country;

/* QUES 5. Display all active customers.*/
select * from customer 
where active = 1;

/* QUES 6. List of all rental IDs for customer with ID 1.*/
select rental_id, customer_id from rental
where customer_id = 1;

/* QUES 7. Display all the films whose rental duration is greater than 5 .*/
select * from film
where rental_duration > 5;

/* QUES 8. List the total number of films whose replacement cost is greater than $15 and less
 than $20*/
select count(replacement_cost) as total_films
from film
where replacement_cost between 15 and 20;

/* QUES 9. Display the count of unique first names of actors. */
select count(distinct first_name) 
from actor;

/* QUES 10. Display the first 10 records from the customer table . */
select * from customer
limit 10;

/* QUES 11. Display the first 3 records from the customer table whose first name starts with ‘b’. */
select * from customer
where first_name like 'b%'
limit 3;

/* QUES 12. Display the names of the first 5 movies which are rated as ‘G. */
select title, rating 
from film
where rating = 'G'
limit 5;

/* QUES 13. Find all customers whose first name starts with "a". */
select * from customer
where first_name like 'a%';

/* QUES 14. Find all customers whose first name ends with "a". */
select * from customer
where first_name like '%a';

/* QUES 15. Display the list of first 4 cities which start and end with ‘a’. */
select * from city
where city like 'a%a'
limit 4;

/* QUES 16. Find all customers whose first name have "NI" in any position.*/
select * from customer
where first_name like '%NI%';

/* QUES 17.  Find all customers whose first name have "r" in the second position.*/
select * from customer
where first_name like '_r%';

/* QUES 18. Find all customers whose first name starts with "a" and are at least 5 characters 
in length.*/
select * from customer
where first_name like 'a____%';

/* QUES 19. Find all customers whose first name starts with "a" and ends with "o".*/
select * from customer
where first_name like 'a%o';

/* QUES 20.  Get the films with pg and pg-13 rating using IN operator. */
select * from film
where rating in ('pg','pg-13');

/* QUES 21.  Get the films with length between 50 to 100 using between operator. */
select * from film
where length between 50 and 100;

/* QUES 22. Get the top 50 actors using limit operator.  */
select * from actor
limit 50;

/* QUES 23. Get the distinct film ids from inventory table. */
select distinct film_id 
from inventory;


##FUNCTIONS--


/* QUES 1. Retrieve the total number of rentals made in the Sakila database.
Hint: Use the COUNT() function.*/ 
use sakila;
select count(*) as total_rentals 
from rental;

/* QUES 2. Find the average rental duration (in days) of movies rented from the Sakila database.
Hint: Utilize the AVG() function.*/
select avg(datediff(return_date,rental_date)) as holding_days
from rental;

/* QUES 3. Display the first name and last name of customers in uppercase.
Hint: Use the UPPER () function.*/
select upper(first_name) as up_first_name, upper(last_name) as up_last_name
from customer;

/* QUES 4. Extract the month from the rental date and display it alongside the rental ID.
Hint: Employ the MONTH() function.*/
select month(rental_date) as rental_month, rental_id
from rental;

/* QUES 5. Retrieve the count of rentals for each customer (display customer ID and the count of rentals).
Hint: Use COUNT () in conjunction with GROUP BY. */
select  customer_id, count(*)as rental_count
from rental
group by customer_id;

/* QUES 6. Find the total revenue generated by each store.
Hint: Combine SUM() and GROUP BY.*/

SELECT s.store_id, 
       SUM(p.amount) AS total_revenue
FROM payment p
JOIN staff st ON p.staff_id = st.staff_id
JOIN store s ON st.store_id = s.store_id
GROUP BY s.store_id;

/* QUES 7. Determine the total number of rentals for each category of movies.
Hint: JOIN film_category, film, and rental tables, then use cOUNT () and GROUP BY. */ 
SELECT c.name AS category_name, 
       COUNT(r.rental_id) AS total_rentals
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_rentals DESC;

/* QUES 8. Find the average rental rate of movies in each language.
Hint: JOIN film and language tables, then use AVG () and GROUP BY.*/
select l.name, avg(f.rental_rate) as avg_rental_rate
from film f
join language l
on 
f.language_id = l.language_id
group by l.name;


## JOINS--


/* QUES 9. Display the title of the movie, customer s first name, and last name who rented it.
Hint: Use JOIN between the film, inventory, rental, and customer tables. */

use sakila;

SELECT 
    f.title AS Movie_Title,
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName
FROM 
    film f
JOIN 
    inventory i ON f.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
JOIN 
    customer c ON r.customer_id = c.customer_id;
    
/* QUES 10. Retrieve the names of all actors who have appeared in the film "Gone with the Wind."
Hint: Use JOIN between the film actor, film, and actor tables */

SELECT 
    a.first_name AS Actor_FirstName,
    a.last_name AS Actor_LastName
FROM 
    actor a
JOIN 
    film_actor fa ON a.actor_id = fa.actor_id
JOIN 
    film f ON fa.film_id = f.film_id
WHERE 
    f.title = 'Gone with the Wind';
    
/* QUES 11. Retrieve the customer names along with the total amount they've spent on rentals.
Hint: JOIN customer, payment, and rental tables, then use SUM() and GROUP BY. */
SELECT 
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName,
    SUM(p.amount) AS Total_Amount_Spent
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    payment p ON r.rental_id = p.rental_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    Total_Amount_Spent DESC;

/* QUES 12. List the titles of movies rented by each customer in a particular city (e.g., 'London').
Hint: JOIN customer, address, city, rental, inventory, and film tables, then use GROUP BY. */
SELECT 
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName,
    f.title AS Movie_Title,
    ci.city AS City
FROM 
    customer c
JOIN 
    address a ON c.address_id = a.address_id
JOIN 
    city ci ON a.city_id = ci.city_id
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
WHERE 
    ci.city = 'London'
ORDER BY 
    c.last_name, c.first_name, f.title;
    
    
    ##Advanced Joins and GROUP BY:
    
/* QUES 13. Display the top 5 rented movies along with the number of times they've been rented.
Hint: JOIN film, inventory, and rental tables, then use COUNT () and GROUP BY, and limit the results */

SELECT 
    f.title AS Movie_Title,
    COUNT(r.rental_id) AS Times_Rented
FROM 
    film f
JOIN 
    inventory i ON f.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
GROUP BY 
    f.title
ORDER BY 
    Times_Rented DESC
LIMIT 5;

/* QUES 14. Determine the customers who have rented movies from both stores (store ID 1 and store ID 2).
Hint: Use JOINS with rental, inventory, and customer tables and consider COUNT() and GROUP BY */

SELECT 
    c.customer_id,
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
WHERE 
    i.store_id IN (1, 2)
GROUP BY 
    c.customer_id, c.first_name, c.last_name
HAVING 
    COUNT(DISTINCT i.store_id) = 2;
    
###  Windows Function:

/* 1. Rank the customers based on the total amount they've spent on rentals. */
SELECT 
    c.customer_id,
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName,
    SUM(p.amount) AS Total_Amount_Spent,
    RANK() OVER (ORDER BY SUM(p.amount) DESC) AS `Rank`
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    payment p ON r.rental_id = p.rental_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    `Rank`;

/* 2.  Calculate the cumulative revenue generated by each film over time. */
SELECT 
    f.title AS Film_Title,
    p.amount AS Payment_Amount,
    SUM(p.amount) OVER (PARTITION BY f.film_id ORDER BY r.rental_date) AS Cumulative_Revenue
FROM 
    film f
JOIN 
    inventory i ON f.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
JOIN 
    payment p ON r.rental_id = p.rental_id
ORDER BY 
    f.title, r.rental_date;

/* 3. Determine the average rental duration for each film, considering films with similar lengths */

SELECT 
    f.title AS Film_Title,
    f.length AS Film_Length,
    AVG(TIMESTAMPDIFF(MINUTE, r.rental_date, r.return_date)) AS Average_Rental_Duration
FROM 
    film f
JOIN 
    inventory i ON f.film_id = i.film_id
JOIN 
    rental r ON i.inventory_id = r.inventory_id
GROUP BY 
    f.title, f.length
ORDER BY 
    f.length;

/* 4.  Identify the top 3 films in each category based on their rental counts.*/
SELECT 
    Category_Name,
    Film_Title,
    Rental_Count
FROM (
    SELECT 
        c.name AS Category_Name,
        f.title AS Film_Title,
        COUNT(r.rental_id) AS Rental_Count,
        ROW_NUMBER() OVER (PARTITION BY c.name ORDER BY COUNT(r.rental_id) DESC) AS`Rank`
    FROM 
        film f
    JOIN 
        film_category fc ON f.film_id = fc.film_id
    JOIN 
        category c ON fc.category_id = c.category_id
    JOIN 
        inventory i ON f.film_id = i.film_id
    JOIN 
        rental r ON i.inventory_id = r.inventory_id
    GROUP BY 
        c.name, f.title
) AS ranked_films
WHERE 
    `Rank` <= 3
ORDER BY 
    Category_Name, `Rank`;

/* 5.   Calculate the difference in rental counts between each customer's total rentals and the average rentals
across all customers.*/

SELECT 
    c.customer_id,
    c.first_name AS Customer_FirstName,
    c.last_name AS Customer_LastName,
    COUNT(r.rental_id) AS Customer_Rental_Count,
    (COUNT(r.rental_id) - avg_rental_count.Avg_Rental_Count) AS Rental_Count_Difference
FROM 
    customer c
JOIN 
    rental r ON c.customer_id = r.customer_id
JOIN 
    (SELECT AVG(rental_count) AS Avg_Rental_Count
     FROM (SELECT customer_id, COUNT(rental_id) AS rental_count
           FROM rental
           GROUP BY customer_id) AS customer_rentals) AS avg_rental_count
GROUP BY 
    c.customer_id, c.first_name, c.last_name, avg_rental_count.Avg_Rental_Count
ORDER BY 
    Rental_Count_Difference DESC;

/* 6. Find the monthly revenue trend for the entire rental store over time.*/
SELECT 
    YEAR(p.payment_date) AS Year,
    MONTH(p.payment_date) AS Month,
    SUM(p.amount) AS Monthly_Revenue
FROM 
    payment p
GROUP BY 
    YEAR(p.payment_date), MONTH(p.payment_date)
ORDER BY 
    Year, Month;

/* 7. Identify the customers whose total spending on rentals falls within the top 20% of all customers.*/

WITH CustomerSpending AS (
    SELECT 
        c.customer_id,
        c.first_name AS Customer_FirstName,
        c.last_name AS Customer_LastName,
        SUM(p.amount) AS Total_Spent
    FROM 
        customer c
    JOIN 
        rental r ON c.customer_id = r.customer_id
    JOIN 
        payment p ON r.rental_id = p.rental_id
    GROUP BY 
        c.customer_id, c.first_name, c.last_name
),
PercentileThreshold AS (
    SELECT 
        COUNT(*) AS TotalCustomers,
        MAX(Total_Spent) AS MaxSpending
    FROM CustomerSpending
),
RankedCustomers AS (
    SELECT 
        cs.customer_id,
        cs.Customer_FirstName,
        cs.Customer_LastName,
        cs.Total_Spent,
        RANK() OVER (ORDER BY cs.Total_Spent DESC) AS CustomerRank,
        pct.TotalCustomers
    FROM 
        CustomerSpending cs
    CROSS JOIN 
        PercentileThreshold pct
)
SELECT 
    customer_id,
    Customer_FirstName,
    Customer_LastName,
    Total_Spent
FROM 
    RankedCustomers
WHERE 
    CustomerRank <= FLOOR(TotalCustomers * 0.2)
ORDER BY 
    Total_Spent DESC;

/* 8. Identify the customers whose total spending on rentals falls within the top 20% of all customers.*/
SELECT 
    cat.name AS Category,
    COUNT(r.rental_id) AS Rental_Count,
    SUM(COUNT(r.rental_id)) OVER (ORDER BY COUNT(r.rental_id) DESC) AS Running_Total
FROM 
    rental r
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
JOIN 
    film_category fc ON f.film_id = fc.film_id
JOIN 
    category cat ON fc.category_id = cat.category_id
GROUP BY 
    cat.name
ORDER BY 
    Rental_Count DESC;

/* 9.  Find the films that have been rented less than the average rental count for their respective categories*/

SELECT 
    f.title AS Film_Title,
    cat.name AS Category,
    COUNT(r.rental_id) AS Rental_Count,
    avg_category_avg.Avg_Rental_Count
FROM 
    rental r
JOIN 
    inventory i ON r.inventory_id = i.inventory_id
JOIN 
    film f ON i.film_id = f.film_id
JOIN 
    film_category fc ON f.film_id = fc.film_id
JOIN 
    category cat ON fc.category_id = cat.category_id
JOIN (
    -- Subquery to calculate the average rental count per category
    SELECT 
        cat.category_id,
        AVG(rental_count) AS Avg_Rental_Count
    FROM 
        (
            SELECT 
                cat.category_id,
                COUNT(r.rental_id) AS rental_count
            FROM 
                rental r
            JOIN 
                inventory i ON r.inventory_id = i.inventory_id
            JOIN 
                film f ON i.film_id = f.film_id
            JOIN 
                film_category fc ON f.film_id = fc.film_id
            JOIN 
                category cat ON fc.category_id = cat.category_id
            GROUP BY 
                cat.category_id, f.film_id
        ) AS category_rentals
    GROUP BY 
        cat.category_id
) AS avg_category_avg ON avg_category_avg.category_id = cat.category_id
GROUP BY 
    f.title, cat.name, avg_category_avg.Avg_Rental_Count
HAVING 
    Rental_Count < Avg_Rental_Count
ORDER BY 
    Rental_Count;

/* 10. Identify the top 5 months with the highest revenue and display the revenue generated in each month Identify the top 5 months with the
 highest revenue and display the revenue generated in each month*/
SELECT 
    DATE_FORMAT(p.payment_date, '%Y-%m') AS Month,
    SUM(p.amount) AS Total_Revenue
FROM 
    payment p
GROUP BY 
    Month
ORDER BY 
    Total_Revenue DESC
LIMIT 5;


### Normalisation & CTE:

/*5. CTE Basics:
 a. Write a query using a CTE to retrieve the distinct list of actor names and the number of films they 
 have acted in from the actor and film_actor tables  */

WITH ActorFilmCount AS (
    SELECT
        a.actor_id,
        CONCAT(a.first_name, ' ', a.last_name) AS actor_name,
        COUNT(fa.film_id) AS film_count
    FROM
        actor a
    JOIN
        film_actor fa ON a.actor_id = fa.actor_id
    GROUP BY
        a.actor_id
)
SELECT
    actor_name,
    film_count
FROM
    ActorFilmCount
ORDER BY
    film_count DESC;

/*6. CTE with Joins:
 a. Create a CTE that combines information from the film and language tables to display the film title, 
 language name, and rental rate.*/

WITH FilmLanguageInfo AS (
    SELECT
        f.title AS film_title,
        l.name AS language_name,
        f.rental_rate
    FROM
        film f
    JOIN
        language l ON f.language_id = l.language_id
)
SELECT
    film_title,
    language_name,
    rental_rate
FROM
    FilmLanguageInfo
ORDER BY
    film_title;

/* 7. CTE for Aggregation:
 a. Write a query using a CTE to find the total revenue generated by each customer (sum of payments) 
 from the customer and payment tables. */
WITH CustomerRevenue AS (
    SELECT
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        SUM(p.amount) AS total_revenue
    FROM
        customer c
    JOIN
        payment p ON c.customer_id = p.customer_id
    GROUP BY
        c.customer_id, c.first_name, c.last_name
)
SELECT
    customer_name,
    total_revenue
FROM
    CustomerRevenue
ORDER BY
    total_revenue DESC;

/*8. CTE with Window Functions:
 a. Utilize a CTE with a window function to rank films based on their rental duration from the film table   */
WITH FilmRanked AS (
    SELECT
        f.title AS film_title,
        f.rental_duration,
        RANK() OVER (ORDER BY f.rental_duration DESC) AS rental_rank
    FROM
        film f
)
SELECT
    film_title,
    rental_duration,
    rental_rank
FROM
    FilmRanked
ORDER BY
    rental_rank;

/*9. CTE and Filtering:
 a. Create a CTE to list customers who have made more than two rentals, and then join this CTE with the 
 customer table to retrieve additional customer details. */

WITH CustomersWithMoreThanTwoRentals AS (
    SELECT
        r.customer_id,
        COUNT(r.rental_id) AS rental_count
    FROM
        rental r
    GROUP BY
        r.customer_id
    HAVING
        COUNT(r.rental_id) > 2
)
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.email,
    c.address_id,
    c.active
FROM
    customer c
JOIN
    CustomersWithMoreThanTwoRentals cte
    ON c.customer_id = cte.customer_id
ORDER BY
    c.first_name, c.last_name;
    
/*10. CTE for Date Calculations:
 a. Write a query using a CTE to find the total number of rentals made each month, considering the 
 rental_date from the rental table. */

WITH MonthlyRentalCounts AS (
    SELECT
        DATE_FORMAT(r.rental_date, '%Y-%m') AS rental_month,
        COUNT(r.rental_id) AS total_rentals
    FROM
        rental r
    GROUP BY
        DATE_FORMAT(r.rental_date, '%Y-%m')
)
SELECT
    rental_month,
    total_rentals
FROM
    MonthlyRentalCounts
ORDER BY
    rental_month;

/* 11. EE' CTE and Self-Join:
 a. Create a CTE to generate a report showing pairs of actors who have appeared in the same film 
 together, using the film_actor table*/
 WITH ActorPairs AS (
    SELECT
        fa1.actor_id AS actor_1_id,
        fa2.actor_id AS actor_2_id,
        f.title AS film_title
    FROM
        film_actor fa1
    JOIN
        film_actor fa2 ON fa1.film_id = fa2.film_id
    JOIN
        film f ON fa1.film_id = f.film_id
    WHERE
        fa1.actor_id < fa2.actor_id
)
SELECT
    a1.actor_id AS actor_1_id,
    CONCAT(a1.first_name, ' ', a1.last_name) AS actor_1_name,
    a2.actor_id AS actor_2_id,
    CONCAT(a2.first_name, ' ', a2.last_name) AS actor_2_name,
    ap.film_title
FROM
    ActorPairs ap
JOIN
    actor a1 ON ap.actor_1_id = a1.actor_id
JOIN
    actor a2 ON ap.actor_2_id = a2.actor_id
ORDER BY
    ap.film_title, actor_1_name, actor_2_name;

/* 12. 12. CTE for Recursive Search:
 a. Implement a recursive CTE to find all employees in the staff table who report to a specific manager, 
 considering the reports_to column*/

WITH RECURSIVE EmployeeHierarchy AS (
    -- Anchor member: Start with the manager
    SELECT
        s.staff_id,
        s.first_name,
        s.last_name,
        s.reports_to
    FROM
        staff s
    WHERE
        s.staff_id = 1 -- Replace 1 with the actual manager's ID
    
    UNION ALL
    
    -- Recursive member: Find employees reporting to the current staff
    SELECT
        s.staff_id,
        s.first_name,
        s.last_name,
        s.reports_to
    FROM
        staff s
    INNER JOIN
        EmployeeHierarchy eh ON s.reports_to = eh.staff_id
)
SELECT
    staff_id,
    first_name,
    last_name,
    reports_to
FROM
    EmployeeHierarchy
ORDER BY
    staff_id;





