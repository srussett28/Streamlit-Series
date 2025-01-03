import streamlit as st
st.title("SQL Command Guide")
st.image(r"C:\Users\Sloan\Documents\Github\SQL_Stuff\SQL_Database.png", caption="SQL CMD", use_column_width=True)
st.write("This guide covers essential SQL Commands with examples and business use cases")


st.header("Why SQL is Relevant for Data Professionals")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\venn-diagram-wizeline.jpg", caption="Data Professions Venn Diagram", use_column_width=True)


st.subheader("Data Analysts")
st.write(
    "Data analysts use SQL to extract, manipulate, and analyze data from databases. "
    "SQL helps them to query large datasets, generate reports, and perform data aggregations "
    "to support business decisions. Analysts rely on SQL for routine tasks like data extraction, filtering, and summarizing."
)


st.subheader("Data Scientists")
st.write(
    "Data scientists need SQL to work with data directly in databases, especially when handling large datasets. "
    "They use SQL to extract clean, relevant data for analysis and modeling. SQL also helps in data wrangling and "
    "preparing datasets for machine learning models."
)


st.subheader("Analytics Engineers")
st.write(
    "Analytics engineers leverage SQL to design and maintain robust data pipelines that ensure data availability for analysis. "
    "They also write complex queries to support analytics tools and optimize data storage for faster query performance."
)


st.subheader("Data Engineers")
st.write(
    "Data engineers use SQL to build and maintain databases, data warehouses, and ETL pipelines. "
    "SQL plays a key role in defining and managing the structure of data in these systems, ensuring it is clean, organized, "
    "and easy to query for other roles like data analysts and data scientists."
)


st.header("SQL Command Categories")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\SQLCMD.png", caption="SQL CMD Categories", use_column_width=True)

st.subheader("1. Data Definition Language (DDL)")
st.write(
    "DDL commands are used to define and manage database structures like tables, schemas, and indexes. They include commands"
   
)


st.subheader("2. Data Manipulation Language (DML)")
st.write(
    "DML commands are used to manipulate data stored in the database. These commands allow you to query and update data."
)


st.subheader("3. Data Control Language (DCL)")
st.write(
    "DCL commands are used to manage access permissions on database objects."
)


st.subheader("4. Transaction Control Language (TCL)")
st.write(
    "TCL commands are used to manage transactions in a database. These commands help ensure data integrity and consistency. " 
)


st.header("Basic SQL Commands")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\basicCMD.png", caption="Basic SQL Commands", use_column_width=True)
st.subheader("SELECT")
st.write("""
-** What It Does**: Retrieves Data from one or more tables in a database.
-** Selecting Specific Columns**: Select * retrieves all columns from the table(s), while selecting for specific columns follows this path
SELECT column 1, column 2, column 3 etc. 
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
   - **Data Analyst**: Extracts data for analysis and reporting.
   - **Data Scientist**: Retrieves data for cleaning and modeling.
   - **Analytics Engineer**: Queries data for pipeline processing.
   - **Data Engineer**: Retrieves data for data pipeline and storage.
-** Business Case**: Retrieve customer information, analyzing sales data, and even generating inventiory reports.
-** Keywords**: "Pull", "Show', "Retrieve", "List", "Extract". 
""" )
st.code("SELECT * FROM orders WHERE status = 'Shipped';", language="sql")


st.subheader("INSERT INTO")
st.write("""
- **What It Does**: Adds new data into a table in the database. This can include inserting a single row or multiple rows of data.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
   - **Data Engineer**: Inserts data into databases as part of ETL processes.
   - **Analytics Engineer**: May use for inserting data into staging or temporary tables.
- **Business Case**: Adding new customer records, logging a new transaction, or storing survey responses.
- **Keywords**: "Add", "Insert", "Include", "Create", "Populate".
""")
st.code("INSERT INTO customers (name, email, age) VALUES ('John Doe', 'john@example.com', 28);", language="sql")


st.subheader("UPDATE")
st.write("""
- **What It Does**: Modifies existing data in a table based on specified conditions. Allows for updating one or more rows.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
   - **Data Analyst**: Updates data for reporting or analysis.
   - **Data Scientist**: Adjusts data for analysis or model training.
   - **Analytics Engineer**: Modifies data in pipeline workflows.
   - **Data Engineer**: Updates records for data consistency and accuracy.
- **Business Case**: Updating customer contact information, adjusting product prices, or marking orders as fulfilled.
- **Keywords**: "Update", "Modify", "Change", "Edit", "Adjust".
""")
st.code("UPDATE products SET price = 19.99 WHERE product_id = 101;", language="sql")


st.subheader("DELETE")
st.write("""
- **What It Does**: Removes rows from a table based on specified conditions. Be cautious as it can delete one or all rows if no condition is applied.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
   - **Data Analyst**: Removes outdated or irrelevant data for analysis.
   - **Data Scientist**: Deletes invalid or irrelevant data for analysis.
   - **Analytics Engineer**: Deletes records in pipeline operations.
   - **Data Engineer**: Deletes records for data maintenance and cleaning.
- **Business Case**: Removing obsolete customer records, deleting canceled orders, or clearing temporary data.
- **Keywords**: "Delete", "Remove", "Purge", "Clear", "Drop".
""")
st.code("DELETE FROM orders WHERE order_date < '2023-01-01';", language="sql")


st.header("Filtering Data Commands")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\filtering.jpg", caption="Filtering Commands", use_column_width=True)
st.subheader("WHERE")
st.write("""
- **What It Does**: Filters records based on specific conditions. Used with `SELECT`, `UPDATE`, and `DELETE` to target rows.
- **Category**: DML (Data Manipulation Language)
- **Most Likely to Use**:
  - **Data Analyst**: Commonly used to filter data for specific analysis or reporting (e.g., pulling sales data for a specific region).
  - **Data Science**: Applied to filter data for model training or exploration.
  - **Analytics Engineer**: Used to retrieve specific data for analytics pipelines.
- **Business Case**: Fetching orders with a specific status, retrieving users from a certain city, or removing outdated data.
- **Keywords**: "Filter", "Condition", "Specify", "Limit results".
""")
st.code("SELECT * FROM orders WHERE status = 'Shipped';", language="sql")


st.subheader("AND/OR/NOT")
st.write("""
- **What It Does**: Combines multiple conditions in a `WHERE` clause:
  - `AND`: All conditions must be true.
  - `OR`: At least one condition must be true.
  - `NOT`: Negates a condition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Used to build more complex filters to analyze data (e.g., customers within a specific region and age group).
  - **Data Science**: Applied in feature selection for models to filter datasets.
  - **Analytics Engineer**: Used for complex queries to refine the data for analysis.
- **Business Case**: Fetching records with complex conditions, such as customers from a specific region and within a certain age range.
- **Keywords**: "Combine", "All", "Any", "Exclude".
""")
st.code("SELECT * FROM customers WHERE city = 'New York' AND age > 30;", language="sql")
st.code("SELECT * FROM orders WHERE status = 'Pending' OR status = 'Processing';", language="sql")
st.code("SELECT * FROM products WHERE NOT category = 'Electronics';", language="sql")


