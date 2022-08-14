# Write your MySQL query statement below
SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM salaries WHERE salary IS NOT NULL) 
    UNION 
SELECT employee_id FROM salaries WHERE employee_id NOT IN (SELECT employee_id FROM Employees WHERE name IS NOT NULL) 
    ORDER BY employee_id;