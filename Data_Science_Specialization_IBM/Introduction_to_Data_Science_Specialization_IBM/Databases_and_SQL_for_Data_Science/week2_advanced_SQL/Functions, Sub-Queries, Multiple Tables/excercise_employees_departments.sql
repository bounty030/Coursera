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

--sub-queries and nested selects

--select all employees whose salary is greater than the average salary
select * from employees
where salary > (select AVG(salary) from employees);

select EMP_ID, SALARY, 
	(select AVG(salary) from employees) as AVG_SALARY
	from employees;
	
select * from 
	(select emp_id, f_name, l_name, dep_id 
	from employees) as EMP4ALL;
	
select * from employees
	where DEP_ID IN
	(select DEPT_ID_DEP from departments);
	
select * from employees;
select * from departments;

select * from employees
	where dep_id in
	(select dept_id_dep from departments
	where loc_id = 'L0002');
	
select dept_id_dep, dep_name from departments 
	where dept_id_dep in 
	(select dep_id from employees
	where SALARY > 70000);
	
select * from employees, departments
	where employees.dep_id = departments.dept_id_dep;