st.subheader("IN")
st.write("""
- **What It Does**: Matches a value against a list of specified values.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Frequently used to filter data based on a predefined list of values.
  - **Data Science**: Applied to categorize or segment data for further analysis.
  - **Analytics Engineer**: Used in data extraction and transformation processes to filter based on a list of valid values.
- **Syntax Example**: Use IN to match a column value against a list of specific values.
- **Business Case**: Fetching records with specific criteria, such as orders placed by a list of key customers.
- **Keywords**: "List", "Subset", "Match specific values".
""")
st.code("SELECT * FROM orders WHERE status IN ('Shipped', 'Processing', 'Pending');", language="sql")


st.subheader("BETWEEN")
st.write("""
- **What It Does**: Filters rows where a column value lies within a specified range (inclusive).
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Often used to filter time-series data for reporting or analysis.
  - **Data Science**: Applied to select data within a specific range for modeling or testing.
  - **Analytics Engineer**: Frequently used in queries for ETL processes to narrow down large datasets.     
- **Business Case**: Fetching data for a specific time period, such as sales from the last month.
- **Keywords**: "Range", "Between", "Inclusive", "Within limits".
""")
st.code("SELECT * FROM sales WHERE sale_date BETWEEN '2023-01-01' AND '2023-12-31';", language="sql")


st.subheader("LIKE")
st.write("""
- **What It Does**: Matches patterns in text using wildcard characters (`%` and `_`).
  - `%`: Matches zero or more characters.
  - `_`: Matches a single character.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Applied to filter or search for records that match certain text patterns (e.g., finding all customers whose names begin with 'J').
  - **Data Scientist**: Used for preprocessing and text feature extraction, especially in Natural Language Processing (NLP).
  - **Analytics Engineer**: Utilized to clean or segment data based on text pattern matching.
- **Business Case**: Searching for records with partially matching text, such as finding all customers whose names start with 'J'.
- **Keywords**: "Pattern", "Search", "Wildcard".
""")
st.code("SELECT * FROM customers WHERE name LIKE 'J%';", language="sql")


st.subheader("IS NULL/IS NOT NULL")
st.write("""
- **What It Does**: Checks whether a column has null (missing) values or not.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Used for identifying incomplete or missing data during analysis (e.g., finding records with no shipping dates).
  - **Data Scientist**: Essential for handling missing data, either by imputation or removal, before training models.
  - **Data Engineer**: Applied to check for and handle null values during data processing or transformation.
- **Business Case**: Identifying incomplete records, such as orders missing shipping details.
- **Keywords**: "Missing", "Empty", "Null", "No value".
""")
st.code("SELECT * FROM orders WHERE shipping_date IS NULL;", language="sql")
st.code("SELECT * FROM customers WHERE email IS NOT NULL;", language="sql")


st.subheader("EXISTS")
st.write("""
- **What It Does**: Tests for the existence of any record in a subquery. Returns `TRUE` if the subquery yields results.
- **Category**: DML (Data Manipulation Language) / Subqueries
- **Roles Most Likely to Use**:
  - **Data Analyst**: Used to check for relationships between tables and ensure dependencies exist before analysis.
  - **Data Engineering**: Often used in ETL processes to ensure dependent data exists before performing joins or transformations.
  - **Analytics Engineer**: Applied in more complex queries when validating relationships across datasets.       
- **Business Case**: Checking if a customer has placed any orders, or verifying if a product is in stock.
- **Keywords**: "Check existence", "Subquery", "Dependent data".
""")
st.code("SELECT * FROM customers WHERE EXISTS (SELECT * FROM orders WHERE customers.id = orders.customer_id);", language="sql")


st.header("Sorting & Limiting Data")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\sorting.jpg", caption="Basic SQL Commands", use_column_width=True)
st.subheader("ORDER BY")
st.write("""
- **What It Does**: Sorts the result set by one or more columns in ascending (`ASC`) or descending (`DESC`) order.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To rank data for reports like top-performing products or employees by metrics.
  - **Data Scientists**: To sort data for preprocessing before analysis or model training.
- **Business Case**: Generating ranked lists, such as top-selling products or customers by sales amount.
- **Keywords**: "Sort", "Arrange", "Rank", "Order".
""")
st.code("SELECT * FROM products ORDER BY price ASC;", language="sql")
st.code("SELECT * FROM employees ORDER BY hire_date DESC;", language="sql")


st.subheader("LIMIT")
st.write("""
- **What It Does**: Restricts the number of rows returned in the result set.
 **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To limit rows when creating summaries or sample datasets.
  - **Data Scientists**: To fetch small subsets of data for quick analysis or prototyping.
  - **Analytics Engineers**: Occasionally, to test ETL pipelines with smaller datasets.
- **Business Case**: Fetching the top-performing products, getting sample data, or displaying the first few records in a report.
- **Keywords**: "Top", "First", "Subset", "Restrict rows".
""")
st.code("SELECT * FROM orders LIMIT 10;", language="sql")
st.code("SELECT * FROM customers ORDER BY total_spent DESC LIMIT 5;", language="sql")


st.subheader("DISTINCT")
st.write("""
- **What It Does**: Returns only unique values, removing duplicates from the result set.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To identify unique categories, customer locations, or order statuses.
  - **Analytics Engineers**: To retrieve distinct values when designing data models.
  - **Data Engineers**: To validate and de-duplicate data during ETL processes.
- **Business Case**: Identifying unique customer locations, product categories, or order statuses.
- **Keywords**: "Unique", "No duplicates", "Distinct", "Different values".
""")
st.code("SELECT DISTINCT country FROM customers;", language="sql")
st.code("SELECT DISTINCT status FROM orders;", language="sql")

st.header("Aggregating Data")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\aggrgate.png", caption="Basic SQL Commands", use_column_width=True)
st.subheader("COUNT()")
st.write("""
- **What It Does**: Returns the number of rows matching a specified condition.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To count the number of records for reporting purposes.
  - **Data Scientists**: To check the number of data points or samples in a dataset.
  - **Analytics Engineers**: Occasionally, when performing data quality checks.
- **Business Case**: Counting the total number of orders, customers, or products in inventory.
- **Keywords**: "Total", "Number of", "Count", "How many".
""")
st.code("SELECT COUNT(*) FROM orders WHERE status = 'Shipped';", language="sql")
st.code("SELECT COUNT(customer_id) FROM customers;", language="sql")


st.subheader("SUM()")
st.write("""
- **What It Does**: Returns the total sum of a numeric column.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To calculate total sales, revenue, or any other sums for reporting.
  - **Data Scientists**: To calculate the sum of values in preprocessing for analysis or feature engineering.
  - **Analytics Engineers**: Occasionally, when creating aggregate metrics for dashboards.
- **Syntax Example**: Use `SUM()` with the column name to sum values.
- **Syntax Example**: Use `AVG()` with the column name to calculate the average value.
- **Business Case**: Calculating total sales revenue, summing up inventory quantities, or computing total employee salaries.
- **Keywords**: "Total", "Add", "Sum", "Aggregate".
""")
st.code("SELECT SUM(amount) FROM orders WHERE status = 'Completed';", language="sql")
st.code("SELECT SUM(quantity) FROM inventory;", language="sql")


