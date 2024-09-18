# SQL-Chinook Music Analysis
The Chinook database represents a digital media store, including tables for artists, albums, media tracks, invoices, and customers.

### Dataset 
[Click here to download dataset](https://cdn.fs.teachablecdn.com/dRmwOLQsS22FVFbXfh3x)

### Methodology
1. Data Understanding: Reviewed the structure of the Chinook database, which includes tables for artists, albums, media tracks, invoices, and customers.
2. Objective Definition: To evaluate employee performance, analyze customer and market trends, and catalog insights.
3. Query Formulation:

   Crafted specific SQL queries to extract relevant data for analysis:
    -  Customers (full names, customer ID, and country) not in the US.
    -  Customers specifically from Brazil and then invoices for customers from Brazil.
    -  Employees who are Sales Agents.
    -  Unique list of billing countries from the Invoice table.
    -  Invoices associated with each sales agent.
    -  Show the Invoice Total, Customer name, Country, and Sales Agent name for all invoices and customers.
    -  Identify purchased track names with each invoice line ID.
    -  Identify the purchased track name AND artist name with each invoice line ID.
5. Data Extraction and Analysis:
     - Executed the SQL queries to retrieve and analyze the data.
     - Interpreted the results to draw meaningful insights.

### Database Diagram
The Chinook database has 11 tables in it. This visualization highlights where the tables are related. 
![chinook diagram](https://github.com/clintprentice/SQL-portfolio/SQL-Chinook-Data-Project/blob/main/chinook%20diagram.png)

### Area of Skills

These SQL skills collectively enable complex data retrieval and manipulation, allowing for comprehensive data analysis and insights generation.

#### Summary of SQL Skills Used
- Basic Querying: SELECT, WHERE
- Filtering Data: WHERE, BETWEEN
- Joining Tables: INNER JOIN, LEFT JOIN
- Removing Duplicates: DISTINCT
- Aggregation: COUNT, SUM
- Aliasing: AS
- Complex Joins: Combining multiple tables using various join operations
- Column Selection and Formatting: Selecting specific columns and renaming them for clarity
