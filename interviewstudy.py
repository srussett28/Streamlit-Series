import streamlit as st
import random

# Load questions
questions = [
    ("How would a colleague, classmate or supervisor describe you?", "Problem Solver: In nearly every engagement I’ve been a part of, I was entrusted with tackling some of the clients’ most complex challenges, often in areas outside my immediate expertise. I thrive on breaking down difficult problems, identifying solutions, and driving meaningful results, even in unfamiliar territories.\n\nAdaptable & Quick Learner: Because I’m often solving problems outside my existing knowledge base, adaptability has become one of my strongest traits. Whether it’s working with new technologies, navigating evolving business landscapes, or learning on the fly, I focus on understanding the problem, learning what’s needed, and delivering solutions efficiently.\n\nTeam Player & Leader: Regardless of the project, I’ve always fostered an environment of collaboration—where success isn’t about individual contributions but about achieving the best outcome as a team. I believe in the 'one team, one fight' mentality, ensuring that no matter what the challenge, we work together to find the best path forward."),
    ("What motivates you to do your best on the job?", "My motivation has been the same since 2011, and it all started with a defining moment in my life. I had just joined the Army after quitting my college football team, feeling directionless and not giving my full effort to anything. Then, within my first week in Afghanistan, my wife called to tell me she was pregnant with our first child. In that instant, everything changed. I realized that someone was going to need me to show up every day, not just for myself but for them. That mindset has driven me ever since. Today, I want my kids to be proud of the work I do. The days I wake up excited to go to work are the ones where I know I'm solving real problems, making an impact, and setting an example for my children—showing them what hard work, resilience, and dedication look like. Whether it’s building a game-changing analytics solution, leading a team through a tough challenge, or driving meaningful change in an organization, I give my best because I know it matters—not just for me, but for my family and those I work with."),
    ("The next morning you say to yourself, ‘I really don’t want to work today because…’? Why?", "Having served in the Army for more than half a decade, I learned that discipline and accountability don’t take days off. As soldiers, we were on duty 24/7—rain, snow, good days, bad days, sick or not. That experience built a mindset where showing up isn’t optional; it’s a responsibility.\n\nOf course, there are mornings where motivation is low—whether it's fatigue, challenges, or just one of those days—but I don’t let that dictate my actions. When that feeling comes, I fall back on my discipline, accountability, and my ‘why’—my family, my team, and the impact I strive to make. Those principles push me forward, ensuring that I give my best even when it’s not easy."),
    ("So far in your career, what is the one thing if you had to do over again, would you do differently?", "If I could do one thing differently, I would have learned to say 'no' more often, much earlier in my career.\n\nI’ve always been someone who wants to help, support, and contribute, but I’ve learned that in business, there will always be more asks than time. Early on, I thought that by saying ‘yes’ to everything, I could make everyone happy and prove my value. But I quickly realized that even when you say ‘yes’ to everything, some people will still be unhappy, and worse—you can end up overworked, stretched thin, and feeling undervalued.\n\nOver time, I’ve learned that setting boundaries isn’t about saying no to work—it’s about saying yes to the right work. Now, I focus on prioritizing high-impact tasks, aligning my efforts with strategic goals, and ensuring that my time is spent on what truly moves the needle. Saying ‘no’ when necessary has made me more effective, allowed me to deliver higher-quality results, and ultimately helped me grow as a leader."),
    ("Can you describe your experience with data quality control and ensuring accuracy, reproducibility, and end-user enablement?", "Situation: At my previous employer, I worked with a multi-billion-dollar liquor distiller undergoing an ERP modernization to Oracle from a legacy DOS-based system. During the transition, it became evident that the company’s master data was in poor shape, making the migration risky without significant data quality improvements.\n\nTask: I was responsible for identifying and resolving all data quality issues to ensure that the data migrated into Oracle was accurate, complete, and consistently formatted.\n\nAction:\n- Extracted all master data from the legacy ERP system.\n- Developed a data summary script to provide a high-level assessment of data health—identifying unique values, distributions, missing data, and outliers.\n- Designed a data cleaning script to standardize formats, handle null values, correct outliers, and enforce data type consistency.\n- Established a repeatable process for data validation, ensuring data quality checks before each migration batch.\n\nResult:\n- In two months, data quality went from a complete unknown to a reliable foundation for decision-making.\n- The organization was able to confidently migrate clean, structured data into Oracle, reducing future data integrity risks.\n- My process became a standardized approach for data quality control, allowing ongoing data governance and reproducibility beyond the initial migration."),
    ("Can you discuss a time when you used statistical methods or trend analysis to drive a business decision?", "Situation: At the liquor distiller, the CFO unexpectedly raised concerns about the Days Payable Outstanding (DPO) figures provided by AP/Treasury, feeling they were not in an advantageous position compared to industry benchmarks.\n\nTask: I needed to analyze vendor payment trends and uncover why DPO was lower than expected, essentially understanding what factors were shortening the company’s payment cycle.\n\nAction:\n- Developed two queries:\n  - Vendor Administrative Data – Included payment terms, categories, and approval processes.\n  - Vendor Spend Data – Captured payment history, invoice amounts, and frequency.\n- Joined these datasets to perform summary statistics on payment terms and vendor contribution to total spend.\n- Identified that 40% of the top 100 vendors (by spend) had payment terms shorter than 10 days, including the top vendor which was due upon receipt.\n- Used trend analysis to show how these short payment terms negatively impacted DPO, making it difficult to maintain a 45-day benchmark.\n\nResult:\n- The company adopted a more structured approach to vendor payment terms and approvals, preventing automatic short-term agreements without procurement oversight.\n- Procurement used my insights to strategically renegotiate vendor terms, improving cash flow management while maintaining strong supplier relationships."),
    ("Tell me about a time when you used data to solve a business problem.", "**Situation:** While working for a large federal healthcare provider, the organization was rolling out multiple new software implementations in waves. As part of this effort, we collected Voice of the Customer (VoC) data after each wave to measure system adoption, user experience, and potential issues. However, the data was being collected but not being leveraged effectively to drive decision-making.\n\n**Task:** My task was to create a VoC dashboard that would provide real-time insights to the executive team during go-live implementations, allowing them to make data-driven decisions on system rollouts.\n\n**Action:**\n- Collected VoC data from multiple sources, including Azure Data Factory and Excel files maintained by different teams.\n- Modeled the backend data structure to enhance interactivity and ensure seamless integration of structured and unstructured data.\n- Developed two dashboards:\n  1. Executive-Level Overview – Provided a high-level summary for quick analysis of trends and key performance indicators.\n  2. Deep-Dive Analytics Page – Allowed teams to drill down into detailed data, uncovering insights on specific implementation issues.\n\n**Result:**\n- The dashboard is now presented at the executive level during go-lives, providing real-time insights into system adoption and user feedback.\n- It has become the organization’s benchmark for tracking Voice of the Customer data, directly influencing decision-making and system improvements.\n- Improved the efficiency of issue resolution by enabling leadership to identify and address adoption challenges faster."),
    ("Tell me about a time when you had to explain a complex concept to a non-technical audience.", "**Situation:** As part of a wave implementation at a large federal healthcare provider, the organization was adopting a new order management system. However, leadership wanted to explore gaps in the system and identify where AI/ML or RPA solutions could enhance efficiency and drive additional value.\n\n**Task:** I was tasked with developing a list of AI/ML and RPA use cases, clearly detailing:\n- What gap each solution addressed\n- How the solution worked (conceptually and technically)\n- Its benefits, cost analysis, and ROI\n- Required data, compute, storage, and integration within their architecture\n- How end-users would interact with these solutions\n\nThe challenge was that many stakeholders, including senior leadership, had limited technical expertise. My goal was to present these concepts in an accessible way that would enable informed decision-making.\n\n**Action:**\n- Compiled a 109-page document outlining 15+ AI/ML and RPA solutions in a way that distilled complex technical concepts into easy-to-understand insights.\n- Used simplified explanations and relatable analogies to make tough concepts digestible.\n- Structured my pitch around real-world examples and interactive discussions instead of just technical documentation.\n\n**Result:**\n- The leadership team fully understood the impact of AI/ML and RPA and was able to make strategic decisions based on my analysis.\n- When the order management system expansion is built on AWS, Deloitte will lead the execution of the pilot plan for selected AI/ML/RPA solutions.\n- High-value solutions will proceed to full-scale implementation and be added to the federal AI Use Case Registry for future scalability."),
    ("Describe a time when you had conflicting data sources. How did you resolve the issue?", "**Situation:** While leading a client’s annual 1099 process, I was tasked with ensuring that vendor payment data was accurate and compliant to avoid legal and financial risks. Historically, the process contained gaps that led to significant rework. IT provided me with two potential reports to determine which vendors required a 1099:\n- Spend Report\n- Paid Report\n\nHowever, I quickly discovered inconsistencies between the two reports—some vendor payment figures did not match, meaning that selecting the wrong dataset could lead to incorrect tax filings and substantial rework costs.\n\n**Task:** I needed to determine which report was the source of truth with 100% certainty.\n\n**Action:**\n- Isolated vendors with discrepancies and analyzed their transaction histories to identify the root cause.\n- Discovered that the Spend Report was overstating vendor payments because it did not account for canceled transactions.\n- Example: If a $100 check was issued but later canceled and reissued, the Spend Report incorrectly counted both transactions, effectively overstating vendor payments.\n- Validated findings with ERP transaction logs and cross-checked payment processing records.\n- Recommended using the Paid Report as the source of truth, ensuring that only successfully processed payments were included.\n\n**Result:**\n- Significant cost avoidance – Prior to implementing this process, substantial manual rework was required to fix incorrect 1099 data.\n- Accuracy improved dramatically – Out of 2,000+ 1099s filed, only one required correction, and that was due to a unique employee-contractor classification issue rather than a reporting error.\n- The organization institutionalized this new process, ensuring future compliance and efficiency."),
    ("Why Do You Want to Join Virginia Tech?", "My decision to transition into higher education is driven by two key factors: **family and impact.**\n\nFirst, family—particularly my children—is a major consideration. In consulting, frequent travel is the norm, often requiring extended time away from home. While going into an office and returning home each evening is one thing, spending multiple days away from my family is another. At this stage in my career, I want to be more present for them while continuing to do meaningful work.\n\nSecond, impact. The Office of Research and Innovation (ORI) plays a critical role in advancing research and supporting Virginia Tech’s mission. I am particularly interested in the research frontiers of AI and quantum computing and was impressed by the partnerships forged with Amazon and Northrop. ORI presents a unique opportunity to contribute to research initiatives that not only strengthen the university’s bottom line but also equip the next generation of learners with the data, tools, and solutions to solve real-world problems.\n\nJoining Virginia Tech allows me to align my expertise with my passion for innovation and education while making a meaningful difference in both my family’s life and the university’s future."),
    ("Why Should We Hire You?", "I believe I am the right fit for this role because I bring a unique combination of deep technical expertise, strategic thinking, and a passion for using data to drive impact—qualities that align perfectly with Virginia Tech’s Office of Research and Innovation (ORI).\n\n**Proven Experience in Data & Analytics:**\nWith over a decade of experience in data-driven decision-making, I have built and led analytics solutions in high-stakes environments, including Fortune 500 companies and large federal institutions. I have experience establishing analytics frameworks that enhance decision-making and drive organizational success. I led the development of a Business Intelligence Center of Excellence, standardizing analytics processes and implementing AI, machine learning, and automation-driven insights to improve data accessibility and executive reporting.\n\n**Ability to Build Scalable, Impactful Solutions:**\nThis role requires someone who can turn complex data into actionable insights that advance research and innovation. I have a track record of doing just that—whether it’s optimizing master data governance, leveraging machine learning for predictive insights, or driving process improvements that resulted in millions in cost savings. I can bring this same level of analytical rigor and solution-building to Virginia Tech, ensuring data is not just collected but leveraged to inform research strategies and institutional growth.\n\n**Alignment with Virginia Tech’s Mission & Culture:**\nBeyond my technical skills, I am passionate about higher education, research, and innovation. I want to be part of an institution that pushes the boundaries of AI, quantum computing, and data science—and Virginia Tech is at the forefront of this transformation. This role is not just a career move for me; it’s an opportunity to make a meaningful impact on the next generation of researchers and lifelong learners."),
    ("What is the difference between a primary key and a foreign key?", "A **primary key** uniquely identifies each record in a table (e.g., `id` in an `employees` table). A **foreign key** is a reference to a primary key in another table, ensuring data integrity between related tables."),
    ("What is normalization, and why is it important?", "Normalization is the process of organizing database tables to reduce redundancy and improve data integrity. It ensures that each piece of data is stored in only one place, making updates and queries more efficient."),
    ("What are the different types of database relationships?", "- **One-to-One (1:1)** – A single record in Table A is linked to a single record in Table B.\n- **One-to-Many (1:M)** – A single record in Table A can be linked to multiple records in Table B (e.g., a customer with multiple orders).\n- **Many-to-Many (M:N)** – Requires a junction table to link records from both tables (e.g., students and courses)."),
    ("What is denormalization, and when would you use it?", "Denormalization is the process of adding redundancy to a database to improve read performance. It is used in reporting or analytical databases where fast queries are more important than storage efficiency."),
    ("What is indexing, and how does it improve performance?", "An **index** is a database structure that speeds up data retrieval by creating a lookup mechanism for queries. It’s like an index in a book, allowing the database to find rows faster."),
    ("What is the difference between clustered and non-clustered indexes?", "- **Clustered Index:** Sorts and stores the data rows in the table physically in order. (Only one per table).\n- **Non-Clustered Index:** Creates a separate structure pointing to the original data (Can have multiple per table)."),
    ("What is a transaction in SQL, and why is it important?", "A **transaction** is a sequence of SQL operations that are treated as a single unit of work. Transactions ensure data consistency and integrity using **ACID** properties (Atomicity, Consistency, Isolation, Durability)."),
    ("What are the ACID properties in databases?", "- **Atomicity:** All parts of a transaction succeed or none do.\n- **Consistency:** The database remains in a valid state before and after a transaction.\n- **Isolation:** Transactions don’t interfere with each other.\n- **Durability:** Once a transaction is committed, it remains permanent."),
    ("What is the difference between DELETE, TRUNCATE, and DROP?", "- **DELETE:** Removes specific rows but logs the action (can be rolled back).\n- **TRUNCATE:** Removes all rows but keeps the table structure (cannot be rolled back).\n- **DROP:** Deletes the entire table, including structure and indexes."),
    ("What is a materialized view, and how is it different from a regular view?", "A **regular view** is a stored SQL query that doesn’t store data. A **materialized view** is a stored query result that needs to be refreshed periodically for updated data."),
    ("What is the difference between UNION and UNION ALL?", "- **UNION** removes duplicates.\n- **UNION ALL** includes duplicates."),
    ("What is the difference between INNER JOIN and LEFT JOIN?", "- **INNER JOIN:** Returns only matching rows from both tables.\n- **LEFT JOIN:** Returns all rows from the left table and matching rows from the right (fills missing data with NULLs)."),
    ("What is a common table expression (CTE), and why is it useful?", "A CTE is a temporary result set that improves query readability and can be referenced multiple times within a query."),
    ("What is the difference between OLTP and OLAP databases?", "- **OLTP (Online Transaction Processing):** Optimized for fast insert/update/delete operations (e.g., banking, e-commerce).\n- **OLAP (Online Analytical Processing):** Optimized for reporting and analysis, using large datasets (e.g., BI tools)."),
    ("What is the purpose of the EXPLAIN command in SQL?", "The **EXPLAIN** command analyzes a query execution plan to help optimize performance by showing how the database processes a query."),
    ("What is referential integrity, and how does it work?", "Referential integrity ensures that foreign key relationships remain valid—i.e., a record in one table cannot reference a non-existent record in another."),
    ("What are stored procedures, and how do they differ from functions?", "- **Stored Procedure:** A set of SQL statements that can return multiple results and perform transactions.\n- **Function:** Returns a single value and can be used in SQL queries."),
    ("What is a self-join, and when would you use it?", "A self-join joins a table to itself to compare rows within the same table.\n**Example use case:** Finding employees who report to the same manager."),
    ("What are window functions, and how are they different from GROUP BY?", "Window functions perform calculations across a set of rows without collapsing them, unlike GROUP BY.\n**Examples:** RANK(), DENSE_RANK(), ROW_NUMBER(), AVG() OVER()."),
    ("What is the difference between an alias and a subquery?", "- **Alias:** A temporary name for a column or table (SELECT column AS alias).\n- **Subquery:** A query within another query (SELECT * FROM (SELECT ...))."),
    ("What are the advantages of using a surrogate key over a natural key?", "- **Surrogate Key (Auto-increment ID):** Unique, independent of data changes.\n- **Natural Key (Real-world attribute):** Tied to business logic, harder to maintain."),
    ("What is the difference between ETL and ELT?", "- **ETL (Extract, Transform, Load):** Data is transformed before loading into the database.\n- **ELT (Extract, Load, Transform):** Data is loaded first, then transformed using SQL."),
    ("How do you prevent SQL injection?", "- Use prepared statements & parameterized queries.\n- Restrict user permissions.\n- Validate user input."),
    ("What is the difference between a schema and a database?", "- **Database:** A collection of tables, schemas, indexes, views, and stored procedures.\n- **Schema:** A logical grouping of tables and database objects within a database."),
    ("What are database constraints, and why are they important?", "Constraints enforce rules to maintain data integrity:\n- **NOT NULL** – Ensures a column cannot have NULL values.\n- **UNIQUE** – Ensures all values in a column are distinct.\n- **CHECK** – Enforces a condition on column values.\n- **DEFAULT** – Provides a default value when none is specified.\n- **FOREIGN KEY** – Ensures referential integrity."),
    ("What is the difference between a database and a data warehouse?", "- A **database** is designed for transactional processing (OLTP), focusing on real-time insert/update/delete operations (e.g., banking systems).\n- A **data warehouse** is optimized for analytical queries (OLAP), storing historical data for reporting and decision-making."),
    ("What is a fact table and a dimension table in a data warehouse?", "- **Fact Table:** Stores numerical data (facts) such as sales revenue, transaction amounts, etc.\n- **Dimension Table:** Stores descriptive attributes (dimensions) such as time, location, or customer information."),
    ("What is the difference between a star schema and a snowflake schema?", "- **Star Schema:** A denormalized structure where dimension tables connect directly to a fact table.\n- **Snowflake Schema:** A normalized structure where dimension tables are further split into sub-dimensional ones."),
    ("What are database partitions, and why are they useful?", "Partitioning divides a large table into smaller, manageable pieces (e.g., by date, region). This improves performance and makes queries faster."),
    ("What is sharding in databases?", "Sharding splits a large database into multiple smaller databases across servers to improve performance and scalability."),
    ("What is referential integrity, and how do you enforce it?", "Referential integrity ensures relationships between tables remain consistent, typically using foreign keys."),
    ("What is the difference between a view and a table?", "- **Table:** Stores data physically.\n- **View:** A virtual table based on a query, does not store data but retrieves it dynamically."),
    ("How do you handle NULL values in a database?", "- Use **COALESCE()** or **ISNULL()** to replace NULLs with default values.\n- Apply **NOT NULL** constraints to prevent NULLs.\n- Design queries to handle NULL scenarios properly."),
    ("What is a surrogate key, and when would you use one?", "A surrogate key is a system-generated unique identifier (e.g., auto-incremented ID). It is preferred when natural keys are too complex or subject to change."),
    ("What are the benefits of using stored procedures?", "- **Code reusability** (prewritten logic).\n- **Performance optimization** (precompiled).\n- **Security** (controlled execution of SQL)."),
    ("What is the difference between a temporary table and a permanent table?", "- **Temporary Table:** Exists only for the duration of a session or transaction.\n- **Permanent Table:** Persists in the database until manually deleted."),
    ("What is database replication, and why is it used?", "Replication creates copies of a database across multiple servers to improve availability and disaster recovery."),
    ("What is the difference between horizontal and vertical scaling?", "- **Horizontal Scaling:** Adding more servers (sharding).\n- **Vertical Scaling:** Adding more resources (RAM, CPU) to an existing server."),
    ("What are the advantages of using JSON or XML in databases?", "- JSON/XML support unstructured data storage.\n- Ideal for API responses and document-based data."),
    ("What is the CAP theorem in distributed databases?", "CAP theorem states that a distributed system can have only two of the three:\n- **Consistency** (all nodes see the same data).\n- **Availability** (every request gets a response).\n- **Partition Tolerance** (continues working despite network failures)."),
    ("What is database indexing, and what are the trade-offs?", "- Indexing speeds up read operations but slows down inserts/updates.\n- Too many indexes increase storage overhead."),
    ("What are the benefits of using a composite index?", "- Improves performance for queries filtering on multiple columns.\n- Reduces the need for multiple individual indexes."),
    ("What is the difference between full-text search and a regular index search?", "- **Regular Index:** Optimized for exact matches or small range queries.\n- **Full-Text Search:** Optimized for searching long text fields (e.g., finding words in articles)."),
    ("What are the different types of NoSQL databases?", "- **Key-Value Stores** (Redis)\n- **Document Stores** (MongoDB)\n- **Column-Family Stores** (Cassandra)\n- **Graph Databases** (Neo4j)"),
    ("What is the purpose of database constraints?", "Constraints enforce data integrity:\n- **PRIMARY KEY** (ensures uniqueness).\n- **FOREIGN KEY** (enforces referential integrity).\n- **UNIQUE** (prevents duplicates).\n- **CHECK** (validates conditions)."),
    ("What is a deadlock in SQL, and how do you prevent it?", "A deadlock occurs when two transactions block each other, waiting indefinitely.\n- **Prevention:**\n  - Use locking strategies (row-level vs. table-level).\n  - Ensure transactions execute in the same order."),
    ("What is the purpose of database isolation levels?", "Isolation levels control how transactions interact to prevent issues like dirty reads, non-repeatable reads, and phantom reads.\n- **Read Uncommitted** (allows dirty reads).\n- **Read Committed** (prevents dirty reads).\n- **Repeatable Read** (prevents non-repeatable reads).\n- **Serializable** (highest isolation, prevents all concurrency issues)."),
    ("What is a recursive query, and when would you use one?", "A recursive query is used for hierarchical data (e.g., employee-manager relationships or category trees)."),
    ("What is an execution plan, and how can it help optimize queries?", "An execution plan shows how a query will be executed, allowing performance tuning by identifying bottlenecks, missing indexes, and inefficient joins."),
    ("What are the best practices for database security?", "- Use role-based access control (RBAC).\n- Implement encryption for sensitive data.\n- Use parameterized queries to prevent SQL injection.\n- Apply least privilege principle (limit database access)."),\
    ("Write a query to select all columns from a table called employees.", "SELECT * FROM employees;"),
    ("How do you retrieve unique job titles from an employees table?", "SELECT DISTINCT job_title FROM employees;"),
    ("Write a query to get employees hired after January 1, 2020.", "SELECT * FROM employees WHERE hire_date > '2020-01-01';"),
    ("Write a query to find all employees whose name starts with ‘A’.", "SELECT * FROM employees WHERE name LIKE 'A%';"),
    ("Get all employees whose salary is between $50,000 and $100,000.", "SELECT * FROM employees WHERE salary BETWEEN 50000 AND 100000;"),
    ("Write a query to retrieve the top 5 highest-paid employees.", "SELECT * FROM employees ORDER BY salary DESC LIMIT 5;"),
    ("Count the total number of employees in the company.", "SELECT COUNT(*) FROM employees;"),
    ("Find the average salary in the employees table.", "SELECT AVG(salary) FROM employees;"),
    ("Get the department-wise total salary expense.", "SELECT department_id, SUM(salary) AS total_salary FROM employees GROUP BY department_id;"),
    ("Get the minimum and maximum salary in the company.", "SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary FROM employees;"),
    ("Retrieve all employees along with their department names.", "SELECT e.name, d.department_name FROM employees e JOIN departments d ON e.department_id = d.id;"),
    ("Find employees who have not been assigned a department.", "SELECT e.name FROM employees e LEFT JOIN departments d ON e.department_id = d.id WHERE d.id IS NULL;"),
    ("Get a list of customers and their orders (if any).", "SELECT c.name, o.order_id, o.order_date FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id;"),
    ("Retrieve the total number of employees in each department, including departments with zero employees.", "SELECT d.department_name, COUNT(e.id) AS employee_count FROM departments d LEFT JOIN employees e ON d.id = e.department_id GROUP BY d.department_name;"),
    ("Find employees who have the same manager.", "SELECT e1.name AS employee, e2.name AS manager FROM employees e1 JOIN employees e2 ON e1.manager_id = e2.id;"),
    ("Retrieve employees who earn more than the company’s average salary.", "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);") ,
    ("Find employees who work in the same department as ‘John Doe’.", "SELECT * FROM employees WHERE department_id = (SELECT department_id FROM employees WHERE name = 'John Doe');"),
    ("Get the 3rd highest salary from the employees table.", "SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;"),
    ("Retrieve employees who have more than one job role.", "SELECT employee_id FROM job_history GROUP BY employee_id HAVING COUNT(job_id) > 1;"),
    ("Get the names of employees who have placed at least one order.", "SELECT name FROM employees WHERE employee_id IN (SELECT DISTINCT employee_id FROM orders);") ,
    ("Get all orders placed in the last 30 days.", "SELECT * FROM orders WHERE order_date >= NOW() - INTERVAL 30 DAY;") ,
    ("Find employees hired in the current year.", "SELECT * FROM employees WHERE YEAR(hire_date) = YEAR(CURDATE());") ,
    ("Retrieve all employees who have been with the company for more than 5 years.", "SELECT * FROM employees WHERE hire_date <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);") ,
    ("Get the number of orders placed per month in the last year.", "SELECT MONTH(order_date) AS order_month, COUNT(*) AS order_count FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR) GROUP BY MONTH(order_date);") ,
    ("Find employees who were hired on a Monday.", "SELECT * FROM employees WHERE DAYOFWEEK(hire_date) = 2;") ,
    ("Assign a unique rank to employees based on salary.", "SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank FROM employees;") ,
    ("Retrieve the running total of sales per month.", "SELECT order_date, amount, SUM(amount) OVER (ORDER BY order_date) AS running_total FROM sales;") ,
    ("Find the previous salary for each employee.", "SELECT name, salary, LAG(salary) OVER (PARTITION BY department_id ORDER BY hire_date) AS previous_salary FROM employees;") ,
    ("Get the highest salary per department without using GROUP BY.", "SELECT name, salary, department_id, MAX(salary) OVER (PARTITION BY department_id) AS max_salary FROM employees;") ,
    ("Find employees whose salary is above their department’s average.", "SELECT name, salary, department_id FROM employees WHERE salary > AVG(salary) OVER (PARTITION BY department_id);") ,
    ("Insert a new employee into the employees table.", "INSERT INTO employees (name, job_title, salary, hire_date) VALUES ('Jane Doe', 'Analyst', 70000, '2024-02-01');") ,
    ("Update all employees’ salaries by 5%.", "UPDATE employees SET salary = salary * 1.05;") ,
    ("Delete employees who have been inactive for more than 2 years.", "DELETE FROM employees WHERE last_active < DATE_SUB(NOW(), INTERVAL 2 YEAR);"),
    ("What does EXPLAIN do in SQL?", "EXPLAIN helps analyze query performance by showing how the database executes a query, including indexes and execution plans."),
    ("How can you optimize a slow SQL query?", "- Use indexes on frequently searched columns.\n- Avoid SELECT *; retrieve only necessary columns.\n- Use EXISTS instead of IN for subqueries.\n- Optimize joins by ensuring indexed columns are used."),
    ("How do you find duplicate records in a table?", "SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > 1;"),
    ("Retrieve the first 10 rows from a table.", "SELECT * FROM table_name LIMIT 10;"),
    ("Find employees who do not have a manager.", "SELECT * FROM employees WHERE manager_id IS NULL;"),
    ("Retrieve employees working in more than one department.", "SELECT employee_id, COUNT(department_id) FROM employee_departments GROUP BY employee_id HAVING COUNT(department_id) > 1;"),
    ("Show the top 3 selling products.", "SELECT product_id, SUM(sales_amount) AS total_sales FROM sales GROUP BY product_id ORDER BY total_sales DESC LIMIT 3;"),
    ("Get a list of inactive customers (customers with no orders in the last year).", "SELECT * FROM customers WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders WHERE order_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR));"),
    ("Calculate profit margins from sales data.", "SELECT product_id, (SUM(sales_amount) - SUM(cost_amount)) / SUM(sales_amount) * 100 AS profit_margin FROM sales GROUP BY product_id;"),
    ("Retrieve the last 5 orders placed by each customer.", "SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn FROM orders) temp WHERE rn <= 5;"),
    ("Show the highest spending customers.", "SELECT customer_id, SUM(total_price) AS total_spent FROM orders GROUP BY customer_id ORDER BY total_spent DESC LIMIT 10;"),
    ("Find employees with missing phone numbers.", "SELECT * FROM employees WHERE phone_number IS NULL;"),
    ("Get total revenue per quarter.", "SELECT QUARTER(order_date) AS quarter, YEAR(order_date) AS year, SUM(total_price) AS total_revenue FROM orders GROUP BY YEAR(order_date), QUARTER(order_date) ORDER BY year DESC, quarter DESC;"),
    ("Find all employees with the same salary.", "SELECT salary, COUNT(*) FROM employees GROUP BY salary HAVING COUNT(*) > 1;"),
    ("Retrieve order trends over the past year (monthly order count).", "SELECT MONTH(order_date) AS order_month, COUNT(*) AS order_count FROM orders WHERE order_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR) GROUP BY MONTH(order_date) ORDER BY order_month;"),
    ("Find orders that were delivered late.", "SELECT * FROM orders WHERE delivery_date > expected_delivery_date;"),
    ("Identify customers who have not placed an order in the last year.", "SELECT c.* FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.order_date >= DATE_SUB(NOW(), INTERVAL 1 YEAR) WHERE o.order_id IS NULL;")
]

# Initialize session state for question index
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.show_answer = False

def next_question():
    st.session_state.current_index = (st.session_state.current_index + 1) % len(questions)
    st.session_state.show_answer = False

def flip_card():
    st.session_state.show_answer = not st.session_state.show_answer

st.title("Sloan's Flashcard Practice App")
st.image("resy.png", caption="ITS YOUR TIME TO PASS!", use_container_width=True)
# Get current question and answer
question, answer = questions[st.session_state.current_index]

st.subheader("Question:")
st.write(question)

if st.session_state.show_answer:
    st.subheader("Answer:")
    st.write(answer)

col1, col2 = st.columns(2)
with col1:
    st.button("Flip Card", on_click=flip_card)
with col2:
    st.button("Next Question", on_click=next_question)