st.subheader("AVG()")
st.write("""
- **What It Does**: Calculates the average value of a numeric column.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To calculate average values, such as average sales or average customer spending.
  - **Data Scientists**: To understand data distributions or as a feature in machine learning models.
  - **Analytics Engineers**: Occasionally, when working on aggregate data for reporting.
- **Business Case**: Finding the average sales price, average customer spend, or average delivery time.
- **Keywords**: "Average", "Mean", "Typical", "Compute average".
""")
st.code("SELECT AVG(price) FROM products;", language="sql")
st.code("SELECT AVG(salary) FROM employees WHERE department = 'Engineering';", language="sql")


st.subheader("MIN()")
st.write("""
- **What It Does**: Returns the smallest value in a specified column.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To find the minimum value in datasets, like the lowest price or earliest date.
  - **Data Scientists**: To identify minimum values in data preprocessing or to understand the range of features.
  - **Analytics Engineers**: Occasionally, for data validation in aggregation or summarization.
- **Syntax Example**: Use `MIN()` with the column name to find the minimum value.
- **Business Case**: Identifying the lowest sales price, the earliest hire date, or the minimum stock quantity.
- **Keywords**: "Lowest", "Minimum", "Earliest", "Smallest".
""")
st.code("SELECT MIN(price) FROM products;", language="sql")
st.code("SELECT MIN(hire_date) FROM employees;", language="sql")


st.subheader("MAX()")
st.write("""
- **What It Does**: Returns the largest value in a specified column.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To find the maximum value in a dataset, such as highest revenue or maximum sale amount.
  - **Data Scientists**: To identify the maximum values during data preprocessing or analysis.
  - **Analytics Engineers**: Occasionally, for data summarization and validation.
- **Business Case**: Identifying the highest sales price, the latest delivery date, or the maximum customer order total.
- **Keywords**: "Highest", "Maximum", "Latest", "Largest".
""")
st.code("SELECT MAX(price) FROM products;", language="sql")
st.code("SELECT MAX(delivery_date) FROM orders;", language="sql")


st.subheader("GROUP BY")
st.write("""
- **What It Does**: Groups rows that have the same values in specified columns, often used with aggregate functions.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To group data and perform aggregation on categorical variables, like total sales by region.
  - **Data Scientists**: To aggregate data for feature engineering or to understand patterns in the data.
  - **Analytics Engineers**: Frequently used when creating aggregate metrics or building data models.
- **Business Case**: Aggregating sales by region, summarizing inventory by category, or counting customers by membership tier.
- **Keywords**: "Group", "Aggregate", "Summarize", "By category".
""")
st.code("SELECT region, SUM(sales) FROM orders GROUP BY region;", language="sql")
st.code("SELECT category, COUNT(*) FROM products GROUP BY category;", language="sql")


st.subheader("HAVING")
st.write("""
- **What It Does**: Filters grouped data based on a specified condition, often used with aggregate functions.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To filter aggregated results, such as finding only regions with total sales greater than a threshold.
  - **Data Scientists**: Less frequently used, but occasionally for filtering grouped data in exploratory analysis.
  - **Analytics Engineers**: Used for filtering results in aggregate queries, often in dashboarding or reporting pipelines.
- **Business Case**: Filtering for regions with high sales totals, categories with more than a certain number of products, or departments with above-average salaries.
- **Keywords**: "Filter", "Condition", "After aggregation", "Grouped results".
""")
st.code("SELECT region, SUM(sales) FROM orders GROUP BY region HAVING SUM(sales) > 10000;", language="sql")
st.code("SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) > 50;", language="sql")

st.header("Joins")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\joins.png", caption="Basic Joins", use_column_width=True)
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\SQL-JOINS-Example-0.png", caption="Join Logic", use_column_width=True)


st.subheader("INNER JOIN")
st.write("""
- **What It Does**: Returns rows when there is a match in both joined tables.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To combine and compare data from two tables based on related columns for reporting and analysis.
  - **Data Scientists**: For merging datasets to create features or enhance data for analysis.
  - **Analytics Engineers**: Frequently used when building data models or pipelines to join tables with matching keys.
- **Business Case**: Combining orders and customers to find information about customers who made purchases.
- **Keywords**: "Match", "Both tables", "Common", "Intersection".
""")
st.code("""
SELECT customers.customer_id, customers.name, orders.order_id
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
""", language="sql")


st.subheader("LEFT JOIN")
st.write("""
- **What It Does**: Returns all rows from the left table and matched rows from the right table. Unmatched rows in the right table result in `NULL`.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To keep all records from the left table (e.g., all products) and show related data (e.g., sales data) from the right table.
  - **Data Scientists**: To join datasets while preserving all records from a primary dataset, even if no match exists in the secondary dataset.
  - **Analytics Engineers**: Commonly used for building data pipelines where it’s essential to retain all entries from the primary table.
- **Business Case**: Finding all customers and their orders, even if some customers have not placed any orders.
- **Keywords**: "All from left", "Unmatched", "Include nulls".
""")
st.code("""
SELECT customers.customer_id, customers.name, orders.order_id
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
""", language="sql")


st.subheader("RIGHT JOIN")
st.write("""
- **What It Does**: Returns all rows from the right table and matched rows from the left table. Unmatched rows in the left table result in `NULL`.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To ensure all records from the right table are included, useful when the right table has critical data that must be preserved.
  - **Data Scientists**: To preserve all records from a secondary dataset, while still relating data from a primary dataset.
  - **Analytics Engineers**: Commonly used for aggregating data where the secondary dataset is the most important source.
- **Business Case**: Listing all orders and the customers who placed them, even if some orders don’t have customer data.
- **Keywords**: "All from right", "Unmatched", "Include nulls".
""")
st.code("""
SELECT customers.customer_id, customers.name, orders.order_id
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
""", language="sql")


st.subheader("FULL OUTER JOIN")
st.write("""
- **What It Does**: Returns all rows from both tables, with `NULL` in columns where there is no match.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To ensure no data is excluded from either side of the join, especially useful when both tables contain unique data.
  - **Data Scientists**: For situations where it’s important to include all data from both datasets, even if no matches exist.
  - **Analytics Engineers**: Used for merging datasets from different sources to ensure that no data is lost from either side.
- **Business Case**: Combining two tables to find all customers and all orders, regardless of whether there’s a match.
- **Keywords**: "All rows", "Both tables", "Nulls included".
""")
st.code("""
SELECT customers.customer_id, customers.name, orders.order_id
FROM customers
FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id;
""", language="sql")


st.subheader("CROSS JOIN")
st.write("""
- **What It Does**: Returns the Cartesian product of two tables, combining each row in the first table with every row in the second table.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: Rarely used, but might be used for combinatorial analysis or scenario planning.
  - **Data Scientists**: To generate combinations of datasets, particularly useful in experimental design or feature combinations.
  - **Analytics Engineers**: Occasionally used when generating all possible combinations of data points in analysis or tests.
- **Business Case**: Generating all possible combinations of products and categories for pairing or testing purposes.
- **Keywords**: "All combinations", "Cartesian product", "Pairing".
""")
st.code("""
SELECT products.product_name, categories.category_name
FROM products
CROSS JOIN categories;
""", language="sql")


