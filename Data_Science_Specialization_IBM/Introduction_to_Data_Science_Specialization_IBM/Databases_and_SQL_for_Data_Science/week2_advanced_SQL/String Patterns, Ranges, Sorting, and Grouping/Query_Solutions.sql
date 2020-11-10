------------------------------------------
--DDL statement for table 'HR' database--
--------------------------------------------

--Query 1: Retrieve all employees whose address is in Elgin,IL [Hint: Use the LIKE operator to find similar strings]
SELECT f_name, l_name
FROM EMPLOYEES
WHERE address LIKE '%Elgin,IL'; 

--Query 2: Retrieve all employees who were born during the 1970's.
SELECT f_name, l_name
FROM EMPLOYEES
WHERE b_date LIKE '%197%'; 

--Query 3: Retrieve all employees in department 5 whose salary is between 60000 and 70000 . 
--[Hint: Use the keyword BETWEEN for this query ]

SELECT f_name, l_name
FROM EMPLOYEES
WHERE SALARY BETWEEN '60000' and '70000'; 

--Query 4A: Retrieve a list of employees ordered by department ID. 
--[Hint: Use the ORDER BY clause for this query]

SELECT dep_id, f_name, l_name
FROM EMPLOYEES
ORDER BY dep_id; 

--Query 4B: Retrieve a list of employees ordered in descending order by department ID and within each 
--department ordered alphabetically in descending order by last name.
SELECT dep_id, f_name, l_name
FROM EMPLOYEES
ORDER BY dep_id, l_name DESC;

--Query 5A: For each department ID retrieve the number of employees in the department. 
--[Hint: Use COUNT(*) to retrieve the total count of a column, and then GROUP BY]
SELECT dep_id,
COUNT(dep_id) as count
FROM EMPLOYEES
GROUP BY dep_id;

--Query 5B: For each department retrieve the number of employees in the department, 
--and the average employees salary in the department. 
--[Hint: Use COUNT(*) to retrieve the total count of a column, and AVG() function to compute 
--average salaries, and then group]
SELECT dep_id,
COUNT(dep_id) as total_employees,
AVG(salary) as avg_salary
FROM EMPLOYEES
GROUP BY dep_id;

--Query 5C: Label the computed columns in the result set of Query 5B as “NUM_EMPLOYEES” and 
--“AVG_SALARY”. 
--[Hint: Use AS “LABEL_NAME” after the column name]
SELECT dep_id,
COUNT(dep_id) as num_employees,
AVG(salary) as avg_salary
FROM EMPLOYEES
GROUP BY dep_id;

--Query 5D: In Query 5C order the result set by Average Salary. 
--[Hint: Use ORDER BY after the GROUP BY]
SELECT dep_id,
COUNT(dep_id) as num_employees,
AVG(salary) as avg_salary
FROM EMPLOYEES
GROUP BY dep_id
ORDER BY avg_salary DESC;

--Query 5E: In Query 5D limit the result to departments with fewer than 4 employees. 
--[Hint: Use HAVING after the GROUP BY, and use the count() function in the HAVING clause 
--instead of the column label. Note: WHERE clause is used for filtering the entire result set 
--whereas the HAVING clause is used for filtering the result of the grouping]
SELECT dep_id,
COUNT(dep_id) as num_employees,
AVG(salary) as avg_salary
FROM EMPLOYEES
GROUP BY dep_id having COUNT(dep_id)<4
ORDER BY avg_salary DESC;

--BONUS 
--Query 6: Similar to 4B but instead of department ID use department name. 
--Retrieve a list of employees ordered by department name, and within each department 
--ordered alphabetically in descending order by last name. 
--[Hint: Department name is in the DEPARTMENTS table. So your query will need to 
--retrieve data from more than one table. Don’t worry if you are not able to figure 
--this one out … we’ll cover working with multiple tables in the next lesson.]
SELECT D.DEP_NAME, E.L_NAME, E.F_NAME
FROM EMPLOYEES as E, DEPARTMENTS as D
WHERE E.DEP_ID=D.DEPT_ID_DEP
ORDER BY D.DEP_NAME, E.L_NAME DESC;