st.subheader("SELF JOIN")
st.write("""
- **What It Does**: Joins a table to itself to compare rows within the same table.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**:
  - **Data Analysts**: To relate records in the same table, such as finding employees who report to other employees.
  - **Data Scientists**: Rarely used but may be helpful for analysis where relationships within the same dataset need to be identified.
  - **Analytics Engineers**: Occasionally used when building relationships within the same dataset, such as hierarchical or recursive data.
- **Business Case**: Finding hierarchical relationships, such as managers and employees in an organization.
- **Keywords**: "Same table", "Hierarchy", "Self-relationship".
""")
st.code("""
SELECT e1.employee_id, e1.name AS employee_name, e2.name AS manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
""", language="sql")


st.header("Subqueries")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\subqueries.png", caption="Subquery Commands", use_column_width=True)
st.subheader("Subquery in SELECT")
st.write("""
- **What It Does**: Allows using the result of another query as a derived value within the `SELECT` statement.
- **Category**: Data Query Language (DQL)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To enrich reports by adding calculated metrics like totals or averages for better insights.
  - **Data Engineers**: To preprocess data when designing reporting views or materialized queries.
- **Business Case**: Adding aggregated metrics like total sales or average order value as columns to a report.
- **Keywords**: "Derived column", "Calculate", "Nested query".
""")
st.code("""
SELECT 
    customer_id, 
    (SELECT SUM(order_total) 
     FROM orders o2 
     WHERE o2.customer_id = o1.customer_id) AS total_spent
FROM customers o1;
""", language="sql")


st.subheader("Subquery in WHERE")
st.write("""
- **What It Does**: Filters rows based on criteria derived from another query.
- **Category**: Data Query Language (DQL)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To filter data dynamically based on complex conditions for ad-hoc analysis.
  - **Data Scientists**: To create datasets with specific criteria for model training and evaluation.
- **Business Case**: Finding customers who placed orders above a certain threshold, determined dynamically.
- **Keywords**: "Condition", "Filter", "Dynamic threshold".
""")
st.code("""
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE order_total > 500
);
""", language="sql")


st.subheader("Subquery in FROM")
st.write("""
- **What It Does**: Treats the result of a subquery as a temporary table that can be queried further.
- **Category**: Data Query Language (DQL)
- **Roles Most Likely to Use**: 
  - **Data Analysts**: To analyze pre-aggregated or grouped data for reporting purposes.
  - **Data Engineers**: To structure intermediate data during ETL processes for further transformation.
  - **Analytics Engineers**: To design intermediate layers in data models for visualization tools.
- **Business Case**: Analyzing aggregated or preprocessed data like average sales by region.
- **Keywords**: "Derived table", "Temporary data", "Intermediate query".
""")
st.code("""
SELECT region, AVG(total_sales) AS avg_sales
FROM (
    SELECT region, SUM(order_total) AS total_sales
    FROM orders
    GROUP BY region
) sales_data
GROUP BY region;
""", language="sql")

st.header("Set Operations")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\operations.jpg", caption="Set Operations", use_column_width=True)
st.subheader("UNION")
st.write("""
- **What It Does**: Combines the results of two or more `SELECT` queries into a single result set, removing duplicates.
**Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analyst**: Often used to merge data from multiple sources or tables for reporting purposes.
  - **Data Scientist**: Useful when consolidating datasets for model training or exploratory analysis.
- **Business Case**: Merging lists of unique data, such as active and inactive customers, into one report.
- **Keywords**: "Combine", "Merge", "Unique", "Unify".
""")
st.code("""
SELECT customer_id, customer_name
FROM active_customers
UNION
SELECT customer_id, customer_name
FROM inactive_customers;
""", language="sql")


st.subheader("UNION ALL")
st.write("""
- **What It Does**: Combines the results of two or more `SELECT` queries into a single result set, retaining duplicates.
-- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analyst**: Analyzes combined datasets while retaining duplicates for detailed insights.
  - **Analytics Engineer**: Used in ETL pipelines to merge datasets where duplicates are expected or required.
- **Business Case**: Combining data without removing duplicates, such as all sales transactions from multiple regions.
- **Keywords**: "Combine", "Merge", "Duplicates allowed", "All data".
""")
st.code("""
SELECT order_id, order_total
FROM online_orders
UNION ALL
SELECT order_id, order_total
FROM in_store_orders;
""", language="sql")


st.subheader("INTERSECT")
st.write("""
- **What It Does**: Returns only the rows that are present in both queries' result sets.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Analyst**: Identifies common data points, such as customers common to two systems.
  - **Data Scientist**: Finds overlapping data when integrating multiple datasets for analysis.
- **Business Case**: Finding overlapping data, such as customers who placed orders in both the online and in-store systems.
- **Keywords**: "Overlap", "Common records", "Intersection", "Both queries".
""")
st.code("""
SELECT customer_id
FROM online_orders
INTERSECT
SELECT customer_id
FROM in_store_orders;
""", language="sql")


st.subheader("EXCEPT")
st.write("""
- **What It Does**: Returns rows from the first query that are not present in the second query's result set.
- **Category**: DQL (Data Query Language)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Compares datasets to ensure consistency across systems.
  - **Analytics Engineer**: Identifies discrepancies during ETL processes or data validation.
- **Business Case**: Identifying discrepancies, such as customers in one system but not in another.
- **Keywords**: "Difference", "Exclusive", "Not in", "Mismatch".
""")
st.code("""
SELECT customer_id
FROM online_orders
EXCEPT
SELECT customer_id
FROM in_store_orders;
""", language="sql")


st.header("Data Modification")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\modification.png", caption="Data Modification", use_column_width=True)
st.subheader("INSERT")
st.write("""
- **What It Does**: Adds new rows to a table.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Responsible for creating pipelines to populate tables with new data.
  - **Analytics Engineer**: Inserts pre-processed or cleaned data into analytic tables.
- **Business Case**: Adding new customer records, inserting sales transactions, or appending log entries.
- **Business Case**: Adding new customer records, inserting sales transactions, or appending log entries.
- **Keywords**: "Add", "Create", "New", "Insert".
""")
st.code("""
INSERT INTO customers (customer_id, customer_name, email)
VALUES (1, 'John Doe', 'john.doe@example.com');
""", language="sql")


st.subheader("UPDATE")
st.write("""
- **What It Does**: Modifies existing rows in a table based on a condition.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Updates pipeline-generated data when corrections are required.
  - **Data Analyst**: Fixes errors in datasets for reporting purposes.
- **Business Case**: Updating customer contact details, correcting errors in sales data, or changing the status of an order.
- **Keywords**: "Change", "Modify", "Update", "Edit".
""")
st.code("""
UPDATE orders
SET status = 'Shipped'
WHERE order_id = 101;
""", language="sql")


st.subheader("DELETE")
st.write("""
- **What It Does**: Removes rows from a table based on a condition.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Deletes obsolete or invalid data from staging or raw tables.
  - **Analytics Engineer**: Clears out outdated analytic data before reprocessing.
- **Business Case**: Deleting obsolete data, removing duplicate records, or clearing canceled orders.
- **Keywords**: "Remove", "Delete", "Clear", "Purge".
""")
st.code("""
DELETE FROM orders
WHERE status = 'Canceled';
""", language="sql")


st.header("Indexing")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\index.png", caption="Index Commands", use_column_width=True)
st.subheader("CREATE INDEX")
st.write("""
- **What It Does**: Creates an index on a table to speed up data retrieval operations.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Creates indexes to optimize query performance in data pipelines and storage systems.
  - **Analytics Engineer**: Ensures analytical queries run efficiently on key columns.
- **Business Case**: Optimizing query performance for frequently searched columns or large datasets.
- **Keywords**: "Speed up", "Optimize", "Index", "Search".
""")
st.code("""
CREATE INDEX idx_customer_name
ON customers (customer_name);
""", language="sql")

st.subheader("DROP INDEX")
st.write("""
- **What It Does**: Removes an existing index from a table.
 **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Removes unused or redundant indexes to reduce storage overhead or improve write operations.
- **Business Case**: Removing unused or redundant indexes to optimize storage or maintain performance during updates and inserts.
- **Keywords**: "Remove index", "Delete index", "Optimize storage".
""")
st.code("""
DROP INDEX idx_customer_name
ON customers;
""", language="sql")

st.subheader("UNIQUE INDEX")
st.write("""
- **What It Does**: Ensures all values in the indexed column(s) are unique, preventing duplicates.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Enforces uniqueness constraints in database schemas.
- **Business Case**: Enforcing uniqueness on email addresses, product IDs, or usernames in databases.
- **Keywords**: "Unique", "No duplicates", "Distinct values".
""")
st.code("""
CREATE UNIQUE INDEX idx_unique_email
ON customers (email);
""", language="sql")

st.subheader("FULLTEXT INDEX")
st.write("""
- **What It Does**: Creates an index optimized for full-text search in text columns.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Implements full-text indexing for fast searching in text-heavy databases.
- **Business Case**: Enabling fast searches in columns containing large textual data, such as blog posts or product descriptions.
- **Keywords**: "Search text", "Full-text", "Text indexing".
""")
st.code("""
CREATE FULLTEXT INDEX idx_fulltext_description
ON products (description);
""", language="sql")
 
st.subheader("COMPOSITE INDEX")
st.write("""
- **What It Does**: Creates an index on two or more columns, optimizing queries that filter or sort on multiple columns.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Builds composite indexes to enhance performance in multi-condition queries.
  - **Analytics Engineer**: Uses composite indexes to optimize complex analytical queries.
- **Business Case**: Speeding up complex queries involving multiple conditions, such as filtering by city and age group.
- **Keywords**: "Multiple columns", "Multi-condition", "Query optimization".
""")
st.code("""
CREATE INDEX idx_city_age
ON customers (city, age);
""", language="sql")


st.header("Transactions")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\transaction.png", caption="Transaction Commands", use_column_width=True)
st.subheader("BEGIN TRANSACTION")
st.write("""
- **What It Does**: Starts a new transaction to group multiple SQL operations as a single unit of work.
- **Category**: Transaction Control Language (TCL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Ensures consistency when performing multiple dependent operations.
  - **Data Analyst**: Uses transactions to maintain data integrity during analysis adjustments.         
- **Business Case**: Used when multiple dependent operations must succeed together or fail together.
- **Keywords**: "Start transaction", "Group operations", "All-or-nothing".
""")
st.code("""
BEGIN TRANSACTION;
-- Perform operations
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
""", language="sql")


st.subheader("COMMIT")
st.write("""
- **What It Does**: Saves all changes made during the transaction permanently to the database.
- **Category**: Transaction Control Language (TCL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Finalizes changes after successful operations.
  - **Analytics Engineer**: Ensures reliable updates to data pipelines or transformations.         
- **Business Case**: Finalizing changes after successfully completing a batch of operations.
- **Keywords**: "Finalize", "Save changes", "Commit changes".
""")
st.code("""
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
""", language="sql")


st.subheader("ROLLBACK")
st.write("""
- **What It Does**: Undoes all changes made during the transaction, reverting the database to its previous state.
- **Category**: Transaction Control Language (TCL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Prevents saving partial or incorrect data during operations.
  - **Data Analyst**: Ensures integrity when working with temporary or test data.         
- **Business Case**: Used when an error occurs, ensuring no partial or invalid data is saved.
- **Keywords**: "Undo changes", "Revert", "Error handling".
""")
st.code("""
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
-- Error occurs here
ROLLBACK;
""", language="sql")


st.subheader("SAVEPOINT")
st.write("""
- **What It Does**: Creates a checkpoint within a transaction, allowing partial rollbacks to that point without undoing the entire transaction.
- **Category**: Transaction Control Language (TCL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Adds checkpoints to enable fine-grained transaction control.
  - **Analytics Engineer**: Manages partial operations during complex data updates.         
- **Business Case**: Useful for complex operations with multiple stages, where only certain parts may need to be reverted.
- **Keywords**: "Checkpoint", "Partial rollback", "Transaction stages".
""")
st.code("""
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
SAVEPOINT sp1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
ROLLBACK TO sp1; -- Revert to savepoint
COMMIT;
""", language="sql")


st.subheader("SET TRANSACTION ISOLATION LEVEL")
st.write("""
- **What It Does**: Configures the isolation level for a transaction, determining the visibility of changes made by other transactions.
- **Category**: Transaction Control Language (TCL)
- **Roles Most Likely to Use**: 
  - **Data Engineer**: Adjusts isolation levels to balance consistency and concurrency.
  - **Analytics Engineer**: Ensures appropriate visibility and performance for analytical queries.         
- **Business Case**: Used to balance consistency and performance depending on business needs.
- **Keywords**: "Consistency", "Isolation", "Transaction conflict resolution".
""")
st.code("""
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;
-- Operations
COMMIT;
""", language="sql")

st.header("Views")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\views.jpg", caption="Views Commands", use_column_width=True)
st.subheader("CREATE VIEW")
st.write("""
- **What It Does**: Creates a virtual table (view) based on the result set of an SQL query. Views can simplify complex queries by encapsulating them in reusable objects.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Simplifies complex queries by creating reusable views for reporting and analysis.
  - **Data Engineer**: Builds views to standardize data access and reduce query complexity for downstream users.
- **Business Case**: Simplifies frequent or complex queries, enhances security by restricting access to specific columns, and supports reporting needs.
- **Keywords**: "Simplify query", "Encapsulate", "Reusable", "Virtual table".
""")
st.code("""
CREATE VIEW Active_Customers AS
SELECT customer_id, name, email
FROM customers
WHERE status = 'Active';
""", language="sql")


st.subheader("DROP VIEW")
st.write("""
- **What It Does**: Removes a view from the database.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Deletes outdated or unused views to maintain a clean database schema.
  - **Analytics Engineer**: Removes views that are no longer relevant to updated analysis workflows.
- **Business Case**: Used to clean up obsolete or unnecessary views that are no longer needed.
- **Keywords**: "Remove view", "Delete view", "Clean up".
""")
st.code("""
DROP VIEW Active_Customers;
""", language="sql")


st.subheader("ALTER VIEW")
st.write("""
- **What It Does**: Modifies an existing view's definition without deleting and recreating it.
- **Category**: Data Definition Language (DDL)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Updates views to reflect changes in underlying data structures.
  - **Analytics Engineer**: Adjusts views to align with updated reporting or analysis requirements.
- **Business Case**: Updates views when underlying table structures or business logic change.
- **Keywords**: "Modify view", "Update view", "Change view definition".
""")
st.code("""
ALTER VIEW Active_Customers AS
SELECT customer_id, name, email, last_order_date
FROM customers
WHERE status = 'Active';
""", language="sql")


st.subheader("INSERT INTO VIEW")
st.write("""
- **What It Does**: Inserts data into a table through a view if the view is updatable (based on specific rules).
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Inserts data into base tables via views for standardization.
  - **Analytics Engineer**: Adds data to underlying tables while using a structured view for consistency.         
- **Business Case**: Adds new rows to the underlying table using the view for controlled data access.
- **Keywords**: "Insert data", "Add rows", "Insert through view".
""")
st.code("""
INSERT INTO Active_Customers (customer_id, name, email)
VALUES (101, 'John Doe', 'johndoe@example.com');
""", language="sql")


st.subheader("UPDATE VIEW")
st.write("""
- **What It Does**: Updates data in a table through a view if the view is updatable.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Updates underlying table data via views to ensure consistency.
  - **Analytics Engineer**: Makes adjustments to base tables using views that enforce business rules.          
- **Business Case**: Modifies existing records in the underlying table using the view for restricted data updates.
- **Keywords**: "Update data", "Modify rows", "Update through view".
""")
st.code("""
UPDATE Active_Customers
SET email = 'newemail@example.com'
WHERE customer_id = 101;
""", language="sql")

st.header("Triggers")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\trigger.png", caption="Trigger Commands", use_column_width=True)
st.subheader("CREATE TRIGGER")
st.write("""
- **What It Does**: Creates a trigger, a stored procedure that automatically executes in response to specific events (INSERT, UPDATE, DELETE) on a table or view.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Uses triggers to automate database tasks like logging or enforcing rules.
  - **Data Analyst**: Leverages triggers to ensure data consistency during insert/update/delete operations.
- **Business Case**: Automates tasks such as auditing changes, enforcing business rules, or synchronizing related tables.
- **Keywords**: "Automate actions", "Trigger events", "Enforce rules", "Audit changes".
""")
st.code("""
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  INSERT INTO order_audit (order_id, status, created_at)
  VALUES (NEW.order_id, NEW.status, NOW());
END;
""", language="sql")


st.subheader("DROP TRIGGER")
st.write("""
- **What It Does**: Removes a trigger from the database.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Deletes obsolete or redundant triggers to improve database maintainability.
  - **Analytics Engineer**: Removes triggers that no longer align with updated analytical processes.        
- **Business Case**: Cleans up triggers that are no longer relevant or required.
- **Keywords**: "Remove trigger", "Delete trigger", "Cleanup".
""")
st.code("""
DROP TRIGGER after_order_insert;
""", language="sql")


st.subheader("AFTER INSERT/UPDATE/DELETE")
st.write("""
- **What It Does**: Executes the trigger's code after an INSERT, UPDATE, or DELETE operation is performed on a table.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Logs changes to audit tables or updates dependent systems.
  - **Analytics Engineer**: Ensures data transformations occur after data modifications.
- **Business Case**: Logs changes, updates dependent records, or enforces data integrity after the primary operation.
- **Keywords**: "Post-action", "Log changes", "Cascade updates".
""")
st.code("""
CREATE TRIGGER after_customer_update
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
  INSERT INTO customer_audit (customer_id, old_email, new_email, updated_at)
  VALUES (OLD.customer_id, OLD.email, NEW.email, NOW());
END;
""", language="sql")


st.subheader("BEFORE INSERT/UPDATE/DELETE")
st.write("""
- **What It Does**: Executes the trigger's code before an INSERT, UPDATE, or DELETE operation is performed on a table.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Validates or modifies data before it's written to the database.
  - **Analytics Engineer**: Ensures data meets predefined criteria before updates or inserts.
- **Business Case**: Validates data, prevents invalid operations, or enforces rules before the main operation executes.
- **Keywords**: "Pre-action", "Validate", "Prevent errors".
""")
st.code("""
CREATE TRIGGER before_order_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
  IF NEW.total_amount <= 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Order amount must be positive.';
  END IF;
END;
""", language="sql")

st.header ("Common Table Expressions "CTE"")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\CTE.png", caption="CTE Commands", use_column_width=True)
st.subheader("WITH CTE AS")
st.write("""
- **What It Does**: Creates a Common Table Expression (CTE), a temporary result set that can be referenced within a SQL query.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses CTEs to break down complex queries into manageable parts for better readability.
  - **Data Engineer**: Implements CTEs for modular query design and reusability in data pipelines.  
- **Business Case**: Simplifies complex queries by breaking them into manageable parts, improves readability, and promotes reusability of query logic.
- **Keywords**: "Simplify query", "Temporary result", "Organize logic".
""")
st.code("""
WITH CustomerOrders AS (
  SELECT customer_id, COUNT(order_id) AS order_count
  FROM orders
  GROUP BY customer_id
)
SELECT customer_id, order_count
FROM CustomerOrders
WHERE order_count > 5;
""", language="sql")


st.subheader("RECURSIVE CTE")
st.write("""
- **What It Does**: Extends the capabilities of a CTE to allow recursive queries, which call themselves iteratively.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Processes hierarchical data like organizational charts or graph structures.
  - **Data Analyst**: Uses recursive CTEs for pathfinding or tree-based calculations.        
- **Business Case**: Useful for hierarchical data like organizational charts, folder structures, or navigating parent-child relationships.
- **Keywords**: "Hierarchy", "Parent-child", "Recursive relationships".
""")
st.code("""
WITH RECURSIVE EmployeeHierarchy AS (
  SELECT employee_id, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.manager_id, eh.level + 1
  FROM employees e
  INNER JOIN EmployeeHierarchy eh
  ON e.manager_id = eh.employee_id
)
SELECT employee_id, manager_id, level
FROM EmployeeHierarchy;
""", language="sql")


st.subheader("WITH TEMPORARY CTE")
st.write("""
- **What It Does**: A variant of CTEs that acts as a temporary construct, often for session-specific or throwaway computations.
- **Category**: Data Manipulation Language (DML)
- **Roles Most Likely to Use**:
  - **Data Engineer**: Uses temporary CTEs for intermediate processing within ETL workflows.
  - **Data Analyst**: Creates temporary CTEs for ad-hoc query simplifications.
- **Business Case**: Used for quick one-off analyses or temporary calculations that don’t need permanent storage or further usage.
- **Keywords**: "Temporary calculation", "Session-specific", "Quick analysis".
""")
st.code("""
WITH TempOrderSummary AS (
  SELECT product_id, SUM(quantity) AS total_sold
  FROM order_details
  GROUP BY product_id
)
SELECT product_id, total_sold
FROM TempOrderSummary
WHERE total_sold > 100;
""", language="sql")


st.header("Window Functions")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\windowfunctions.png", caption="Window Functions", use_column_width=True)
st.subheader("ROW_NUMBER()")
st.write("""
- **What It Does**: Assigns a unique sequential integer to rows within a partition, starting at 1.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses ROW_NUMBER() to identify and filter duplicates or rank rows within partitions.
  - **Data Engineer**: Implements ROW_NUMBER() for data deduplication or ranking logic in pipelines.
- **Business Case**: Useful for pagination or uniquely identifying rows in a sorted subset.
- **Keywords**: "Sequential ID", "Unique row", "Pagination".
""")
st.code("""
SELECT ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num,
       employee_id, department_id, salary
FROM employees;
""", language="sql")


st.subheader("RANK()")
st.write("""
- **What It Does**: Assigns a rank to rows in a partition based on order, with gaps for ties.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Applies RANK() for leaderboard or competition rankings.
  - **Data Engineer**: Uses RANK() for rank-based data filtering or ordering.
- **Business Case**: Identifying top performers or ranking entities with ordered data.
- **Keywords**: "Rank", "Top performers", "Order with ties".
""")
st.code("""
SELECT RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank,
       employee_id, department_id, salary
FROM employees;
""", language="sql")


st.subheader("DENSE_RANK()")
st.write("""
- **What It Does**: Similar to `RANK()` but without gaps for ties.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Creates dense rankings for ordered categories.
  - **Data Engineer**: Uses DENSE_RANK() for tightly ordered ranking systems.
- **Business Case**: Useful when consistent numbering is needed for tied ranks.
- **Keywords**: "Dense rank", "Rank without gaps", "Consistent numbering".
""")
st.code("""
SELECT DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank,
       employee_id, department_id, salary
FROM employees;
""", language="sql")


st.subheader("NTILE()")
st.write("""
- **What It Does**: Divides rows into a specified number of buckets and assigns a bucket number.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Segments data into quartiles, deciles, or percentiles.
  - **Data Engineer**: Uses NTILE() for data distribution analysis or tiered grouping.
- **Business Case**: Percentile calculations or segmenting data into quantiles.
- **Keywords**: "Buckets", "Percentiles", "Quantiles".
""")
st.code("""
SELECT NTILE(4) OVER (PARTITION BY department_id ORDER BY salary DESC) AS quartile,
       employee_id, department_id, salary
FROM employees;
""", language="sql")


st.subheader("LEAD()")
st.write("""
- **What It Does**: Provides access to the next row's value in the same partition.
- **Category**: DML (Data Manipulation Language)
 - **Roles Most Likely to Use**:
  - **Data Analyst**: Uses LEAD() to compare a value with the next value in a sequence.
  - **Data Engineer**: Implements LEAD() for time-series or trend analysis.        
- **Business Case**: Compare current value to the next value, such as in time series or sequential data.
- **Keywords**: "Next value", "Compare to future row", "Sequential analysis".
""")
st.code("""
SELECT employee_id, salary,
       LEAD(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS next_salary
FROM employees;
""", language="sql")


st.subheader("LAG()")
st.write("""
- **What It Does**: Provides access to the previous row's value in the same partition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses LAG() to compare a value with the previous value in a sequence.
  - **Data Engineer**: Implements LAG() for historical comparison or time-series analysis.      
- **Business Case**: Compare current value to the previous value, often in trends or sequential data.
- **Keywords**: "Previous value", "Compare to prior row", "Trends".
""")
st.code("""
SELECT employee_id, salary,
       LAG(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS previous_salary
FROM employees;
""", language="sql")


st.subheader("FIRST_VALUE()")
st.write("""
- **What It Does**: Retrieves the first value in the window partition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses FIRST_VALUE() to identify baseline or starting values.
  - **Data Engineer**: Applies FIRST_VALUE() for initialization or benchmark comparisons.
- **Business Case**: Identify baseline values or starting points in data.
- **Keywords**: "First value", "Starting point", "Baseline".
""")
st.code("""
SELECT employee_id, salary,
       FIRST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS highest_salary
FROM employees;
""", language="sql")


st.subheader("LAST_VALUE()")
st.write("""
- **What It Does**: Retrieves the last value in the window partition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses LAST_VALUE() to identify ending or most recent values.
  - **Data Engineer**: Applies LAST_VALUE() for finalization or end-state comparisons.
- **Business Case**: Identify ending points or final values in sorted data.
- **Keywords**: "Last value", "Ending point", "Final value".
""")
st.code("""
SELECT employee_id, salary,
       LAST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_salary
FROM employees;
""", language="sql")


st.subheader("SUM() OVER")
st.write("""
- **What It Does**: Computes a running total or aggregate over a partition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses SUM() OVER() for running totals or cumulative metrics.
  - **Data Engineer**: Implements SUM() OVER() for aggregated metrics in pipelines.
- **Business Case**: Track cumulative metrics such as total sales or running totals.
- **Keywords**: "Running total", "Cumulative sum", "Aggregate by partition".
""")
st.code("""
SELECT employee_id, department_id, salary,
       SUM(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS running_total
FROM employees;
""", language="sql")


st.subheader("AVG() OVER")
st.write("""
- **What It Does**: Computes a running average or aggregate over a partition.
- **Category**: DML (Data Manipulation Language)
 **Roles Most Likely to Use**:
  - **Data Analyst**: Uses AVG() OVER() for running averages or cumulative metrics.
  - **Data Engineer**: Implements AVG() OVER() for trend analysis in pipelines. 
- **Business Case**: Track trends in averages or moving averages within partitions.
- **Keywords**: "Running average", "Cumulative average", "Trends".
""")
st.code("""
SELECT employee_id, department_id, salary,
       AVG(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS running_avg
FROM employees;
""", language="sql")


st.subheader("PARTITION BY")
st.write("""
- **What It Does**: Divides a result set into partitions to apply window functions separately to each partition.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Groups data for granular analysis within partitions.
  - **Data Engineer**: Uses PARTITION BY to isolate data subsets for computations.
- **Business Case**: Perform calculations or aggregations for distinct groups in a dataset.
- **Keywords**: "Groups", "Partitioned analysis", "Distinct sets".
""")
st.code("""
SELECT employee_id, department_id, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS row_num
FROM employees;
""", language="sql")


st.subheader("ORDER BY")
st.write("""
- **What It Does**: Defines the order of rows within a partition for window functions.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses ORDER BY within partitions to calculate metrics like running totals or rankings.
  - **Data Engineer**: Ensures data is properly ordered for pipelines using window functions.
- **Business Case**: Specify sort order for calculations like ranking or running totals.
- **Keywords**: "Sorting", "Ordering", "Sequence".
""")
st.code("""
SELECT employee_id, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
FROM employees;
""", language="sql")


st.header("Date & Time Functions")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\calendar.png", caption="Date & Time Commands", use_column_width=True)
st.subheader("GETDATE()")
st.write("""
- **What It Does**: Returns the current date and time of the system.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses GETDATE() for timestamping reports or creating audit trails.
  - **Data Engineer**: Applies GETDATE() for logging or capturing system-generated timestamps.
- **Business Case**: Useful for logging actions or tracking when an event occurred.
- **Keywords**: "Current date", "System time", "Timestamp now".
""")
st.code("""
SELECT GETDATE();
""", language="sql")


st.subheader("CURRENT_TIMESTAMP")
st.write("""
- **What It Does**: Provides the current date and time in UTC.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Similar use to GETDATE(), but specifically for SQL Server systems.
  - **Data Engineer**: Used in ETL processes to record timestamps of operations.
- **Business Case**: Standardized timestamp for global applications.
- **Keywords**: "Current UTC time", "Timestamp", "Standard time".
""")
st.code("""
SELECT CURRENT_TIMESTAMP;
""", language="sql")


st.subheader("DATEADD()")
st.write("""
- **What It Does**: Adds a specific interval to a date.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Calculates future or past dates for analysis.
  - **Data Engineer**: Adjusts timestamps in pipelines or workflows.
- **Business Case**: Calculate future or past dates based on specific intervals (e.g., adding days, months).
- **Keywords**: "Add time", "Future date", "Adjust date".
""")
st.code("""
SELECT DATEADD(day, 10, '2024-12-27') AS NewDate;
""", language="sql")


st.subheader("DATEDIFF()")
st.write("""
- **What It Does**: Calculates the difference between two dates in specified units (days, months, etc.).
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Calculates the duration between events for reporting.
  - **Data Engineer**: Measures processing or execution time in workflows
- **Business Case**: Measure the time elapsed between events.
- **Keywords**: "Time difference", "Elapsed time", "Gap in dates".
""")
st.code("""
SELECT DATEDIFF(day, '2024-01-01', '2024-12-27') AS DaysElapsed;
""", language="sql")


st.subheader("DATEPART()")
st.write("""
- **What It Does**: Extracts a specific part of a date (e.g., year, month, day).
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Breaks down dates for granular analysis (e.g., by month or year).
  - **Data Engineer**: Extracts date parts for categorization or grouping in ETL processes.
- **Business Case**: Retrieve components of a date for analysis or filtering.
- **Keywords**: "Extract year", "Part of date", "Date component".
""")
st.code("""
SELECT DATEPART(year, '2024-12-27') AS YearPart;
""", language="sql")


st.subheader("DATE_FORMAT()")
st.write("""
- **What It Does**: Formats a date value into a specified format.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Converts dates for presentation or reporting.
  - **Data Engineer**: Formats dates to standardize across systems.
- **Business Case**: Display dates in a user-friendly or localized format.
- **Keywords**: "Format date", "Display date", "Custom date format".
""")
st.code("""
SELECT DATE_FORMAT('2024-12-27', '%W, %M %d, %Y') AS FormattedDate;
""", language="sql")


st.subheader("NOW()")
st.write("""
- **What It Does**: Returns the current date and time.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Generates real-time timestamps for analysis.
  - **Data Engineer**: Captures timestamps for data pipeline operations.
- **Business Case**: Useful for logging, tracking real-time actions, or as a timestamp.
- **Keywords**: "Current time", "Real-time date", "System date".
""")
st.code("""
SELECT NOW();
""", language="sql")


st.subheader("EXTRACT()")
st.write("""
- **What It Does**: Extracts a specified part (e.g., year, month) from a date or time.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Uses for granular time-based analysis.
  - **Data Engineer**: Extracts components for filtering or transformation.
- **Business Case**: Analyze specific components of timestamps.
- **Keywords**: "Extract part", "Break down date", "Analyze component".
""")
st.code("""
SELECT EXTRACT(YEAR FROM '2024-12-27') AS ExtractedYear;
""", language="sql")


st.subheader("TIMESTAMPDIFF()")
st.write("""
- **What It Does**: Calculates the difference between two timestamps in a specified unit (e.g., seconds, hours).
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Analyzes durations between timestamps.
  - **Data Engineer**: Measures intervals for performance or scheduling.
- **Business Case**: Determine the duration of events or gaps in time.
- **Keywords**: "Timestamp difference", "Duration", "Elapsed time".
""")
st.code("""
SELECT TIMESTAMPDIFF(MONTH, '2024-01-01', '2024-12-27') AS MonthDifference;
""", language="sql")


st.header("Conditional Logic")
st.image("C:\Users\Sloan\Documents\Github\SQL_Stuff\logic.png", caption="Basic SQL Commands", use_column_width=True)
st.subheader("CASE WHEN")
st.write("""
- **What It Does**: Allows conditional logic within SQL queries. It evaluates conditions and returns specific values based on those conditions.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Categorizes data or creates derived fields based on conditions.
  - **Data Engineer**: Implements conditional transformations in ETL pipelines.
- **Business Case**: Useful for categorizing data, creating derived columns, or performing conditional transformations.
- **Keywords**: "If-then logic", "Conditional", "Categorize", "Transform", "Evaluate conditions".
""")
st.code("""
SELECT 
  employee_id, 
  salary, 
  CASE 
    WHEN salary > 50000 THEN 'High'
    WHEN salary BETWEEN 30000 AND 50000 THEN 'Medium'
    ELSE 'Low'
  END AS SalaryCategory
FROM employees;
""", language="sql")


st.subheader("IFNULL()")
st.write("""
- **What It Does**: Replaces `NULL` values with a specified replacement value.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Ensures data completeness by replacing NULLs in analysis.
  - **Data Engineer**: Standardizes data by filling NULL values during ETL.
- **Business Case**: Ensure no `NULL` values in datasets, providing default values for calculations or displays.
- **Keywords**: "Handle nulls", "Replace null", "Default value", "Fill blanks".
""")
st.code("""
SELECT 
  employee_id, 
  IFNULL(bonus, 0) AS AdjustedBonus
FROM employee_bonuses;
""", language="sql")


st.subheader("COALESCE()")
st.write("""
- **What It Does**: Returns the first non-`NULL` value from a list of arguments.
- **Category**: DML (Data Manipulation Language)
- **Roles Most Likely to Use**:
  - **Data Analyst**: Combines multiple columns or values to ensure data consistency.
  - **Data Engineer**: Resolves missing data issues by prioritizing available values.
- **Business Case**: Handle multiple potential `NULL` values in hierarchical or fallback data fields.
- **Keywords**: "First non-null", "Fallback value", "Default handling", "Null management".
""")
st.code("""
SELECT 
  employee_id, 
  COALESCE(phone_work, phone_mobile, 'No Phone Available') AS ContactNumber
FROM employees;
""", language="sql")